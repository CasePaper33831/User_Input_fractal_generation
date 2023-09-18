'''
TODO: 
decrease wait times per zoom/load instance
describe/define "event" with parentesis of movment def (lines 58-101)

FINISHED:
popup
load fractal
WSAD for navigation
Q and E zoom function
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

def move_left(event):
    global x_min, x_max
    x_min -= pan_step
    x_max -= pan_step
    recreate_mandelbrot()

def move_right(event):
    global x_min, x_max
    x_min += pan_step
    x_max += pan_step
    recreate_mandelbrot()

def move_up(event):
    global y_min, y_max
    y_min += pan_step
    y_max += pan_step
    recreate_mandelbrot()

def move_down(event):
    global y_min, y_max
    y_min -= pan_step
    y_max -= pan_step
    recreate_mandelbrot()

def zoom_in(event):
    global x_min, x_max, y_min, y_max
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_min += x_range / 2 * (1 - 1 / zoom_factor)
    x_max -= x_range / 2 * (1 - 1 / zoom_factor)
    y_min += y_range / 2 * (1 - 1 / zoom_factor)
    y_max -= y_range / 2 * (1 - 1 / zoom_factor)
    recreate_mandelbrot()

def zoom_out(event):
    global x_min, x_max, y_min, y_max
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_min -= x_range / 2 * (zoom_factor - 1)
    x_max += x_range / 2 * (zoom_factor - 1)
    y_min -= y_range / 2 * (zoom_factor - 1)
    y_max += y_range / 2 * (zoom_factor - 1)
    recreate_mandelbrot()

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

    # Bind keys for movement and zoom
    popup.bind("w", move_up)
    popup.bind("s", move_down)
    popup.bind("a", move_left)
    popup.bind("d", move_right)
    popup.bind("q", zoom_in)
    popup.bind("e", zoom_out)

root = tk.Tk()
root.after(0, create_popup)

def close_main_window():
    root.withdraw()

root.after(500, close_main_window)

root.mainloop()
