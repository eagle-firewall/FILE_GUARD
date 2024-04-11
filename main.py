import tkinter as tk
from tkinter import ttk
import threading
import subprocess

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home Page")
        
        # Create buttons for each module
        modules = [('EncryptDecrypt', 'python3 EncryptDecrypt.py'), 
                   ('DataRecovery', 'python3 DataRecovery.py'), 
                   ('Secure_Deletion-Drive', 'python3 Secure_Deletion_Drive.py'), 
                   ('Secure_Deletion-File', 'python3 Secure_Deletion_File.py'), 
                   ('Metadata_Viewer', 'python3 Metadata_Viewer.py'), 
                   ('Metadata_Removal', 'python3 Metadata_Removal.py')]
                   
        for module_name, module_file in modules:
            button = ttk.Button(self, text=module_name, 
                                command=lambda m=module_file: self.run_module(m))
            button.pack(pady=5)

    def run_module(self, module_file):
        threading.Thread(target=self.run_module_in_thread, args=(module_file,)).start()

    def run_module_in_thread(self, module_file):
        subprocess.run(module_file, shell=True)  

if __name__ == "__main__":
    app = HomePage()
    app.mainloop()
