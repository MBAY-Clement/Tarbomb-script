import os
import zipfile
import bz2
import gzip

def extract_archive(file_path, extract_dir):
    ext = os.path.splitext(file_path)[1]
    if ext == '.zip':
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
    elif ext == '.bz2':
        with bz2.BZ2File(file_path, 'rb') as bz2_file:
            with open(os.path.join(extract_dir, os.path.splitext(os.path.basename(file_path))[0]), 'wb') as f_out:
                f_out.write(bz2_file.read())
    elif ext == '.gz':
        with gzip.open(file_path, 'rb') as gz_file:
            with open(os.path.join(extract_dir, os.path.splitext(os.path.basename(file_path))[0]), 'wb') as f_out:
                f_out.write(gz_file.read())

def recursive_extract(file_path, target_dir, secrets_number):
    while file_path:
        extract_archive(file_path, target_dir)
        base_name, ext = os.path.splitext(os.path.basename(file_path))
        file_path = None
        if ext == '.zip':
            secrets_number -= 1
            base_name = f'secrets{secrets_number}.zip.bz2.gz'
        elif ext == '.bz2':
            base_name = f'secrets{secrets_number}.zip'
        elif ext == '.gz':
            base_name = f'secrets{secrets_number}.zip.bz2'

        file_path = os.path.join(target_dir, base_name)

def main():
    starting_file = 'secrets657.zip.bz2.gz'  # Le fichier racine 
    target_dir = os.getcwd()  # Répertoire courant (répertoire de travail actuel)
    secrets_number = 657  # Nombre de secrets à extraire ici 657 car secrets657 est le fichier racine

    while starting_file:
        recursive_extract(starting_file, target_dir, secrets_number)
        base_name, ext = os.path.splitext(os.path.basename(starting_file))
        starting_file = None
        if ext == '.zip':
            secrets_number -= 1 #on fait -1 a chaque fois donc on va de 657 a 0
            base_name = f'secrets{secrets_number}.zip.bz2.gz'
        starting_file = os.path.join(target_dir, base_name)

if __name__ == '__main__':
    main()
