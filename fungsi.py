import os

def buat_direktori(nama_folder):
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)

def apakah_file_ada(path):
    return os.path.exists(path)

def buat_file_baru(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("")

def tulis_ke_file(path, isi):
    with open(path, "a", encoding="utf-8") as f:
        f.write(isi + "\n")
