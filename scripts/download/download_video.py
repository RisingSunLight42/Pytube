from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=4bUBotqLdbc") # Crée l'objet Youtube correspondant à la vidéo
streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
streams_progressive.get_highest_resolution().download() # Télécharge la qualité la plus haute