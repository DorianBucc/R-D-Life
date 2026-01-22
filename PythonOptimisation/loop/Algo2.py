import numpy as np

# Crée un tableau de 0 à 999_999_999
arr = np.arange(1_000_000_000, dtype=np.int32)

# Prend la dernière valeur
y = arr[-1]
print("Dernière valeur y =", y)

# 1,7 secondes