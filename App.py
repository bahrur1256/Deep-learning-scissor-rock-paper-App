# import tkinter as tk
# from tkinter import filedialog
# from PIL import  Image, ImageTk
# import tensorflow as tf
# import numpy as np
# root = tk.Tk()
# root.title("Image Viewer")
# # membuat lable
# label = tk.Label(root, text="Pilih gambar yang akan diprediksi")
# label.pack()
# # membuat canvas
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
# # membuat fungsi untuk membuka gambar
# def open_image():
#     global file_path
#     file_path = filedialog.askopenfilename()
#     image = Image.open(file_path)
#     photo = ImageTk.PhotoImage(image)
#     canvas.create_image(0, 0, image=photo, anchor=tk.NW)
#     canvas.image= photo
# # membuat button
# button = tk.Button(root, text="buka gambar", command=open_image)
# button.pack()
# # result label 
# result_label = tk.Label(root, text="")
# result_label.pack()
# # membuat model
# model = tf.keras.models.load_model("model.h5")
# # fungsi prediksi gamabar 
# def predict_image():
#     image = Image.open(file_path)
#     image = image.resize((150,150))
#     image = np.array(image)
#     image = image/255
#     image = np.expand_dims(image, axis=0)
#     prediction = model.predict(image)
#     label = np.argmax(prediction)
#     if label == 0:
#         result_label.config(text="paper")
#     elif label == 1:
#         result_label.config(text="batu")
#     elif label == 2:
#         result_label.config(text="gunting")
#     else:
#         result_label.config(text="bentuk tidak diketahui")

# # membuat button prediksi
# predict_button = tk.Button(root, text="prediksi gambar", command=predict_image)
# predict_button.pack()


# root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np


root = tk.Tk()
root.title("Image Viewer")

# Membuat label
label = tk.Label(root, text="Pilih gambar yang akan diprediksi")
label.pack()

# Membuat canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Fungsi untuk membuka gambar
def open_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    canvas.image = photo

# Membuat tombol untuk membuka gambar
button = tk.Button(root, text="Buka Gambar", command=open_image)
button.pack()

# Membuat label untuk menampilkan hasil prediksi
result_label = tk.Label(root, text="")
result_label.pack()

# Memuat model
model = tf.keras.models.load_model("model.h5")

def predict_image():
    try:
        image = Image.open(file_path)
        image = image.resize((150,150))
        image = np.array(image)
        image = image/255
        image = np.expand_dims(image, axis=0)
        prediction = model.predict(image)
        label = np.argmax(prediction)
        if label == 0:
            result_label.config(text="paper")
        elif label == 1:
            result_label.config(text="batu")
        elif label == 2:
            result_label.config(text="gunting")
        else:
            result_label.config(text="bentuk tidak diketahui")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat memprediksi gambar")


# Membuat tombol untuk memprediksi gambar
predict_button = tk.Button(root, text="Prediksi", command=predict_image)
predict_button.pack()

root.mainloop()
