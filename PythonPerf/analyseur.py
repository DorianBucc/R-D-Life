import subprocess
import time
import os
import sys
import tracemalloc

def analyser_script(script_path):
    if not os.path.isfile(script_path):
        print(f"Fichier non trouvé : {script_path}")
        return

    print(f"\nAnalyse de : {script_path}")
    
    # Taille du fichier
    taille = os.path.getsize(script_path)
    print(f"📦 Taille : {taille} octets")

    # 📚 Nombre de lignes
    with open(script_path, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        print(f"📄 Nombre de lignes : {len(lignes)}")

    # Tracemalloc pour voir la mémoire (facultatif)
    tracemalloc.start()

    # Temps d'exécution
    debut = time.time()
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except Exception as e:
        print(f"❌ Erreur à l'exécution : {e}")
        return
    fin = time.time()

    # Affichage du temps
    duree = fin - debut
    print(f"⏱️ Temps d'exécution : {duree:.3f} secondes")

    # Mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"📈 Mémoire utilisée : {current / 1024:.1f} Ko (pic : {peak / 1024:.1f} Ko)")

    # Résultat de l'exécution
    print("\n--- Sortie du script ---")
    print(result.stdout)
    if result.stderr:
        print("--- Erreurs ---")
        print(result.stderr)

# Utilisation
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python analyseur.py chemin/vers/script.py")
    else:
        analyser_script(sys.argv[1])
