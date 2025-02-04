const audios = [
    { id: "1", title: "Podcast Dodgers vs Rockies", url: "/audios/dodgers.mp3" },
    { id: "2", title: "Podcast Giants vs Yankees", url: "/audios/giants.mp3" },
    { id: "3", title: "Podcast Red Sox vs Cubs", url: "/audios/redsox.mp3" },
  ];
  
  const AudioHighlights = () => {
    return (
      <div className="space-y-4">
        {audios.map((audio) => (
          <div key={audio.id} className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-lg font-semibold">{audio.title}</h3>
            <audio controls className="w-full mt-2">
              <source src={audio.url} type="audio/mpeg" />
              Votre navigateur ne supporte pas l'élément audio.
            </audio>
          </div>
        ))}
      </div>
    );
  };
  
  export default AudioHighlights;
  