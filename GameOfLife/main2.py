import tkinter as tk
import numpy as np
import numba
import time
import random

# Paramètres
CELL_SIZE = 10
GRID_WIDTH = 100
GRID_HEIGHT = 60
UPDATE_DELAY = 200

# Tkinter : fenêtre
window = tk.Tk()
window.title("Jeu de la Vie optimisé")
info_label = tk.Label(window, text="", fg="white", bg="black", font=("Courier", 12))
info_label.pack()
canvas = tk.Canvas(window, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()


# Grille numpy
grid = np.random.choice([0, 1], size=(GRID_HEIGHT, GRID_WIDTH)).astype(np.uint8)

def draw_grid():
    canvas.delete("all")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y, x] == 1:
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

@numba.njit
def compute_next_state(grid):
    height, width = grid.shape
    new_grid = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        neighbors += grid[ny, nx]
            if grid[y, x] == 1:
                new_grid[y, x] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[y, x] = 1 if neighbors == 3 else 0
    return new_grid

def update_grid():
    global grid
    start_time = time.time()
    grid[:] = compute_next_state(grid)
    draw_grid()
    elapsed = (time.time() - start_time) * 1000
    info_label.config(text=f"Temps de cycle : {elapsed:.2f} ms")
    window.after(UPDATE_DELAY, update_grid)

# Démarrer
draw_grid()
window.after(UPDATE_DELAY, update_grid)
window.mainloop()
