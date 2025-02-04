import { useState } from "react";
import TextHighlights from "../components/TextHighlights";
import VideoHighlights from "../components/VideoHighlights";
import AudioHighlights from "../components/AudioHighlights";

const HighlightsPage = () => {
  const [activeTab, setActiveTab] = useState("text"); // Texte par défaut

  return (
    <div className="container highlights-container">
      <h1>My Highlights</h1>

      {/* Boutons pour changer d'affichage */}
      <div className="tabs">
        <button className={activeTab === "text" ? "active" : ""} onClick={() => setActiveTab("text")}>
          Text
        </button>
        <button disabled className={activeTab === "video" ? "active" : ""} style={{backgroundColor: "grey"}} onClick={() => setActiveTab("video")}>
          Video
        </button>
        <button disabled className={activeTab === "audio" ? "active" : ""} style={{backgroundColor: "grey"}}  onClick={() => setActiveTab("audio")}>
          Audio
        </button>

      </div>

      {/* Affichage dynamique des composants */}
      {activeTab === "text" && <TextHighlights />}
      {activeTab === "video" && <VideoHighlights />}
      {activeTab === "audio" && <AudioHighlights />}
    </div>
  );
};

export default HighlightsPage;
