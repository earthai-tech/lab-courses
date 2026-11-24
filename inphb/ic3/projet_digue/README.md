# Projet IC3 — Système de surveillance d’une digue à résidus

Squelette de référence du projet de synthèse IC3 (à compléter et critiquer par les élèves).

```
digue/features.py     contrat de données + variables (retards du bassin, cumuls de pluie)
digue/modele.py       modèle de comportement normal (Ridge), seuils conformes, alertes, dérive
entrainer.py          entraîne et sauvegarde systeme_digue.joblib
api.py                API FastAPI : GET /sante, POST /evaluer
tableau_de_bord.py    tableau de bord Streamlit
tests/                tests pytest (contrat, alertes, dérive, API)
```

## Démarrage
```
pip install pandas numpy scikit-learn joblib fastapi uvicorn httpx streamlit pytest
python entrainer.py ../data/digue_residus_capteurs.csv
pytest -q
uvicorn api:app --reload          # http://127.0.0.1:8000/docs
streamlit run tableau_de_bord.py
```

Données synthétiques : elles contiennent un suintement progressif sur P2 (à partir du 24 juillet 2025)
et une recalibration du capteur P3 (+0,45 m, mars 2025). Le système doit les distinguer.
