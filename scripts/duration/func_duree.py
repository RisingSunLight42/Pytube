from typing import Tuple


def duree(dureeTotaleSeconde: int) -> Tuple[int]:
    """Fonction calculant l'équivalent en heure(s), minute(s), seconde(s)
    d'une valeur de seconde(s)

    Args:
        duree_totale_seconde (int): valeur en seconde que l'on souhaite convertir

    Returns:
        Tuple[int]: sous la forme (heure, minute, seconde)
    """
    heure = dureeTotaleSeconde // 3600
    dureeTotaleSeconde -= heure * 3600
    minute = dureeTotaleSeconde // 60
    dureeTotaleSeconde -= minute * 60
    seconde = dureeTotaleSeconde
    return heure, minute, seconde
