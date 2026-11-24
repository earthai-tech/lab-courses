# Lab · Courses and notebooks

Travaux pratiques et jeux de données des cours de **Laurent Kouadio** (INP-HB et institutions partenaires).
Notebooks and datasets for the courses taught by **Laurent Kouadio** (INP-HB and partner institutions).

➡️ Portail étudiant / Student portal: **https://www.lkouadio.com/lab**

## Ouvrir un notebook / Open a notebook

| Option | Comment / How |
|---|---|
| **Google Colab** (recommandé) | Cliquez sur le badge *Open in Colab* en haut du notebook ou sur le portail. Rien à installer. |
| **Jupyter local** (hors ligne) | Téléchargez le dépôt (*Code → Download ZIP*), puis `conda env create -f environment.yml` et `jupyter lab`. |

La première cellule de chaque notebook récupère les données (et les tests de vérification) : depuis `../data` si vous avez le dépôt, sinon depuis GitHub.
The first cell of each notebook fetches its data: from `../data` if you have the repo, otherwise from GitHub.

## Cours / Courses

| Institution | Cours | Dossier |
|---|---|---|
| INP-HB | IC1 · Fondations du Machine Learning (20 h) | [`inphb/ic1`](inphb/ic1) |
| IUGB | CSC 2301 · Principles of Computer Programming (in English) | [`iugb/csc2301`](iugb/csc2301) |
| CURAT | Data Sciences, visualisation et Big Data (M2, 20 h) | [`curat/data-science`](curat/data-science) |

## Pour l'enseignant / For the instructor

```bash
python tools/prepare_course.py <notebooks_source> <donnees_source> <institution>/<cours>
```
Copies a course's notebooks and data here, adds the Colab badge and the data-setup cell, and clears outputs. The originals are never changed.
Re-running it overwrites the notebooks of that course, including exercises added afterwards.

### Exercices vérifiés automatiquement / Auto-checked exercises

IC1 S1 and S2 end with short exercises checked by [Otter-Grader](https://otter-grader.readthedocs.io): students run `grader.check("q1")` and see at once which answers pass. Tests live in `inphb/ic1/tests/<session>/` and recompute the expected answer from the student's own variables, so no answer is written in the test files. `tools/add_ic1_checks.py` generates both. IUGB CSC 2301 week 1 works the same way (`tools/make_csc2301.py`).
These checks are for practice; graded tests with hidden cases belong in a private repository.
Solutions and exams do **not** belong in this public repository.
