"""Entraîne et sauvegarde le système : python entrainer.py chemin/digue_residus_capteurs.csv"""
import sys

import pandas as pd

from digue import SystemeSurveillance, verifier_contrat

chemin = sys.argv[1] if len(sys.argv) > 1 else "../data/digue_residus_capteurs.csv"
df = pd.read_csv(chemin)
problemes = verifier_contrat(df)
if problemes:
    sys.exit("Contrat de données non respecté : " + "; ".join(problemes))

# 2 ans d'apprentissage, 1 an complet de calibration (toutes les saisons)
systeme = SystemeSurveillance().entrainer(df, fin_apprentissage=730, fin_calibration=1095)
systeme.sauvegarder("systeme_digue.joblib")
print("Seuils conformes 99 % (m) :", {k: round(v, 3) for k, v in systeme.seuils.items()})
print("Seuils de dérive (m)      :", {k: round(v, 3) for k, v in systeme.seuil_biais.items()})
