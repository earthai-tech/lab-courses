# UAO · IA appliquée aux géosciences (II)

Master 2 Géosciences · Université Alassane Ouattara (Bouaké) · 20 h · Enseignant : Laurent Kouadio

Page du cours (support de cours en PDF après saisie du code de classe) : **https://www.lkouadio.com/fr/lab/uao/m2**

La suite approfondie du Master 1 : démarche scientifique, ingénierie des données géologiques, validation spatiale et temporelle, apprentissage profond, et usage responsable de l'IA générative dans le mémoire. Les bases (Python, nettoyage, régression, classification, clustering) sont dans le cours de Master 1 : [`uao/ia-geosciences-1`](../ia-geosciences-1).

## Données

| Fichier | Contenu |
|---|---|
| [`forages_socle_M2.csv`](data/forages_socle_M2.csv) | 320 forages en socle (mêmes variables que le M1, plus `log_rho`) : régression du débit, validation par zones. |
| [`piezometrie_synthetique.csv`](data/piezometrie_synthetique.csv) | Série journalière 2014–2023 de pluie (mm) et de niveau piézométrique (m) : prévision et validation temporelle. |
| [`sections_failles_48x48.npz`](data/sections_failles_48x48.npz) | 1 200 sections de 48 × 48 pixels (`images`, float32) et leurs étiquettes (`labels`) : détection de failles par réseau de neurones convolutif. |

```python
import numpy as np, pandas as pd
forages = pd.read_csv("data/forages_socle_M2.csv")
piezo = pd.read_csv("data/piezometrie_synthetique.csv", parse_dates=["date"])
z = np.load("data/sections_failles_48x48.npz"); X, y = z["images"], z["labels"]
```

