from numba import njit

@njit
def compteur():
    y = 0
    for i in range(100_000_000):
        y = i
    return y

# Appel de la fonction
resultat = compteur()
print("Résultat :", resultat)

# 1,3 secondes