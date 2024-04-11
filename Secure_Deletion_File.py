import os
import secrets
import tkinter as tk
from tkinter import filedialog, messagebox

def secure_delete(file_path, passes=2, chunk_size=1024*1024):
    try:
        random_data = secrets.token_bytes(chunk_size)

        with open(file_path, 'rb+') as file:
            for _ in range(passes):
                file.seek(0)
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    file.seek(-len(chunk), os.SEEK_CUR)
                    file.write(random_data[:len(chunk)])
    except Exception as e:
        messagebox.showerror("Error", f"Error during secure delete: {str(e)}")

def secure_delete2(file_path, passes=2):
    try:
        with open(file_path, 'ab') as file:
            for _ in range(passes):
                file.truncate(0)
                file.seek(0)
    except Exception as e:
        messagebox.showerror("Error", f"Error during secure delete: {str(e)}")

def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                # Overwrite file
                secure_delete(file_path=file_path)
                print(f'Layer 1 deletion completed for {file_path}')

                # Truncate file
                secure_delete2(file_path=file_path)
                print(f'Layer 2 deletion completed for {file_path}')

                # Remove the file
                os.remove(file_path)
                print(f'Layer 3 deletion completed for {file_path}')
            except Exception as e:
                messagebox.showerror("Error", f"Error during secure delete: {str(e)}")
        else:
            messagebox.showwarning("File Not Found", f"File not found: {file_path}")

    messagebox.showinfo("Deletion Completed", 'Your files have been deleted securely.')

def browse_files(entry):
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_paths)

def add_files(file_paths, entry):
    new_file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])
    file_paths.extend(new_file_paths)
    entry.delete(0, tk.END)
    entry.insert(0, file_paths)

def main():
    root = tk.Tk()
    root.title("Secure File Deletion")

    file_paths_entry = tk.Entry(root, width=50)
    file_paths_entry.grid(row=0, column=0, padx=10, pady=10)

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_files(file_paths_entry))
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    add_button = tk.Button(root, text="Add", command=lambda: add_files(file_paths_entry.get().split(), file_paths_entry))
    add_button.grid(row=0, column=2, padx=10, pady=10)

    delete_button = tk.Button(root, text="Delete Securely", command=lambda: delete_files(file_paths_entry.get().split()))
    delete_button.grid(row=1, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
