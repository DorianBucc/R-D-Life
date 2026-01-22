import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import matplotlib.animation as animation

# --- Paramètres de la simulation ---
SIZE = 100          # taille de la grille
TIME_STEPS = 500    # nombre d'itérations
DT = 0.1            # pas de temps
RADIUS = 5          # rayon du noyau
BETA = 1.0          # intensité de la croissance

# --- Fonction d'initialisation aléatoire ---
def init_grid(size):
    return np.random.rand(size, size)

# --- Création du noyau gaussien circulaire ---
def make_kernel(radius):
    y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
    kernel = np.exp(-(x**2 + y**2) / (2*radius**2))
    return kernel / kernel.sum()

# --- Fonction de croissance ---
def growth(u):
    return 2 * u * (1 - u)  # exemple : sigmoïde simple

# --- Une itération de Lenia ---
def step(grid, kernel):
    conv = convolve2d(grid, kernel, mode='same', boundary='wrap')
    grid += DT * growth(conv) * BETA
    grid = np.clip(grid, 0, 1)  # garder entre 0 et 1
    return grid

# --- Initialisation ---
grid = init_grid(SIZE)
kernel = make_kernel(RADIUS)

# --- Animation ---
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='viridis', interpolation='nearest')

def update(frame):
    global grid
    grid = step(grid, kernel)
    im.set_array(grid)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=TIME_STEPS, interval=50, blit=True)
plt.show()
