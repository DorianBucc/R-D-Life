import taichi as ti

ti.init(arch=ti.cpu)  # tu peux aussi utiliser ti.gpu

# Crée une variable scalaire
y = ti.field(dtype=ti.i32, shape=())

@ti.kernel
def compteur():
    for i in range(100_000_000):
        y[None] = i

compteur()
print("Résultat :", y[None])

# 1,3 secondes