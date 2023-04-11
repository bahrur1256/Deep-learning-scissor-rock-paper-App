import tkinter as tk
from tkinter import filedialog
from PIL import  Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")
# membuat lable
label = tk.Label(root, text="Pilih gambar yang akan diprediksi")
label.pack()
# membuat canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()