# Lab · Courses and notebooks

Travaux pratiques et jeux de données des cours de **Laurent Kouadio** (INP-HB et institutions partenaires).
Notebooks and datasets for the courses taught by **Laurent Kouadio** (INP-HB and partner institutions).

➡️ Portail étudiant / Student portal: **https://www.lkouadio.com/lab**

## Ouvrir un notebook / Open a notebook

| Option | Comment / How |
|---|---|
| **Google Colab** (recommandé) | Cliquez sur le badge *Open in Colab* en haut du notebook ou sur le portail. Rien à installer. |
| **Jupyter local** (hors ligne) | Téléchargez le dépôt (*Code → Download ZIP*), puis `conda env create -f environment.yml` et `jupyter lab`. |

La première cellule de chaque notebook récupère les données : depuis `../data` si vous avez le dépôt, sinon depuis GitHub.
The first cell of each notebook fetches its data: from `../data` if you have the repo, otherwise from GitHub.

## Cours / Courses

| Institution | Cours | Dossier |
|---|---|---|
| INP-HB | IC1 · Fondations du Machine Learning (20 h) | [`inphb/ic1`](inphb/ic1) |

## Pour l'enseignant / For the instructor

```bash
python tools/prepare_course.py <notebooks_source> <donnees_source> <institution>/<cours>
```
Copies a course's notebooks and data here, adds the Colab badge and the data-setup cell, and clears outputs. The originals are never changed.
Solutions and exams do **not** belong in this public repository.
