import os
import shutil

# Ganti path di bawah ini sesuai lokasi folder percobaanmu
TARGET_FOLDER = r"D:\Demo_Portofolio"

# Kategori folder dan ekstensi file yang dikenali
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
}


def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder tidak ditemukan: {folder_path}")
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Lewati jika item tersebut sudah berupa folder
        if os.path.isdir(file_path):
            continue

        # Ambil ekstensi file dan ubah ke huruf kecil
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Tentukan folder tujuan berdasarkan ekstensi
        destination_folder = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                destination_folder = category
                break

        # Buat folder kategori secara otomatis jika belum ada
        category_path = os.path.join(folder_path, destination_folder)
        os.makedirs(category_path, exist_ok=True)

        # Pindahkan file ke folder tujuan
        shutil.move(file_path, os.path.join(category_path, filename))
        print(f"Moved: {filename} -> {destination_folder}/")
        moved_count += 1

    print(f"\nDone! Successfully organized {moved_count} files.")


if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)