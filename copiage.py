import os
import shutil

# Chemin d'origine du dossier à dupliquer
chemin_dossier_source = '../Essai'

# Chemin de destination pour la copie du dossier
chemin_dossier_destination = '../Dupliques/Duplication'

# Copie intégrale du dossier source vers la destination
shutil.copytree(chemin_dossier_source, chemin_dossier_destination)