import tkinter as tk
import random
import time

# Paramètres du jeu
CELL_SIZE = 10
GRID_WIDTH = 60
GRID_HEIGHT = 40
UPDATE_DELAY = 100  # millisecondes

# Création de la fenêtre
window = tk.Tk()
window.title("Jeu de la Vie de Conway")
canvas = tk.Canvas(window, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()
# Label pour afficher le temps
info_label = tk.Label(window, text="", fg="white", bg="black", font=("Courier", 12))
info_label.pack()


# Grille : 0 = morte, 1 = vivante
grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    canvas.delete("all")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

def count_neighbors(x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                count += grid[ny][nx]
    return count

def update_grid():
    global grid
    start_time = time.time()  # Chrono

    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(x, y)
            if grid[y][x] == 1:
                new_grid[y][x] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[y][x] = 1 if neighbors == 3 else 0
    grid = new_grid
    draw_grid()

    elapsed_time = (time.time() - start_time) * 1000  # en millisecondes
    info_label.config(text=f"Temps de cycle : {elapsed_time:.2f} ms")

    window.after(UPDATE_DELAY, update_grid)

# Démarrer le jeu
draw_grid()
window.after(UPDATE_DELAY, update_grid)
window.mainloop()
