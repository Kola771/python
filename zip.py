import shutil
import zipfile
import os


def functionZip(folder_path, zip_path):
    # Vérifie que le dossier existe
    if not os.path.exists(folder_path):
        raise FileNotFoundError("Le dossier spécifié n'existe pas.")

    # Crée une instance de ZipFile pour écrire le fichier zip
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Parcourt tous les fichiers et dossiers du dossier source
        for root, _, files in os.walk(folder_path):
            for file in files:
                # Chemin complet du fichier source
                file_path = os.path.join(root, file)
                # Chemin relatif du fichier par rapport au dossier source
                relative_path = os.path.relpath(file_path, folder_path)
                # Ajoute le fichier au fichier zip avec le chemin relatif
                zipf.write(file_path, relative_path)

# Exemple d'utilisation
folder_to_zip = "test"
output_zip_file = "element/resultats.zip"

functionZip(folder_to_zip, output_zip_file)
print("Le contenu du dossier a été compressé avec succès.")


def functionMove(source_path, destination_path):
    # Utilise la fonction shutil.move pour déplacer le fichier
    shutil.move(source_path, destination_path)

# Exemple d'utilisation
file_to_move = "element/resultats.zip"
destination_path = "test"

functionMove(file_to_move, destination_path)
print("Le fichier a été déplacé avec succès.")
