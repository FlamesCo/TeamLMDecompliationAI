import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Super Mario World Level Editor")
root.geometry("800x600")

def open_rom():
    rom_path = filedialog.askopenfilename()
    with open(rom_path, "rb") as f:
        rom_data = f.read()
    return rom_data

def edit_smw_code(rom_data):
    # Your code to edit the SMW ROM data goes here.
    pass

level_canvas = tk.Canvas(root, width=768, height=512, bg="white")
level_canvas.pack()

open_rom_button = tk.Button(root, text="Open ROM", command=open_rom)
open_rom_button.pack()

root.mainloop()