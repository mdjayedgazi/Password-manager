# 🔐 Password Manager (Tkinter App)

A simple and secure Password Manager built using **Python**, **Tkinter**, and **JSON**. This desktop application allows users to generate strong passwords, store them safely with email/username, and retrieve them later when needed.

---

## ✨ Features

- 🔑 **Password Generator**  
  Generates secure and random passwords containing letters, numbers, and symbols.

- 💾 **Save Passwords**  
  Save login credentials for different websites in a local JSON file.

- 🔍 **Search Functionality**  
  Retrieve saved credentials using the website name.

- 📋 **Clipboard Support**  
  Automatically copies generated passwords to your clipboard (via `pyperclip`).

- ⚠️ **Error Handling**  
  - Handles missing or corrupted JSON files.
  - Prevents saving empty fields.
  - Graceful handling if clipboard copy fails.

---

## 📦 Requirements

- Python 3.x  
- `tkinter` (comes with Python standard library)  
- `pyperclip` (install using `pip install pyperclip`)

---

## 🚀 Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
📁 File Structure
    password-manager/
    │
    ├── main.py             # Main application script
    ├── Password Data.json  # Stores the credentials (auto-created)
    ├── logo.png            # Logo for the UI (optional)
    └── README.md           # Project documentation