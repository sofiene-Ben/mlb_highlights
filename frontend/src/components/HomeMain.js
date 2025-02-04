import React from "react";
import { useNavigate } from "react-router-dom";
import PreferencesButton from "./PreferencesButton";


const HomeMain = () => {
  const navigate = useNavigate();

    return (
      <main className="main">
        <video src="/YjlLTlpfWGw0TUFRPT1fQTFOVFVWQU1Vd0lBQVFjRFVnQUFDVkpVQUZsWEFnY0FVVlpRQVFGUVVsRUFCZ29D.mp4" autoPlay loop muted></video>
        <div className="main-content">
          <h1>Follow your favorite players and teams!</h1>
          <p>Get the best moments, highlights, and commentary in one click.</p>
          {/* <button onClick={() => navigate(`/preferences/`)}>Commencer !</button> */}
          <PreferencesButton />
        </div>
      </main>
    );
  };
  
  export default HomeMain;