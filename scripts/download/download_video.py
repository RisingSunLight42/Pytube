from pytube import YouTube

# Définit les fonctions de progression du téléchargement
def on_progress():
    pass

def on_complete():
    pass

# Demande le lien de la vidéo et la télécharge
url = input("Donne-moi un lien de vidéo à télécharger ! ") # Demande le lien de la vidéo
video = YouTube(url,
                on_progress_callback=on_progress,
                on_complete_callback=on_complete,) # Crée l'objet Youtube correspondant à la vidéo
streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
streams_progressive.get_highest_resolution().download() # Télécharge la qualité la plus haute