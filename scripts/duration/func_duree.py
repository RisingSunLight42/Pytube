from typing import Tuple

# Fonction permettant de calculer la durée
def duree(duree_totale_seconde: int) -> Tuple[int]:
    """Fonction calculant l'équivalent en heure(s), minute(s), seconde(s)
    d'une valeur de seconde(s)

    Args:
        duree_totale_seconde (int): valeur en seconde que l'on souhaite convertir

    Returns:
        Tuple[int]: sous la forme (heure, minute, seconde)
    """
    heure = duree_totale_seconde // 3600
    duree_totale_seconde -= (duree_totale_seconde // 3600) * 3600 # Retire les secondes correspondant au nombre d'heures de la durée totale
    minute = duree_totale_seconde // 60
    duree_totale_seconde -= (duree_totale_seconde // 60) * 60 # Retire les secondes correspondant au nombre de minutes de la durée totale
    seconde = duree_totale_seconde # La durée totale restante correspond aux secondes (variable crée pour une meilleure lisibilitée)
    return heure, minute, seconde