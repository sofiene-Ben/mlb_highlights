import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const PreferencesButton = () => {
  const navigate = useNavigate();
  const [hasPreferences, setHasPreferences] = useState(null);

  useEffect(() => {
    // Appel API pour vérifier si l'utilisateur a des préférences
    const fetchPreferences = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/user/favorite-team/", {
            credentials: "include", // Si tu utilises des cookies pour l'authentification
            headers: {
              "Authorization": `Bearer ${localStorage.getItem("access_token")}`, // Si tu utilises un token JWT stocké
              "Content-Type": "application/json"
            }
          });
        const data = await response.json();
        setHasPreferences(data.favorite_team); // Supposons que l'API renvoie { exists: true/false }
      } catch (error) {
        console.error("Erreur lors de la récupération des préférences", error);
      }
    };

    fetchPreferences();
  }, []);

  const handleClick = () => {
    if (hasPreferences) {
      navigate("/highlights/");
    } else {
      navigate("/preferences/");
    }
  };

  return <button onClick={handleClick}>Start!</button>;
};

export default PreferencesButton;
