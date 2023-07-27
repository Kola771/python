
import shutil, os

# Chemin d'origine du dossier à copier
chemin_dossier_source = '../Essai'

# Chemin de destination pour la copie du dossier
chemin_dossier_destination = '../Dupliques'

# Supprimer le dossier de destination s'il existe déjà
shutil.rmtree(chemin_dossier_destination, ignore_errors=True)

# Copie du dossier source vers la destination
shutil.copytree(chemin_dossier_source, chemin_dossier_destination)
