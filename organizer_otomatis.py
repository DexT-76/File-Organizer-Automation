import os
import shutil

def rapihin_folder_download():
    # 1. Mengunci target langsung ke folder download kamu di drive E
    folder_target = r"E:\Download"
    
    # 2. Menyesuaikan kategori dengan folder yang sudah kamu buat di screenshot
    kategori = {
        "APP": [".exe", ".msi"],
        "File": [".zip", ".rar", ".7z", ".tar", ".gz", ".pdf", ".docx", ".xlsx", ".txt"],
        "Foto": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Video": [".mp4", ".mkv", ".avi", ".mov"]
    }
    
    print("=== Asisten Rapi-Rapi E:\\Download Otomatis ===")
    
    if not os.path.exists(folder_target):
        print(f"Error: Folder '{folder_target}' tidak ditemukan.")
        return

    print(f"Memindai file di {folder_target}...\n")
    file_terpindah = 0

    # 3. Mulai scan semua isi di dalam E:\Download
    for item in os.listdir(folder_target):
        jalur_item = os.path.join(folder_target, item)
        
        # Pastikan yang dipindahkan adalah file (bukan folder APP, File, Foto, Video itu sendiri)
        if os.path.isfile(jalur_item):
            nama_file, ekstensi = os.path.splitext(item)
            ekstensi = ekstensi.lower()
            
            # Cari tahu file ini cocok masuk ke folder mana
            folder_tujuan_nama = None
            for nama_kategori, daftar_ekstensi in kategori.items():
                if ekstensi in daftar_ekstensi:
                    folder_tujuan_nama = nama_kategori
                    break
            
            # Jika ekstensinya cocok dengan salah satu kategori, langsung pindahkan
            if folder_tujuan_nama:
                folder_tujuan_lengkap = os.path.join(folder_target, folder_tujuan_nama)
                jalur_tujuan_file = os.path.join(folder_tujuan_lengkap, item)
                
                try:
                    shutil.move(jalur_item, jalur_tujuan_file)
                    print(f"[BERHASIL] {item} -> {folder_tujuan_nama}/")
                    file_terpindah += 1
                except Exception as e:
                    print(f"[GAGAL] Gagal memindahkan {item}. Error: {e}")
            else:
                # File dengan ekstensi lain yang belum didaftarkan akan dibiarkan di luar agar aman
                print(f"[LEWAT] Ekstensi {ekstensi} pada file '{item}' belum diatur.")

    print("\n=========================================")
    print("PROSES RAPI-RAPI SELESAI!")
    print(f"Total ada {file_terpindah} file baru yang berhasil disortir ke tempatnya.")

if __name__ == "__main__":
    rapihin_folder_download()