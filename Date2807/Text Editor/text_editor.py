import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

recent_files = []

def autosave(func):
    def wrapper(self, *args, **kwargs):
        if self.file_path:
            try:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    f.write(self.text.get("1.0", tk.END))
                print("Auto-saved before exit.")
            except Exception as e:
                print("Autosave failed:", e)
        return func(self, *args, **kwargs)
    return wrapper

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Text Editor")
        self.text = tk.Text(self.root, undo=True)
        self.text.pack(expand=True, fill='both')
        self.file_path = None

        self.create_menu()
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Search", command=self.search_text)
        edit_menu.add_command(label="Replace", command=self.replace_text)

        recent_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Recent Files", menu=recent_menu)
        self.recent_menu = recent_menu
        self.update_recent_files()

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.file_path = None
        self.root.title("Untitled - Text Editor")

    def open_file(self):
        try:
            path = filedialog.askopenfilename()
            if path:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)
                self.file_path = path
                self.root.title(os.path.basename(path) + " - Text Editor")
                self.add_to_recent(path)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    f.write(self.text.get("1.0", tk.END))
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        try:
            path = filedialog.asksaveasfilename(defaultextension=".txt")
            if path:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(self.text.get("1.0", tk.END))
                self.file_path = path
                self.root.title(os.path.basename(path) + " - Text Editor")
                self.add_to_recent(path)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot save file: {e}")

    def search_text(self):
        word = simpledialog.askstring("Search", "Enter word to search:")
        if word:
            start = "1.0"
            while True:
                start = self.text.search(word, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(word)}c"
                self.text.tag_add('found', start, end)
                self.text.tag_config('found', background='yellow')
                start = end

    def replace_text(self):
        word = simpledialog.askstring("Replace", "Enter word to replace:")
        replacement = simpledialog.askstring("Replace", f"Replace '{word}' with:")
        if word and replacement is not None:
            content = self.text.get("1.0", tk.END)
            new_content = content.replace(word, replacement)
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", new_content)

    def add_to_recent(self, path):
        if path not in recent_files:
            recent_files.insert(0, path)
            if len(recent_files) > 5:
                recent_files.pop()
            self.update_recent_files()

    def update_recent_files(self):
        self.recent_menu.delete(0, tk.END)
        for path in recent_files:
            self.recent_menu.add_command(label=path, command=lambda p=path: self.open_recent(p))

    def open_recent(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)
            self.file_path = path
            self.root.title(os.path.basename(path) + " - Text Editor")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

    @autosave
    def on_exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
