import tkinter as tk
from tkinter import filedialog
 
class LevelEditor:
    def __init__(self, master):
        # Create the main window
        self.master = master
        self.master.title("Level Editor")
        self.master.geometry("600x400")

        # Add a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Add a File menu
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Add a canvas for level editing
        self.level_canvas = tk.Canvas(self.master, bg="white")
        self.level_canvas.pack(fill=tk.BOTH, expand=True)

    def open_file(self):
        # Open a file dialog and load the selected file
        file_path = filedialog.askopenfilename()
        if file_path:
            self.load_level_data(file_path)

    def load_level_data(self, file_path):
        # Load level data from the file and render it on the canvas
        pass  # Implement this based on your level format and rendering logic


def main():
    root = tk.Tk()
    app = LevelEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
