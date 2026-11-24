"""Tests : pytest -q   (à lancer depuis le dossier IC3_projet_digue, après python entrainer.py)"""
import os
import sys

import pandas as pd
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from digue import SystemeSurveillance, verifier_contrat  # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, "..", "data", "digue_residus_capteurs.csv")


@pytest.fixture(scope="module")
def df():
    return pd.read_csv(DONNEES)


@pytest.fixture(scope="module")
def systeme(df):
    return SystemeSurveillance().entrainer(df, 730, 1095)


def test_contrat_ok(df):
    assert verifier_contrat(df) == []


def test_contrat_detecte_erreurs(df):
    mauvais = df.head(100).copy()
    mauvais.loc[5, "pluie_mm"] = -3
    mauvais = mauvais.drop(index=10)
    pb = verifier_contrat(mauvais)
    assert "pluie négative" in pb and "jours manquants dans la série" in pb


def test_pas_d_alerte_en_regime_normal(systeme, df):
    a = systeme.alertes(df.iloc[730:1095])
    assert a["P2_kPa_m_alerte"].sum() == 0


def test_alerte_suintement_P2(systeme, df):
    a = systeme.alertes(df)
    assert a.loc[a["date"] >= "2025-10-01", "P2_kPa_m_alerte"].any()


def test_derive_P3_detectee(systeme, df):
    d = systeme.derive(df)
    p3 = d[(d["capteur"] == "P3_kPa_m") & (d["mois"] >= "2025-04")]
    assert p3["derive"].all()


def test_api(df, tmp_path, monkeypatch):
    fastapi = pytest.importorskip("fastapi")
    from fastapi.testclient import TestClient
    SystemeSurveillance().entrainer(df, 730, 1095).sauvegarder(str(tmp_path / "systeme_digue.joblib"))
    monkeypatch.chdir(tmp_path)
    sys.modules.pop("api", None)
    import api
    client = TestClient(api.app)
    assert client.get("/sante").json()["statut"] == "ok"
    mesures = df.iloc[-120:].to_dict(orient="records")
    for m in mesures:
        m.pop("tassement_mm", None)
    rep = client.post("/evaluer", json={"mesures": mesures})
    assert rep.status_code == 200
    assert rep.json()["capteurs"]["P2_kPa_m"]["alerte"] is True
    rep = client.post("/evaluer", json={"mesures": mesures[:20]})
    assert rep.status_code == 422
