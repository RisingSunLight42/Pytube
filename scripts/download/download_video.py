from pytube import YouTube

# Définit les fonctions de progression du téléchargement
def on_progress(stream, chunk, bytes_remaining):
    pass

def on_complete(stream, file_path):
    """Fonction appelée lorsque le téléchargement est terminé

    Args:
        stream (stream object): objet contenant les différentes informations du fichier vidéo
        file_path (str): chemin d'accès vers le fichier vidéo
    """
    print(f"La vidéo '{stream.title}' a bien été enregistrée dans le chemin ci-contre :\n{file_path}")

# Demande le lien de la vidéo et la télécharge
url = input("Donne-moi un lien de vidéo à télécharger ! ") # Demande le lien de la vidéo
video = YouTube(url,
                on_progress_callback=on_progress,
                on_complete_callback=on_complete,) # Crée l'objet Youtube correspondant à la vidéo
streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
streams_progressive.get_highest_resolution().download() # Télécharge la qualité la plus haute