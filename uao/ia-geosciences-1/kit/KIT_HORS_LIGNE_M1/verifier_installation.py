"""Vérifie que le poste peut faire les TD/TP M1 sans Internet.
Utilisation : python verifier_installation.py   (ou double-clic sur VERIFIER.bat)"""
import importlib
import os
import sys

print("Python", sys.version.split()[0], "-", sys.executable)
ok = True
for nom in ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "notebook"]:
    try:
        m = importlib.import_module(nom)
        print(f"  [OK] {nom:<11} {getattr(m, '__version__', '')}")
    except ImportError:
        print(f"  [MANQUANT] {nom}")
        ok = False

ici = os.path.dirname(os.path.abspath(__file__))
csv = os.path.join(ici, "forages_socle_synthetique.csv")
print("  [OK] données trouvées" if os.path.exists(csv) else "  [MANQUANT] forages_socle_synthetique.csv")
ok = ok and os.path.exists(csv)

if ok:
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    df = pd.read_csv(csv).dropna()
    RandomForestRegressor(20, random_state=0).fit(df[["sfi", "power"]], df["debit_m3h"])
    print("\nTout est prêt : double-cliquez sur LANCER_JUPYTER.bat")
else:
    print("\nInstallation incomplète : voir LISEZMOI.txt")
input("\nAppuyez sur Entrée pour fermer...")
