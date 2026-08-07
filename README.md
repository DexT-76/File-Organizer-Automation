# Automated File Organizer (For disk E)

A lightweight Python OS automation script designed to clean up and structure chaotic directory folders by automatically categorizing and moving files based on their extension types and this only works if you have an E drive; I'll update it to work on any drive if this gets a good response.

---

## 🌟 Key Features

- **Categorized File Sorting:** Automatically scans a target directory (e.g., `E:\Download`) and maps loose files into designated subfolders (`APP`, `File`, `Foto`, `Video`) based on file extension matching.
- **Safe Directory Skipping:** Detects and skips existing subfolders and unregistered file extensions to prevent accidental file movement or data overwrites[cite: 2].
- **Standard Library Implementation:** Built purely using Python's built-in `os` and `shutil` modules, requiring zero external dependencies[cite: 2].
- **Live Terminal Logging:** Provides clear, real-time feedback in the terminal for every successfully moved file, skipped item, or execution error[cite: 2].

---

## ⚙️ How It Categorizes Files

The script groups extensions into specific default target directories[cite: 2]:

| Category Folder | Supported Extensions[cite: 2] |
| :--- | :--- |
| **APP** | `.exe`, `.msi`[cite: 2] |
| **File** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.pdf`, `.docx`, `.xlsx`, `.txt`[cite: 2] |
| **Foto** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`[cite: 2] |
| **Video** | `.mp4`, `.mkv`, `.avi`, `.mov`[cite: 2] |

---

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DexT-76/Automated-File-Organizer.git

1. Prepare Target Directory:
Ensure the category subfolders (APP, File, Foto, Video) exist inside your target path (or modify folder_target in organizer_otomatis.py to point to your desired directory)[cite: 2].

2. Run the Script:

```bash

python organizer_otomatis.py

```

📄 License
This project is open-source and available under the MIT License.
