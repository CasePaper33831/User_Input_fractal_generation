'''
TODO: 
user Input for what equation to use on render instance

FINISH:
remove zoom/load ability
popup
load fractal
arrows for navigation
zoom function
'''
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
zoom_factor = 1.1
pan_step = 0.1


canvas_widget = None

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def create_mandelbrot(width, height, max_iter):
    global canvas_widget
    fig, ax = plt.subplots(figsize=(width / 80, height / 80), dpi=30)
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=np.int32)

    for i in range(width):
        for j in range(height):
            Z[i, j] = mandelbrot(C[i, j], max_iter)

    # Rotate the image 90 degrees to the right
    Z = np.rot90(Z, k=3)

    ax.imshow(Z.T, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
    ax.set_title("Mandelbrot Set")
    ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()


    popup.geometry(f"{width}x{height}")

def recreate_mandelbrot():
    global canvas_widget
    if canvas_widget:
        canvas_widget.destroy()
    create_mandelbrot(1500, 1500, 256)

def create_popup():
    global popup
    popup = tk.Toplevel(root)
    popup.title("Mandelbrot Set")
    create_mandelbrot(1500, 1500, 256)

root = tk.Tk()
root.after(0, create_popup)

def close_main_window():
    root.withdraw()

root.after(500, close_main_window)

root.mainloop()
