'''
TODO: 
figure how fractal can load under equations (AKA: parse the thing)


FINISH:
remove zoom/load ability
popup
load fractal
arrows for navigation, zoom function (NOW SINCE REMOVED)
user input for fractal math equation
'''
import numpy as np
import matplotlib.pyplot as plt

rows = 3000
cols = 3000
iterations = 150

equation_fractal = input("Please input the equation you wish for the fractal: ")

def mandelbrot(c, z):
    count = 0
    while count < iterations and abs(z) < 2:
        equation_fractal
        count += 1
    return count

print("Please wait for fractal render!")

def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            count = mandelbrot(c, z)
            m[i, j] = count
    return m

x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)

m = mandelbrot_set(x, y)

plt.imshow(m.T, cmap="magma")
plt.axis("off")
plt.savefig('mandelbrot_set.png', dpi=300, bbox_inches='tight')
plt.show()
print("fractal loaded!")
