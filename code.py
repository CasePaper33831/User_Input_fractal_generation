'''
TODO: 
parsing???

FINISH:
remove zoom/load ability
popup
load fractal
arrows for navigation, zoom function (NOW SINCE REMOVED)
user input for fractal math equation
figure how fractal can load under equations (interior one color theme, exterior different)
'''
import numpy as np
import matplotlib.pyplot as plt

rows = 3000
cols = 3000
iterations = 500

equation_fractal = input("Please input the equation you wish for the fractal: ")
dpi_amount = int(input("Please input the dots per square inch for the fractal rendering in numbers, no comas: "))
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

cmap_inside = plt.get_cmap("inferno")
cmap_outside = plt.get_cmap("viridis")

inside_mask = m < iterations

m_inside = np.ma.masked_array(m, mask=~inside_mask)
m_outside = np.ma.masked_array(m, mask=inside_mask)


plt.imshow(m_inside.T, cmap=cmap_inside)
plt.imshow(m_outside.T, cmap=cmap_outside)
plt.axis("off")
plt.savefig('mandelbrot_set.png', dpi = dpi_amount, bbox_inches='tight')
plt.show()
print("Fractal loaded!")
