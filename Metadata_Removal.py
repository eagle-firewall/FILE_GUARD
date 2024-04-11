import subprocess
import tkinter as tk
from tkinter import messagebox

def remove_metadata():
    filepath = entry.get()
    try:
        # Run exiftool command to remove metadata
        subprocess.run(['exiftool', '-all=', filepath], check=True)
        messagebox.showinfo("Success", "Metadata removed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error: {e.stderr}")

# Create GUI
root = tk.Tk()
root.title("Metadata Remover")

# Entry for file path
label = tk.Label(root, text="Enter file path:")
label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

# Button to remove metadata
button = tk.Button(root, text="Remove Metadata", command=remove_metadata)
button.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
