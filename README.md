
```markdown
# File Guard

File Guard is a Python-based application designed to provide various file management and security functionalities, including encryption, decryption, data recovery, secure deletion, metadata viewing, and metadata removal.

## Features

- **Encrypt and Decrypt Files:** Encrypt and decrypt files using Fernet encryption.
- **Data Recovery:** Recover JPEG images from binary data.
- **Secure Deletion:** Securely delete drive contents or individual files.
- **Metadata Viewer:** View metadata of files using exiftool.
- **Metadata Remover:** Remove metadata from files using exiftool.

## Requirements

### Python Dependencies

The following Python packages are required to run File Guard:

- `tkinter`: GUI toolkit for Python.
- `pyperclip`: Provides clipboard operations.
- `cryptography`: Required for encryption and decryption functionalities.

You can install these dependencies using the following command:

```bash
pip install tkinter pyperclip cryptography 
```

### Linux Tools

File Guard relies on several Linux tools and commands for certain functionalities. Make sure you have the following tools installed on your Linux system:

- `exiftool`: Required for metadata viewing and removal functionalities.
- `lsblk`: Used for drive information retrieval in the secure deletion module.

You can install these tools on Debian-based systems (such as Ubuntu) using:

```bash
sudo apt-get update
sudo apt-get install -y exiftool util-linux
```

## Getting Started

1. Clone this repository to your local machine.
2. Install the required Python packages and Linux tools as mentioned above.
3. Run the main script (`main.py`) to launch the File Guard application.

## Usage

1. Launch the File Guard application using the main script (`main.py`).
2. Use the GUI interface to perform various file management and security operations.

## Contributing

Contributions to File Guard are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
