import re

# Définir le chemin du fichier à lire
nom_fichier = "fichier.txt"

# Le mot que vous souhaitez rechercher
mot_a_rechercher = "remplacement"

# Liste pour stocker les occurrences trouvées
occurrences = []

try:
    # Ouvrir le fichier en mode lecture ('r' pour read)
    with open(nom_fichier, 'r') as fichier:
        # Lire tout le contenu du fichier
        contenu = fichier.read()

    # Le fichier est automatiquement fermé après la sortie du bloc 'with'

    # Utiliser re.findall() pour trouver toutes les occurrences du mot dans le contenu
    occurrences = re.findall(r'\b' + re.escape(mot_a_rechercher) + r'\b', contenu, flags=re.IGNORECASE)

    # Le drapeau re.IGNORECASE permet d'effectuer une recherche insensible à la casse
    # Le \b avant et après le motif assure que nous trouvons des mots entiers, pas des sous-chaînes

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print(f"Nombre d'occurrences de '{mot_a_rechercher}' dans le fichier : {len(occurrences)}")
    print("Occurrences trouvées :", occurrences)
