import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import pyperclip
from cryptography.fernet import Fernet
from datetime import datetime as dt
import sys
class FileEncryptor:
    def __init__(self, master):
        self.master = master
        master.title("File Encryptor")
        self.file_paths = []
        self.label = tk.Label(master, text="Enter File/Folder Path:")
        self.label.pack()
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()
        self.add_button = tk.Button(master, text="Add", command=self.add_file_or_folder)
        self.add_button.pack()
        self.choice_var = tk.StringVar(value="Encrypt")
        self.choice_label = tk.Label(master, text="Choose an action:")
        self.choice_label.pack()
        self.encrypt_radio = tk.Radiobutton(master, text="Encrypt", variable=self.choice_var, value="Encrypt")
        self.encrypt_radio.pack()
        self.decrypt_radio = tk.Radiobutton(master, text="Decrypt", variable=self.choice_var, value="Decrypt")
        self.decrypt_radio.pack()
        self.process_button = tk.Button(master, text="Process", command=self.process_files)
        self.process_button.pack()
        self.decryption_key_label = tk.Label(master, text="Decryption Key:")
        self.decryption_key_label.pack()
        self.decryption_key_var = tk.StringVar()
        self.decryption_key_entry = tk.Entry(master, textvariable=self.decryption_key_var, state="readonly")
        self.decryption_key_entry.pack()
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_decryption_key)
        self.copy_button.pack()
        self.decryption_key = None
    def add_file_or_folder(self):
        file_or_folder_path = self.input_entry.get().strip()
        if file_or_folder_path:
            self.file_paths.append(file_or_folder_path)
            self.update_label()
    def update_label(self):
        self.label.config(text=f"Entered Files/Folders: {', '.join(map(os.path.basename, self.file_paths))}")
    def process_files(self):
        if self.file_paths:
            if self.choice_var.get() == "Encrypt":
                self.encrypt_files(self.file_paths)
            elif self.choice_var.get() == "Decrypt":
                self.ask_for_decryption_key()
                self.decrypt_files(self.file_paths)
    def encrypt_files(self,paths):
      def encrypt(k):
        for file_path in paths:
            if os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    data = file.read()
                fernet = Fernet(k)
                encrypted_data = fernet.encrypt(data)
                with open(file_path, "wb") as encrypted_file:
                    encrypted_file.write(encrypted_data)
                print(f"File encrypted and saved to: {file_path}")
                with open("logfile.txt","a") as log:
                    text_format=f"[{dt.now()}]: {file_path}"
                    log.write(text_format + "\n")
            elif os.path.isdir(file_path):
                for files in os.listdir(file_path):
                    dir_path=os.path.join(file_path,files)
                    if os.path.isfile(dir_path):
                        with open(dir_path, "rb") as file:
                            data = file.read()
                        fernet = Fernet(k)
                        encrypted_data = fernet.encrypt(data)
                        with open(dir_path, "wb") as encrypted_file:
                            encrypted_file.write(encrypted_data)
                        print(f"File encrypted and saved to: {dir_path}")
                        with open("logfile.txt","a") as log:
                            text_format=f"[{dt.now()}]: {dir_path}"
                            log.write(text_format + "\n")  
      key = Fernet.generate_key()
      self.show_key(key)
      encrypt(key)
    def ask_for_decryption_key(self):
        decryption_key = tk.simpledialog.askstring("Decryption Key", "Enter the decryption key:")
        if decryption_key:
            self.decryption_key = decryption_key.encode()
    def decrypt_files(self,paths):
        if self.decryption_key:
            for file_path in paths:
                if os.path.isfile(file_path):
                    with open(file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()

                    fernet = Fernet(self.decryption_key)
                    decrypted_data = fernet.decrypt(encrypted_data)
                    with open(file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)
                elif os.path.isdir(file_path):
                  for dirs in os.listdir(file_path):
                    dir_path=os.path.join(file_path,dirs)
                    if os.path.isfile(dir_path):
                       with open(dir_path, "rb") as encrypted_file:
                           encrypted_data = encrypted_file.read()
   
                       fernet = Fernet(self.decryption_key)
                       decrypted_data = fernet.decrypt(encrypted_data)
                       with open(dir_path, "wb") as decrypted_file:
                           decrypted_file.write(decrypted_data)
    def show_key(self, key):
        key_str = key.decode()
        messagebox.showinfo("Encryption Key", f"Encryption Key: {key_str}")
        self.decryption_key_var.set(key_str)
    def copy_decryption_key(self):
        if self.decryption_key_var.get():
            pyperclip.copy(self.decryption_key_var.get())
            messagebox.showinfo("Copy to Clipboard", "Decryption Key copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptor(root)
    root.mainloop()
