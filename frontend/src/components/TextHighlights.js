import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const TextHighlights = () => {
  const navigate = useNavigate();
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFavoriteTeamArticles = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/favorite-team/articles/", {
          credentials: "include", // Si tu utilises des cookies pour l'authentification
          headers: {
            "Authorization": `Bearer ${localStorage.getItem("access_token")}`, // Si tu utilises un token JWT stocké
            "Content-Type": "application/json"
          }
        });

        if (!response.ok) throw new Error("Impossible de récupérer les articles");

        const data = await response.json();
        console.log("Réponse API:", data);

        // Trier les articles par date de jeu (du plus récent au plus ancien)
        const sortedArticles = data.articles.sort((a, b) => new Date(b.game_date) - new Date(a.game_date));

        
        setArticles(sortedArticles);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchFavoriteTeamArticles();
  }, []);

  if (loading) return <p>Loading articles...</p>;
  if (error) return <p>Error : {error}</p>;

  return (
    <div className="article-list space-y-4">
      {articles.map((article) => (
        <div
          key={article.id}
          className="article-item p-4 bg-white shadow-md rounded-lg cursor-pointer hover:bg-gray-100"
          onClick={() => navigate(`/article/${article.id}`)}
        >
          <h3 className="text-lg font-semibold">{article.team_name} - {article.opponent_team} <span className="date-match">({new Date(article.game_date).toLocaleDateString()})</span> </h3>
          <p className="text-gray-600">{article.text_summary.slice(0, 200)}... <a href={`/article/${article.id}`}>read more</a></p>
        </div>
      ))}
    </div>
  );
};

export default TextHighlights;

