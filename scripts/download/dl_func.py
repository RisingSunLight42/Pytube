from pytube import YouTube
from os import rename
from os.path import splitext

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
    file_path = file_path.split(".")[0] # Retire l'extension du fichier enregistré, pouvant être fausse
    print(f"La vidéo '{stream.title}' a bien été enregistrée dans le chemin ci-contre :\n{file_path}")

def telechargement(path: str, url: str, audio_ou_video: str) -> None:
    """Fonction permettant de télécharger une vidéo.

    Args:
        path (str): chemin d'accès du fichier
        url (str): lien de la vidéo
        audio_ou_video (str): si on veut un fichier .mp4 ou .mp3
    """
    video = YouTube(url,
                    on_progress_callback=on_progress,
                    on_complete_callback=on_complete,) # Crée l'objet Youtube correspondant à la vidéo
    
    # Réalise le téléchargement
    if audio_ou_video.upper() == "AUDIO": # Si l'utilisateur a demandé un audio
        flux_audio_dl = video.streams.filter(only_audio=True)[0]
        sortie_dl = flux_audio_dl.download(filename=flux_audio_dl.default_filename.replace(" ", "_"),
                            output_path=path) # Télécharge le flux audio, en remplaçant les espaces du nom de fichier par des "_" au chemin d'accès spécifié
        chemin, extension = splitext(sortie_dl) # splitext sépare le chemin d'accès du fichier et son extension
        sortie_dl_rename = f"{chemin}.mp3" # Modifie le chemin pour mettre l'extension .mp3 et pas mp4
        rename(sortie_dl, sortie_dl_rename) # Rename le fichier  avec le nouveau nom
    elif audio_ou_video.upper() == "VIDEO": # Si l'utilisateur a demandé une video
        streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
        flux_video_dl = streams_progressive.get_highest_resolution() # Stocke le flux vidéo que l'on souhaite télécharger, avec la qualité la plus haute possible
        flux_video_dl.download(filename=flux_video_dl.default_filename.replace(" ", "_"),
                            output_path=path) # Télécharge le flux, en remplaçant les espaces du nom de fichier par des "_" au chemin d'accès spécifié
    else: # Si le mot clé ne colle pas
        print("Le mot clé que tu m'as donné est incorrect !")
