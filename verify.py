import re

# Définir le chemin du fichier à lire
nom_fichier = "fichier.txt"

# Les éléments que vous souhaitez rechercher (sous forme de motifs regex)
elements_a_rechercher = [r'dsjf;somme']

try:
    # Ouvrir le fichier en mode lecture ('r' pour read)
    with open(nom_fichier, 'r') as fichier:
        # Lire toutes les lignes du fichier dans une liste
        lignes = fichier.readlines()

    # Le fichier est automatiquement fermé après la sortie du bloc 'with'

    # Parcourir chaque ligne et rechercher les éléments avec les motifs regex
    for ligne in lignes:
        for element in elements_a_rechercher:
            if re.search(element, ligne):
                print(f"L'élément '{element}' se trouve dans le fichier.")

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print("Vérification du fichier terminée.")
