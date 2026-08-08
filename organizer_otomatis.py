import os
import shutil
import string

def cari_semua_folder_download():
    daftar_target = []

#1. Deteksi folder Downloads utama bawaan Windows (C:\Users\<User>\Downloads)
user_download = os.path.join(os.path.expanduser("~"), "Downloads")
if os.path.exists(user_download):
    daftar_target.append(user_download)

#2. Deteksi semua drive/disk yang aktif di PC (A: sampai Z:)
drive_tersedia = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]

#3. Cari folder "Download" atau "Downloads" di setiap drive
variasi_nama_folder = ["Download", "Downloads"]
for drive in drive_tersedia:
    for nama_folder in variasi_nama_folder:
        jalur_download = os.path.join(drive, nama_folder)
        # Pastikan Folder tersebut ada atau belum terdaftar di daftar_target
        if os.path.exists(jalur_download) and jalur_download not in daftar_target:
            daftar_target.append(jalur_download)

return daftar_target

def Rapihin_semua_download():
    # Kategori ekstensi file termasuk Music
    kategori = {
        "APP": [".exe", ".msi", ".bat", ".app"],
        "File": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Video": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
        "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Foto": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    }

    print("=== Asisten Auto-Detect & Organize Multi-Drive ===")
    target_folder = cari_semua_folder_download()

    if not target_folder:
        print("[INFO] Tidak ditemukan folder Download/Downloads di disk manapun.")
        return

    print(f"Berhasil menemukan {len(target_folder)} folder target:")
    for folder in target_folder:
        print(f"- {folder}")
    print("=" * 50 + "\n")

    total_file_terpindah = 0

    # Proses setiap folder Download yang terdeteksi
    for folder in target_folder:
        print(f"▶ memindai: {folder_target}")
        file_terrpisah = 0

        for item in os.listdir(folder_target):
            jalur_item = os.path.join(folder_target, item)

            # Pastikan hanya memproses file (bukan folder APP, Video, Music, Foto, File itu sendiri)
            if os.path.isfile(jalur_item):
                _, ekstensi = os.path.splitext(item)
                ekstensi = ekstensi.lower()

                # Cari kategori yang cocok
                folder_kategori_nama = None
                for nama_kategori, daftar_ekstensi in kategori.items():
                    if ekstensi in daftar_ekstensi:
                        folder_tujuan_nama = nama_kategori
                        break

                # Pindahkan file jika cocok
                if folder_tujuan_nama:
                    folder_tujuan_lengkap = os.path.join(folder_target, folder_tujuan_nama)

                    # Buat subfolder kategori jika belum ada
                    if not os.path.exists(folder_tujuan_lengkap):
                        os.makedirs(folder_tujuan_lengkap)

                    jalur_tujuan_file = os.path.join(folder_tujuan_lengkap, item)

                    try:
                        shutil.move(jalur_item, jalur_tujuan_file)
                        print(f"[BERHASIL] {item} → {folder_tujuan_nama}")
                        file_terpisah += 1
                    except Exception as e:
                        print(f"[GAGAL] {item}, Error: {e}")
        print(f"  Selesai di {folder_target}, ({file_terpindah} file disortir)\n")
        total_semua_file_terpindah += file_terpindah

    print("=========================================")
    print(f"SEMUA PROSES SELESAI!")
    print(f"Total keseluruhan: {total_semua_terpindah} file berhasil disortir di seluruh disk.")

if __name__ == "__main__":
    Rapihin_semua_download()