import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const ArticleDetail = () => {
  const { id } = useParams(); // 🔥 Récupération de l'ID depuis l'URL
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchArticle = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/favorite-team/articles/${id}`, {
          credentials: "include",
          headers: {
            "Authorization": `Bearer ${localStorage.getItem("access_token")}`,
            "Content-Type": "application/json"
          }
        });

        if (!response.ok) throw new Error("Impossible de récupérer l'article");

        const data = await response.json();
        setArticle(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchArticle();
  }, [id]);

  if (loading) return <p>Loading article...</p>;
  if (error) return <p>Error : {error}</p>;

  return (
    <div className="article-detail-block color-black p-6 max-w-2xl mx-auto bg-white shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold">{article.team_name} - {article.opponent_team} <span className="date-match">({new Date(article.game_date).toLocaleDateString()})</span></h2>
      <p className="text-gray-600 mt-2">{article.text_summary}</p>
    </div>
  );
};

export default ArticleDetail;
