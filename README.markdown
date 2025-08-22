# Password Manager

A simple password manager application built with Python using the `tkinter` library. It allows users to generate random passwords, save them along with website and email details to a JSON file, and search for saved entries. The UI features a logo image and basic input fields for website, email, and password.

## Table of Contents
- [Features](#features)
- [Files](#files)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features

- **Password Generation**: Creates a random password with 8-10 letters, 2-4 symbols, and 2-4 numbers, shuffles it, and copies it to the clipboard.
- **Save Password**: Stores website, email, and password in a JSON file (`day29/data.json`), updating existing entries if the file exists.
- **Search Password**: Retrieves and displays saved email and password for a given website via a message box.
- **Default Email**: Pre-fills the email field with "shoaibrizwan9@gmail.com".
- **Simple UI**: Includes labels, entry fields, buttons for generating, adding, and searching, and a logo image.

## Files

- `main.py`: Main script for the password manager application.
- `day29/logo.png`: Logo image (red lock with "MyPass" text) displayed in the UI.
- `day29/data.json`: (Generated) JSON file storing saved passwords (e.g., {"website": {"email": "example@email.com", "password": "generatedpass"}}).

## Requirements

- Python 3.x
- `tkinter` module (included in standard Python library)
- `pyperclip` library for clipboard functionality (`pip install pyperclip`)
- A logo image file (`logo.png`) in the `day29` subdirectory

## How to Run

1. Ensure Python and `pyperclip` are installed:
   ```bash
   pip install pyperclip
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/remi23242/Password-Manager.git
   ```
3. Navigate to the project directory:
   ```bash
   cd Password-Manager
   ```
4. Ensure `logo.png` is in the `day29` subdirectory (use the provided logo image or a similar PNG file).
5. Run the application:
   ```bash
   python main.py
   ```

## Usage

- Enter a website name in the "Website" field.
- The "Email/Username" field is pre-filled; edit if needed.
- Click "Generate Password" to create and auto-fill a random password (also copied to clipboard).
- Click "Add" to save the entry to `day29/data.json`.
- Click "Search" to retrieve and display saved details for the entered website in a message box.
- If no data file exists, one is created on the first save. If a website isn't found during search, a message indicates so.

## Future Improvements

- Add validation for empty fields or duplicate websites.
- Implement encryption for stored passwords in the JSON file.
- Add a delete or edit function for saved entries.
- Include a list view to display all saved websites.
- Enhance UI with themes or better error handling.

## License

This project is open-source and available under the MIT License.