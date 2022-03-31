from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=q73RiLr9GHU")
streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)