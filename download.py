# import urllib.request
# import tempfile
# import shutil

# url = 'URL_DU_FICHIER_ZIP'

# try:
#     # Effectuer la requête pour récupérer le contenu du fichier
#     with urllib.request.urlopen(url) as response:
#         # Lire le contenu du fichier
#         data = response.read()

#     # Créer un fichier temporaire
#     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(data)
#         temp_file.flush()

#         # Obtenir le chemin du fichier temporaire
#         chemin_fichier_temporaire = temp_file.name

#     # Vous pouvez faire ce que vous voulez avec le fichier temporaire ici
#     # Par exemple, vous pouvez extraire le contenu du fichier zip ou le manipuler d'une autre manière

#     print("Téléchargement réussi !")

# except Exception as e:
#     print(f"Une erreur s'est produite lors du téléchargement : {e}")


import os
import urllib.request
import zipfile

def telecharger_et_extraire_zip(url):
    # Téléchargement du fichier ZIP
    nom_fichier_zip = url.split('/')[-1]

    try:
        print("Téléchargement en cours...")
        urllib.request.urlretrieve(url, nom_fichier_zip)
        print("Téléchargement terminé.")
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement :", e)
        return

    # Extraction du contenu du fichier ZIP
    try:
        print("Extraction en cours...")
        with zipfile.ZipFile(nom_fichier_zip, 'r') as zip_ref:
            zip_ref.extractall()
        print("Extraction terminée.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'extraction :", e)
        return

# Exemple d'utilisation :
url_fichier_zip = 'file:///C:/Users/kolade.aboudou/Desktop/cours%20python/test/resultats.zip'

telecharger_et_extraire_zip(url_fichier_zip)
