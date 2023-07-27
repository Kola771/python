# Définir le chemin du fichier à lire
nom_fichier = "fichier.txt"
try:
    # Ouvrir le fichier en mode lecture ('r' pour read)
    with open(nom_fichier, 'r') as fichier:
        # Lire toutes les lignes du fichier dans une liste
        lignes = fichier.readlines()

    # Le fichier est automatiquement fermé après la sortie du bloc 'with'
    
    # Afficher le contenu sous forme de liste (chaque élément de la liste est une ligne du fichier)
    print(lignes)

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print("Lecture du fichier terminée.")