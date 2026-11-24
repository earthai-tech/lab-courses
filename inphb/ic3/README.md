# INP-HB · IC3 — Conception de systèmes d'IA (20 h)

Du modèle au système : contrat de données, modèle de comportement normal, seuils conformes, alertes, dérive, API, tableau de bord et tests, appliqués à la surveillance d'une digue à résidus miniers.

| Dossier | Contenu |
|---|---|
| [`projet_digue/`](projet_digue) | Squelette de référence du projet de synthèse, à compléter et critiquer : `digue/` (variables, modèle, alertes), `entrainer.py`, `api.py` (FastAPI), `tableau_de_bord.py` (Streamlit), `tests/` (pytest). Voir son README. |
| [`data/digue_residus_capteurs.csv`](data/digue_residus_capteurs.csv) | Série de capteurs de la digue (piézomètres, bassin, pluie). Contient un suintement progressif et une recalibration de capteur que le système doit distinguer. |
| [`data/sites_candidats.csv`](data/sites_candidats.csv) | Sites candidats pour l'exercice de choix et de priorisation. |

```bash
cd projet_digue
pip install pandas numpy scikit-learn joblib fastapi uvicorn httpx streamlit pytest
python entrainer.py ../data/digue_residus_capteurs.csv
pytest -q
uvicorn api:app --reload          # http://127.0.0.1:8000/docs
streamlit run tableau_de_bord.py
```
Ce cours se travaille sur un ordinateur (pas sur Colab) : API et tableau de bord tournent en local.
