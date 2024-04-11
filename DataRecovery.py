import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import os
import subprocess
jpg_start1 = bytes.fromhex('ffd8ffe0')  
jpg_start2=bytes.fromhex('ffd8ffe1')
jpg_end = bytes.fromhex('ffd9')
length_jpg_end = len(jpg_end)
#jpg_pattern = re.compile( b'(' + re.escape(jpg_start1) + b'|' + re.escape(jpg_start2)+ b'(.+?)' + jpg_end, re.DOTALL)
jpg_pattern = re.compile(b'(' + re.escape(jpg_start1) + b'|' + re.escape(jpg_start2) + b')(.+?)' + jpg_end, re.DOTALL)

def extract_jpg_images(file_path, progress_bar):
    value = 0
    remaining_bytes = b''
    command = ["lsblk", "--output", "SIZE", "--noheadings", "--bytes", file_path]
    result = subprocess.check_output(command, universal_newlines=True)
    total_bytes = int(result.strip())
    bytes_read = 0
    
    try:
        with open(file_path, 'rb') as f:
            for binary_data in iter(lambda: f.read(104857600), b''): 
                bytes_read += len(binary_data)
                progress = int((bytes_read / total_bytes) * 100)
                progress_bar['value'] = progress
                progress_bar.update()
                
                binary = remaining_bytes + binary_data
                for match in jpg_pattern.finditer(binary):
                    start_index, end_index = match.span()
                    img_name = f'{value}.jpg'
                    with open(img_name, 'wb') as r:
                        r.write(binary[start_index:end_index])
                    value += 1
                    print(f'{img_name} is written successfully')
                remaining_bytes = binary[(binary.rfind(jpg_end) + length_jpg_end):]
        print("finished")
    except Exception as e:
        messagebox.showerror("Error ", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("JPEG Image Extractor")

# Widgets
label_path = tk.Label(root, text="Enter Path:")
entry_path = tk.Entry(root, width=50)
button_browse = tk.Button(root, text="Browse", command=lambda: entry_path.insert(tk.END, filedialog.askopenfilename()))
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
button_extract = tk.Button(root, text="Start Extraction", command=lambda: extract_jpg_images(entry_path.get(),progress_bar))


# Layout
label_path.grid(row=0, column=0, padx=10, pady=10)
entry_path.grid(row=0, column=1, padx=10, pady=10)
button_browse.grid(row=0, column=2, padx=10, pady=10)
button_extract.grid(row=1, column=0, columnspan=3, pady=10)
progress_bar.grid(row=2, column=0, columnspan=3, pady=10)

# Start the GUI event loop
root.mainloop()
