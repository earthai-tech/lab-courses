"""Construction des variables du modèle de comportement normal (aucune information future)."""
import numpy as np
import pandas as pd

CAPTEURS = ["P1_kPa_m", "P2_kPa_m", "P3_kPa_m"]
COLONNES_REQUISES = {"date": "object", "pluie_mm": "float", "niveau_bassin_m": "float",
                     "P1_kPa_m": "float", "P2_kPa_m": "float", "P3_kPa_m": "float"}
RETARDS_BASSIN = (0, 5, 12, 25, 40)
FENETRES_PLUIE = (1, 3, 7, 30, 90)
HISTORIQUE_MIN = max(max(RETARDS_BASSIN), max(FENETRES_PLUIE))  # jours nécessaires avant la 1re prédiction


def verifier_contrat(df: pd.DataFrame) -> list:
    """Contrat de données : renvoie la liste des problèmes (vide si tout va bien)."""
    pb = [f"colonne manquante : {c}" for c in COLONNES_REQUISES if c not in df.columns]
    if pb:
        return pb
    if df["pluie_mm"].lt(0).any():
        pb.append("pluie négative")
    if not df["niveau_bassin_m"].between(0, 60).all():
        pb.append("niveau du bassin hors plage [0, 60] m")
    dates = pd.to_datetime(df["date"], errors="coerce")
    if dates.isna().any():
        pb.append("date illisible")
    elif not dates.is_monotonic_increasing:
        pb.append("dates non triées")
    elif dates.diff().dropna().dt.days.ne(1).any():
        pb.append("jours manquants dans la série")
    return pb


def construire_variables(df: pd.DataFrame) -> pd.DataFrame:
    f = pd.DataFrame(index=df.index)
    for lag in RETARDS_BASSIN:
        f[f"bassin_l{lag}"] = df["niveau_bassin_m"].shift(lag)
    for w in FENETRES_PLUIE:
        f[f"pluie_{w}j"] = df["pluie_mm"].rolling(w).sum()
    return f
