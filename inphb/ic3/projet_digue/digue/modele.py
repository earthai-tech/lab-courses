"""Entraînement, calibration conforme et application du modèle de comportement normal."""
from dataclasses import dataclass, field

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .features import CAPTEURS, construire_variables


@dataclass
class SystemeSurveillance:
    modeles: dict = field(default_factory=dict)
    seuils: dict = field(default_factory=dict)          # seuil conforme 99 % sur |résidu|
    seuil_biais: dict = field(default_factory=dict)     # seuil de dérive sur le biais mensuel
    version: str = "1.0"

    def entrainer(self, df: pd.DataFrame, fin_apprentissage: int, fin_calibration: int, alpha: float = 0.01):
        X = construire_variables(df)
        ok = X.notna().all(axis=1)
        app = X.index[ok & (X.index < fin_apprentissage)]
        cal = X.index[ok & (X.index >= fin_apprentissage) & (X.index < fin_calibration)]
        for c in CAPTEURS:
            m = make_pipeline(StandardScaler(), Ridge(alpha=1.0)).fit(X.loc[app], df.loc[app, c])
            r = df.loc[cal, c] - m.predict(X.loc[cal])
            n = len(r)
            self.seuils[c] = float(np.quantile(np.abs(r), min(1.0, np.ceil((n + 1) * (1 - alpha)) / n)))
            biais = r.groupby(pd.to_datetime(df.loc[cal, "date"]).dt.to_period("M")).mean()
            self.seuil_biais[c] = float(max(0.15, 3 * biais.abs().max()))
            self.modeles[c] = m
        return self

    def residus(self, df: pd.DataFrame) -> pd.DataFrame:
        X = construire_variables(df)
        ok = X.notna().all(axis=1)
        out = pd.DataFrame({"date": df.loc[ok, "date"]})
        for c, m in self.modeles.items():
            out[f"{c}_attendu"] = m.predict(X.loc[ok])
            out[f"{c}_residu"] = df.loc[ok, c] - out[f"{c}_attendu"]
        return out

    def alertes(self, df: pd.DataFrame, persistance: int = 3) -> pd.DataFrame:
        """Alerte si |résidu| dépasse le seuil conforme pendant `persistance` jours consécutifs."""
        r = self.residus(df)
        for c in self.modeles:
            depasse = (r[f"{c}_residu"].abs() > self.seuils[c]).astype(int)
            r[f"{c}_alerte"] = depasse.rolling(persistance).sum().ge(persistance)
        return r

    def derive(self, df: pd.DataFrame) -> pd.DataFrame:
        """Biais mensuel du résidu : une dérive de capteur décale le résidu sans changer sa variance."""
        r = self.residus(df)
        mois = pd.to_datetime(r["date"]).dt.to_period("M")
        lignes = []
        for c in self.modeles:
            b = r.groupby(mois)[f"{c}_residu"].mean()
            for m, v in b.items():
                lignes.append({"capteur": c, "mois": str(m), "biais": float(v), "derive": abs(v) > self.seuil_biais[c]})
        return pd.DataFrame(lignes)

    def sauvegarder(self, chemin: str):
        joblib.dump(self, chemin)

    @staticmethod
    def charger(chemin: str) -> "SystemeSurveillance":
        return joblib.load(chemin)
