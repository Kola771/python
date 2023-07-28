import urllib.request
import tempfile
import shutil

url = 'URL_DU_FICHIER_ZIP'

try:
    # Effectuer la requête pour récupérer le contenu du fichier
    with urllib.request.urlopen(url) as response:
        # Lire le contenu du fichier
        data = response.read()

    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(data)
        temp_file.flush()

        # Obtenir le chemin du fichier temporaire
        chemin_fichier_temporaire = temp_file.name

    # Vous pouvez faire ce que vous voulez avec le fichier temporaire ici
    # Par exemple, vous pouvez extraire le contenu du fichier zip ou le manipuler d'une autre manière

    print("Téléchargement réussi !")

except Exception as e:
    print(f"Une erreur s'est produite lors du téléchargement : {e}")
