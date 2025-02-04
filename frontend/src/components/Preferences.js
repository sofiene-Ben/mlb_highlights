import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
// import axios from "axios";

const Preferences = () => {
  const navigate = useNavigate();
  const [preferences, setPreferences] = useState({
    notifications: true,
    favoritePlayer: "645277",
    favoriteTeam: "119",
    media: "audio",
    frequency: "daily",
  });
  const [message, setMessage] = useState(""); // Stocker les messages de succès/erreur ici
  

  // Gestion des changements dans les préférences
  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setPreferences({
      ...preferences,
      [name]: type === "checkbox" ? checked : value,
  
    });
  };



  // Soumission des préférences (à connecter à un backend pour sauvegarde)
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Préférences sauvegardées :", preferences);
    alert("Vos préférences ont été sauvegardées !");

    const accessToken = localStorage.getItem("access_token");  // Récupérer le token
    if (!accessToken) {
      console.log("Token manquant. Veuillez vous connecter.");
      return;
    }

    const formData = new URLSearchParams({
      media_type: preferences.media,  // Assurez-vous que 'preferences.media' a une valeur
      recurrence: preferences.frequency,  // Idem pour 'preferences.frequency'
      fav_player: preferences.favoritePlayer,  // Idem pour 'preferences.favoritePlayer'
      fav_team: preferences.favoriteTeam,  // Idem pour 'preferences.favoriteTeam'
    });

    try {
      const response = await fetch("http://localhost:8000/api/submit-preferences/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: `Bearer ${accessToken}`, // Passer le JWT ici
        },
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setMessage("Préférences mises à jour avec succès !");
        console.log("Réponse du serveur :", data);
        navigate("/highlights");  // Remplace "/preferences-saved" par l'URL où tu veux rediriger l'utilisateur
      } else {
        const errorData = await response.json();
        setMessage(`Erreur : ${errorData.detail}`);
        console.error("Erreur du serveur :", errorData);
      }
    } catch (error) {
      console.error("Erreur réseau :", error);
      setMessage("Erreur réseau. Impossible de se connecter à l'API.");
    }
  };





//   ###########################

    const [players, setPlayers] = useState([]); // Stockage des joueurs
    const [selectedPlayerId, setSelectedPlayerId] = useState(""); // ID sélectionné
  
    // Récupérer les joueurs depuis l'API
    const fetchPlayers = async () => {
      try {
        const response = await fetch("https://statsapi.mlb.com/api/v1/sports/1/players?season=2025");
        const data = await response.json();
        setPlayers(data.people || []); // Stocker les joueurs dans l'état
      } catch (error) {
        console.error("Erreur lors de la récupération des joueurs :", error);
      }
    };
  
    // Charger les joueurs au montage du composant
    useEffect(() => {
      fetchPlayers();
    }, []);
  
    // Gérer le changement de sélection
    const handleSelectPlayerChange = (event) => {
      setSelectedPlayerId(event.target.value); // Met à jour l'ID sélectionné
      setPreferences((prev) => ({
        ...prev,
        favoritePlayer: event.target.value,
      }));
      console.log("ID du joueur sélectionné :", event.target.value);
    };






// #############################  



    const [teams, setTeams] = useState([]); // Stockage des équipes
    const [selectedTeamId, setSelectedTeamId] = useState(""); // ID de l'équipe sélectionnée
  
    // Récupérer les équipes depuis l'API
    const fetchTeams = async () => {
      try {
        const response = await fetch("https://statsapi.mlb.com/api/v1/teams?sportId=1");
        const data = await response.json();
        setTeams(data.teams || []); // Stocker les équipes dans l'état
      } catch (error) {
        console.error("Erreur lors de la récupération des équipes :", error);
      }
    };
  
    // Charger les équipes au montage du composant
    useEffect(() => {
      fetchTeams();
    }, []);
  
    const handleSelectTeamChange = (event) => {
        setSelectedTeamId(event.target.value); // Met à jour l'ID sélectionné
        setPreferences((prev) => ({
          ...prev,
          favoriteTeam: event.target.value,
        }));
        console.log("ID de l'équipe sélectionnée :", event.target.value);
      };


      
// #############################  

// Gestion des modifications pour le format média
const handleSelectMediaChange = (event) => {
  setPreferences((prev) => ({
    ...prev,
    media: event.target.value,
  }));
  console.log("Format sélectionné :", event.target.value);
};

// Gestion des modifications pour la fréquence
const handleSelectFrequencyChange = (event) => {
  setPreferences((prev) => ({
    ...prev,
    frequency: event.target.value,
  }));
  console.log("Fréquence sélectionnée :", event.target.value);
};

  return (
    <div className="container preferences-container bg-gray-100 p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-blue-900">My Preferences</h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Notifications */}
        <div className="preference-item">
          <label className="flex items-center space-x-3">
            <input
              type="checkbox"
              name="notifications"
              checked={preferences.notifications}
              onChange={handleInputChange}
              className="h-5 w-5 text-blue-600"
            />
            <span className="text-gray-700">Enable notifications</span>
          </label>
        </div>

        {/* Sélection d'équipe favorite */}
        <div className="preference-item">
          <label className="block text-gray-700 font-medium mb-2">
          Favorite team :
          </label>
          <select
            name="favoriteTeam"
            value={selectedTeamId}
            onChange={handleSelectTeamChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            <option value="">-- Choose a team --</option>
            {teams.map((team) => (
            <option key={team.id} value={team.id}>
                {team.name}
            </option>
            ))}
          </select>
          {/* {selectedTeamId && (
        <p>
          Équipe sélectionnée :{" "}
          {teams.find((team) => team.id.toString() === selectedTeamId)?.name || ""}
        </p>
      )} */}
        </div>

        {/* Sélection du joueur favori */}

        <div className="preference-item">
          <label className="block text-gray-700 font-medium mb-2">
            Favorite player :
          </label>
          <select
            name="favoriteplayer"
            value={selectedPlayerId}
            onChange={handleSelectPlayerChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            <option value="">-- Choose a player --</option>
            {players.map((player) => (
            <option key={player.id} value={player.id}>
                {player.fullName}
            </option>
            ))}
          </select>
        </div>

        {/* Format audio, video ou text */}
        <div className="preference-item">
          <label className="block text-gray-700 font-medium mb-2">
            Format :
          </label>
          <select
            name="format"
            value={preferences.media}
            onChange={handleSelectMediaChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            <option value="audio">Audio</option>
            <option value="video">Video</option>
            <option value="text">Texte</option>
          </select>
        </div>

        {/* Frequence d'envoi */}
        <div className="preference-item">
          <label className="block text-gray-700 font-medium mb-2">
          Sending frequency :
          </label>
          <select
            name="frequency"
            value={preferences.frequency}
            onChange={handleSelectFrequencyChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            <option value="daily">Daily</option>
            <option value="weekly">weekly</option>
            <option value="monthly">monthly</option>
          </select>
        </div>


        {/* Bouton de soumission */}
        <div>
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
          >
            Save my preferences
          </button>
        </div>
      </form>
    </div>
  );
};

export default Preferences;
