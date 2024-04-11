import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox

def view_metadata():
    filepath = entry.get()
    try:
        # Run exiftool command to get metadata
        result = subprocess.run(['exiftool', filepath], capture_output=True, text=True, check=True)
        metadata = result.stdout
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, metadata)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error: {e.stderr}")

# Create GUI
root = tk.Tk()
root.title("Metadata Viewer")

# Entry for file path
label = tk.Label(root, text="Enter file path:")
label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

# Button to view metadata
button = tk.Button(root, text="View Metadata", command=view_metadata)
button.grid(row=0, column=2, padx=5, pady=5)

# Text area to display metadata
output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
