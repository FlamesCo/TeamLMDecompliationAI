import tkinter as tk

class LunarMagicGUI:
    def __init__(self, root):         
        self.root = root
        self.root.title("Lunar Magic")
        self.root.geometry("600x400")

        self.create_menu_bar()
        self.create_buttons()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open ROM")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menu_bar)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="both", expand=True)

        open_rom_button = tk.Button(button_frame, text="Open ROM")
        open_rom_button.grid(row=0, column=0)

        edit_level_button = tk.Button(button_frame, text="Edit Level")
        edit_level_button.grid(row=0, column=1)

        save_button = tk.Button(button_frame, text="Save")
        save_button.grid(row=0, column=2)

if __name__ == "__main__":     
    root = tk.Tk()
    gui = LunarMagicGUI(root)
    root.mainloop()
