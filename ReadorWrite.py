# fichier = open("data.txt", "a")
# fichier.write("Bonjour monde")
# fichier.close()

# fichier = open("data.txt", "a")
# fichier.write("\nBonjour monde")
# fichier.close()
# Définir le chemin du fichier à lire
nom_fichier = "fichier.txt"

# Définir le chemin du fichier à lire
# nom_fichier = "chemin/vers/le/fichier.txt"

try:
    with open(nom_fichier, 'r') as fichier:
# fichier.write("Bonjour monde")
        contenu = fichier.read()

    if contenu.strip():
        # Afficher le contenu uniquement si le fichier n'est pas vide
        print(contenu)
    else:
        print("Le fichier est vide.")

except FileNotFoundError:
    print("Le fichier spécifié est introuvable.")

except IOError:
    print("Une erreur s'est produite lors de la lecture du fichier.")

except Exception as e:
    print("Une erreur inattendue s'est produite:", str(e))

finally:
    print("Lecture du fichier terminée.")