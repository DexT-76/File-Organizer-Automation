# Multi-Drive Automated File Organizer

A smart, lightweight Python OS automation tool that automatically detects download directories across all active system drives and organizes loose files into categorized subfolders based on extension mapping.

---

## 🌟 Key Features

- **Multi-Drive & System Auto-Detection:** Automatically scans all active drives (`C:`, `D:`, `E:`, etc.) and system user paths for `Download` or `Downloads` directories.
- **Dynamic Subfolder Creation:** Automatically creates category subfolders (`APP`, `File`, `Foto`, `Video`, `Music`) inside target download directories if they do not exist.
- **Categorized File Sorting:** Routes loose files into designated folders based on their file extensions.
- **Zero External Dependencies:** Built purely using Python standard modules (`os`, `shutil`, `string`), requiring no extra `pip` installations.
- **Safe Execution & Error Handling:** Skips existing folders and unregistered file types to prevent data loss or accidental overwrites, providing live terminal progress logs.

---

## ⚙️ Extension Mapping

The script organizes files into five primary categories:

| Category Folder | Supported File Extensions |
| :--- | :--- |
| **APP** | `.exe`, `.msi`, `.and others` |
| **File** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.pdf`, `.docx`, `.xlsx`, `.txt`, `.and others` |
| **Foto** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.and others` |
| **Video** | `.mp4`, `.mkv`, `.avi`, `.mov`, `.and others` |
| **Music** | `.mp3`, `.wav`, `.flac`, `.aac`, `.m4a`, `.ogg`, `.and others` |

---

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DexT-76/File-Organizer-Automation.git


1. Run the Script:

```
Bash
python organizer_otomatis.py
```

2. How It Works:
The script will automatically identify every download folder across your hard drives, create missing category directories, and move matching files instantly.


📄 License
This project is open-source and available under the MIT License.
