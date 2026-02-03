import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class FolderFileExporterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder File Exporter")
        self.folders = []

        self.listbox = tk.Listbox(root, width=80)
        self.listbox.pack(padx=10, pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Add Folder", command=self.add_folder).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Run", command=self.export_json).pack(side=tk.LEFT, padx=5)

    def add_folder(self):
        folder = filedialog.askdirectory()
        if folder and folder not in self.folders:
            self.folders.append(folder)
            self.listbox.insert(tk.END, folder)

    def remove_selected(self):
        selected = self.listbox.curselection()
        for i in reversed(selected):
            self.folders.pop(i)
            self.listbox.delete(i)

    def export_json(self):
        all_files = {}
        for folder in self.folders:
            files = []
            for item in os.listdir(folder):
                if os.path.isfile(os.path.join(folder, item)):
                    files.append(item)
            all_files[os.path.basename(folder)] = files

        output_path = os.path.join(os.path.expanduser("~"), "Desktop", "file_list.json")
        with open(output_path, "w") as f:
            json.dump(all_files, f, indent=2)

        messagebox.showinfo("Done", f"File list exported to:\n{output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderFileExporterApp(root)
    root.mainloop()
