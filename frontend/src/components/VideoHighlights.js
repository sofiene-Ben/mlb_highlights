const videos = [
    { id: "1", title: "Résumé Dodgers vs Rockies", url: "https://www.youtube.com/embed/xxx1" },
    { id: "2", title: "Résumé Giants vs Yankees", url: "https://www.youtube.com/embed/xxx2" },
    { id: "3", title: "Résumé Red Sox vs Cubs", url: "https://www.youtube.com/embed/xxx3" },
  ];
  
  const VideoHighlights = () => {
    return (
      <div className="space-y-4">
        {videos.map((video) => (
          <div key={video.id} className="p-4 bg-white shadow-md rounded-lg">
            <h3 className="text-lg font-semibold">{video.title}</h3>
            <iframe title={video.title} className="w-full h-56 mt-2" src={video.url} allowFullScreen></iframe>
          </div>
        ))}
      </div>
    );
  };
  
  export default VideoHighlights;
  