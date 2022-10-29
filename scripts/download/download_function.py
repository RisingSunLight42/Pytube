from pytube import YouTube, Stream
import moviepy.editor as mpe
from os import rename, remove
from os.path import splitext
from typing import Tuple


def on_progress(stream, chunk, bytes_remaining) -> None:
    """Fonction appelée lorsque le téléchargement est en cours.

    Args:
        stream (stream object): objet contenant les différentes informations du fichier vidéo
        chunk (chunk object): segment de données binaires encore non écrites sur le disque
        bytes_remaining (int): quantité de bytes restants à télécharger
    """
    progression = (1 - bytes_remaining / stream.filesize) * 100
    print(f"{round(progression, 2)} %")


def on_complete(stream: Stream, file_path) -> None:
    """Fonction appelée lorsque le téléchargement est terminé

    Args:
        stream (stream object): objet contenant les différentes informations du fichier vidéo
        file_path (str): chemin d'accès vers le fichier vidéo
    """
    if (stream.type == "audio"):
        file_path = file_path.split(".")[0] + ".mp3"
        print(
            f"L'audio de la vidéo '{stream.title}' a bien été enregistré dans le chemin ci-contre :\n{file_path}")
    else:
        print(
            f"La vidéo '{stream.title}' (sans audio) a bien été enregistrée dans le chemin ci-contre :\n{file_path}")


def combine_audio(vidname: str, audname: str, outname: str, fps=60) -> None:
    """Fonction permettant de combiner l'audio à une vidéo

    Args:
        vidname (str): nom du fichier vidéo
        audname (str): nom du fichier audio
        outname (str): nom du fichier de sortie
        fps (int, optional): FPS de la vidéo. Par défaut à 60.
    """
    print("Début de la combinaison du fichier audio et vidéo pour obtenir la vidéo complète...")
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=fps)


def telechargement_audio(video: YouTube, path: str) -> str:
    """Fonction qui permet de télécharger le son d'une vidéo

    Args:
        video (YouTube): objet représentant l'audio de la vidéo à télécharger
        path (str): chemin d'accès du fichier

    Returns:
        str: renvoie le chemin d'accès de l'audio
    """
    audio_flux: Stream = video.streams.filter(only_audio=True)[0]
    sortie_dl = audio_flux.download(filename=audio_flux.default_filename.replace(" ", "_"),
                                    output_path=path)
    chemin, extension = splitext(sortie_dl)
    sortie_dl_rename = f"{chemin}.mp3"
    rename(sortie_dl, sortie_dl_rename)
    return sortie_dl_rename


def telechargement_video(video: YouTube, path: str) -> Tuple[str]:
    """Fonction qui permet de télécharger une vidéo au maximum de sa qualité (sans son)

    Args:
        video (YouTube): objet représentant la vidéo à télécharger
        path (str): chemin d'accès du fichier

    Returns:
        Tuple[str]: tuple de deux éléments, un avec le nom du fichier téléchargé sans son, et un pour le fichier avec son
    """
    streams_progressive = video.streams.filter(adaptive=True)
    video_flux: Stream = streams_progressive[0]
    filename = video_flux.default_filename.replace(" ", "_")
    video_flux.download(filename=f"withoutsound_{filename}", output_path=path)
    return f"{path}/withoutsound_{filename}", f"{path}/{filename}"


def telechargement(path: str, url: str, audio_ou_video: str) -> None:
    """Fonction permettant de télécharger une vidéo.

    Args:
        path (str): chemin d'accès du fichier
        url (str): lien de la vidéo
        audio_ou_video (str): si on veut un fichier .mp4 ou .mp3
    """
    video = YouTube(url,
                    on_progress_callback=on_progress,
                    on_complete_callback=on_complete,)  # Crée l'objet Youtube correspondant à la vidéo

    if audio_ou_video == "A":
        telechargement_audio(video, path)
    elif audio_ou_video == "V":
        nomAudio = telechargement_audio(video, path)
        nomVideo = telechargement_video(video, path)
        combine_audio(nomVideo[0], nomAudio, nomVideo[1])
        remove(nomAudio)
        remove(nomVideo[0])
    else:
        print("Le mot clé que tu m'as donné est incorrect !")
