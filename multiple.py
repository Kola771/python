import re

# Définir le chemin du fichier à lire/écrire
nom_fichier = "fichier.txt"

# L'élément que vous souhaitez remplacer et sa chaîne de remplacement
element_a_remplacer = r'Bonjour'
chaîne_de_remplacement = 'remplacement'

try:
    # Ouvrir le fichier en mode lecture ('r' pour read)
    with open(nom_fichier, 'r') as fichier:
        # Lire tout le contenu du fichier
        contenu = fichier.read()

    # Le fichier est automatiquement fermé après la sortie du bloc 'with'

    # Effectuer le remplacement en utilisant re.sub() avec le drapeau re.MULTILINE
    contenu_modifie = re.sub(element_a_remplacer, chaîne_de_remplacement, contenu, flags=re.MULTILINE)

    # Ouvrir le fichier en mode écriture ('w' pour write) pour écrire le contenu modifié
    with open(nom_fichier, 'w') as fichier:
        # Écrire le contenu modifié dans le fichier
        fichier.write(contenu_modifie)

    print(f"Remplacement de '{element_a_remplacer}' par '{chaîne_de_remplacement}' effectué avec succès.")

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture/écriture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print("Opération terminée.")
