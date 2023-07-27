import re

# Définir le chemin du fichier à lire/écrire
nom_fichier = "fichier.txt"

# Les éléments que vous souhaitez remplacer et leur chaîne de remplacement (sous forme de tuples)
remplacements = [
    (r'dsjf;somme', 'Bonjour tout le monde')
]

try:
    # Ouvrir le fichier en mode lecture ('r' pour read)
    with open(nom_fichier, 'r') as fichier:
        # Lire tout le contenu du fichier
        contenu = fichier.read()

    # Le fichier est automatiquement fermé après la sortie du bloc 'with'

    # Effectuer les remplacements en utilisant re.sub()
    for recherche, remplacement in remplacements:
        contenu = re.sub(recherche, remplacement, contenu)

    # Ouvrir le fichier en mode écriture ('w' pour write) pour écrire le contenu modifié
    with open(nom_fichier, 'w') as fichier:
        # Écrire le contenu modifié dans le fichier
        fichier.write(contenu)

    print("Remplacements effectués avec succès.")

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture/écriture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print("Opération terminée.")
