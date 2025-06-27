import numpy as np

# Crée un tableau de 0 à 99_999_999
arr = np.arange(100_000_000, dtype=np.int32)

# Prend la dernière valeur
y = arr[-1]
print("Dernière valeur y =", y)

# 0,4 secondes