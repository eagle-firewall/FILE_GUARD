import os
import subprocess
import secrets
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

def get_drive_size(drive_path):
    try:
        output = subprocess.check_output(["lsblk", "-bdn", "-o", "SIZE", drive_path])
        size_str = output.decode("utf-8").strip().split("\n")[0]
        size = int(size_str)
        return size
    except Exception as e:
        messagebox.showerror("Error", f"Error getting drive size: {str(e)}")
        return 0

def secure_delete_drive(drive_path, passes=1, chunk_size=1024*1024):
    total_size = get_drive_size(drive_path)
    bytes_written = 0

    try:
        with open(drive_path, 'rb+') as drive:
            for _ in range(passes):
                drive.seek(0)
                while True:
                    random_data = secrets.token_bytes(chunk_size)
                    chunk = drive.read(chunk_size)
                    if not chunk:
                        print("finished")
                        break
                    drive.seek(-len(chunk), os.SEEK_CUR)
                    drive.write(random_data[:len(chunk)])
                    bytes_written += len(chunk)
                    progress = min(int(bytes_written / total_size * 100), 100)
                    progress_var.set(progress)
                    root.update()
    except Exception as e:
        messagebox.showerror("Error", f"Error during secure delete: {str(e)}")

    progress_var.set(100)
    root.update()

def delete_drive():
    drive_path = entry.get()
    if os.path.exists(drive_path):
        secure_delete_drive(drive_path)
        messagebox.showinfo("Deletion Completed", "Drive securely deleted.")
    else:
        messagebox.showwarning("Drive Not Found", "Drive not found.")

root = tk.Tk()
root.title("Secure Drive Deletion")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter Drive Path:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(frame, text="Delete Securely", command=delete_drive)
delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

progress_var = tk.DoubleVar()
progress_bar = Progressbar(root, variable=progress_var, maximum=100, mode='determinate')
progress_bar.pack(fill='x', padx=10, pady=5)

root.mainloop()
