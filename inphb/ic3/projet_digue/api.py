"""API de surveillance : uvicorn api:app --reload   (puis http://127.0.0.1:8000/docs)"""
from typing import List

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from digue import HISTORIQUE_MIN, SystemeSurveillance, verifier_contrat

app = FastAPI(title="Surveillance de digue à résidus", version="1.0")
systeme = SystemeSurveillance.charger("systeme_digue.joblib")


class Mesure(BaseModel):
    date: str
    pluie_mm: float = Field(ge=0)
    niveau_bassin_m: float
    P1_kPa_m: float
    P2_kPa_m: float
    P3_kPa_m: float


class Requete(BaseModel):
    mesures: List[Mesure] = Field(description=f"Au moins {HISTORIQUE_MIN + 3} jours consécutifs, du plus ancien au plus récent")


@app.get("/sante")
def sante():
    return {"statut": "ok", "version_modele": systeme.version, "seuils_m": systeme.seuils}


@app.post("/evaluer")
def evaluer(req: Requete):
    df = pd.DataFrame([m.model_dump() for m in req.mesures])
    problemes = verifier_contrat(df)
    if problemes:
        raise HTTPException(status_code=422, detail=problemes)
    if len(df) < HISTORIQUE_MIN + 3:
        raise HTTPException(status_code=422, detail=f"historique insuffisant : {len(df)} jours")
    r = systeme.alertes(df).iloc[-1]
    return {
        "date": r["date"],
        "capteurs": {
            c: {"mesure": float(df[c].iloc[-1]), "attendu": round(float(r[f"{c}_attendu"]), 3),
                "residu": round(float(r[f"{c}_residu"]), 3), "seuil": round(systeme.seuils[c], 3),
                "alerte": bool(r[f"{c}_alerte"])}
            for c in systeme.modeles
        },
    }
