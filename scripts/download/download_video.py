from pytube import YouTube

# Définit les fonctions de progression du téléchargement
def on_progress(stream, chunk, bytes_remaining):
    """Fonction appelée lorsque le téléchargement est en cours.

    Args:
        stream (stream object): objet contenant les différentes informations du fichier vidéo
        chunk (chunk object): segment de données binaires encore non écrites sur le disque
        bytes_remaining (int): quantité de bytes restants à télécharger
    """
    progression = (1 - bytes_remaining / stream.filesize) * 100
    print(f"{round(progression, 2)} %")

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
audio_ou_video = input("Veux-tu télécharger uniquement un fichier AUDIO ou un fichier VIDEO (répondre par AUDIO ou VIDEO) ") # Demande ce que veut l'utilisateur
if audio_ou_video == "AUDIO": # Si l'utilisateur a demandé un audio
    flux_audio_dl = video.streams.filter(only_audio=True)[0]
    flux_audio_dl.download(filename=flux_audio_dl.default_filename.replace(" ", "_")) # Télécharge le flux audio, en remplaçant les espaces du nom de fichier par des "_"
elif audio_ou_video == "VIDEO": # Si l'utilisateur a demandé une video
    streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
    flux_video_dl = streams_progressive.get_highest_resolution() # Stocke le flux vidéo que l'on souhaite télécharger, avec la qualité la plus haute possible
    flux_video_dl.download(filename=flux_video_dl.default_filename.replace(" ", "_")) # Télécharge le flux, en remplaçant les espaces du nom de fichier par des "_"
else: # Si le mot clé ne colle pas
    print("Le mot clé que tu m'as donné est incorrect !")