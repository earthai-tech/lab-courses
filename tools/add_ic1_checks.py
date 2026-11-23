# Adds the auto-checked exercises (Otter-Grader) to the IC1 S1 and S2 notebooks
# and writes their tests to inphb/ic1/tests/. Run once after tools/prepare_course.py;
# it expects the notebooks as prepare_course.py writes them.
import json, textwrap
from pathlib import Path
R = Path(__file__).resolve().parents[1] / 'inphb' / 'ic1'
REPO_RAW = 'https://raw.githubusercontent.com/earthai-tech/lab-courses/main/inphb/ic1/'

def md(s): return {"cell_type": "markdown", "metadata": {}, "source": textwrap.dedent(s).strip("\n")}
def code(s): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": textwrap.dedent(s).strip("\n")}

def setup_cell(data, session, questions):
    return code(f'''
    # Configuration : Colab ou Jupyter local. Exécutez cette cellule en premier.
    # Elle récupère les données et les tests de vérification : depuis le dépôt
    # (../data, ../tests) si vous l'avez téléchargé, sinon depuis GitHub.
    import os, shutil, urllib.request
    URL = '{REPO_RAW}'
    FICHIERS = {[("data/" + d, d) for d in data] + [(f"tests/{session}/{q}.py", f"tests/{q}.py") for q in questions]!r}
    os.makedirs('tests', exist_ok=True)
    for source, cible in FICHIERS:
        if os.path.exists(cible):
            continue
        local = os.path.join('..', source)
        if os.path.exists(local):
            shutil.copy(local, cible)                      # kit hors ligne / dépôt cloné
        else:
            urllib.request.urlretrieve(URL + source, cible)  # Colab : téléchargement
    print('Prêt :', ', '.join(c for _, c in FICHIERS))
    ''')

GRADER = code('''
    # Vérification automatique des réponses (Otter-Grader)
    try:
        import otter
    except ImportError:
        %pip install -q otter-grader
        import otter
    grader = otter.Notebook(tests_dir="tests")
    ''')

def test_file(name, cases, points=1):
    import pprint
    return "OK_FORMAT = True\n\ntest = " + pprint.pformat({
        "name": name, "points": points,
        "suites": [{"cases": [{"code": textwrap.dedent(c).strip("\n"), "hidden": False, "locked": False,
                               **({"failure_message": m} if m else {})} for c, m in cases],
                    "scored": True, "setup": "", "teardown": "", "type": "doctest"}]}, width=100, sort_dicts=False) + "\n"

S1_TESTS = {
 "q1": [(">>> bool(isinstance(meilleur_modele, str) and meilleur_modele in modeles)\nTrue", "meilleur_modele doit être une chaîne : 'lin', 'ridge' ou 'rf'."),
        (">>> _mae = {k: mean_absolute_error(y_te, m.predict(X_te)) for k, m in modeles.items()}\n>>> bool(meilleur_modele == min(_mae, key=_mae.get))\nTrue", "Ce n'est pas le modèle qui a la plus petite MAE sur le test.")],
 "q2": [(">>> bool(isinstance(r2_rf, (float, np.floating)))\nTrue", "r2_rf doit être un nombre (utilisez r2_score)."),
        (">>> bool(abs(r2_rf - r2_score(y_te, modeles['rf'].predict(X_te))) < 1e-3)\nTrue", "r2_rf ne correspond pas au R² de la forêt sur le jeu de test.")],
 "q3": [(">>> bool(abs(ecart_final - (tr.mean(1)[-1] - va.mean(1)[-1])) < 1e-3)\nTrue", "Calculez l'écart entraînement − validation à la plus grande taille d'échantillon (dernière colonne de la courbe).")],
 "q4": [(">>> bool(isinstance(mae_rf_zero, (float, np.floating)) and mae_rf_zero > 0)\nTrue", "mae_rf_zero doit être une MAE positive."),
        (">>> _m0 = make_pipeline(SimpleImputer(strategy='constant', fill_value=0), RandomForestRegressor(400, min_samples_leaf=2, random_state=0)).fit(X_tr, y_tr)\n>>> bool(abs(mae_rf_zero - mean_absolute_error(y_te, _m0.predict(X_te))) < 0.05)\nTrue", "Refaites la forêt avec SimpleImputer(strategy='constant', fill_value=0), mêmes paramètres, et calculez la MAE sur le test.")],
}
S2_TESTS = {
 "q1": [(">>> bool(abs(ecart_rf - (scores['rf'][0] - scores['rf'][1])) < 1e-3)\nTrue", "ecart_rf = exactitude k-fold aléatoire − exactitude GroupKFold, pour la forêt ('rf')."),
        (">>> bool(ecart_rf > 0)\nTrue", "L'écart devrait être positif : le k-fold aléatoire est optimiste.")],
 "q2": [(">>> from sklearn.metrics import recall_score\n>>> _cl = sorted(y.unique()); _r = recall_score(y, pred, labels=_cl, average=None)\n>>> bool(facies_plus_confondu == _cl[int(np.argmin(_r))])\nTrue", "Cherchez le faciès dont la valeur diagonale (rappel) est la plus faible dans la matrice normalisée.")],
 "q3": [(">>> bool(isinstance(acc_gr_norm, (float, np.floating)) and 0 < acc_gr_norm <= 1)\nTrue", "acc_gr_norm doit être une exactitude entre 0 et 1."),
        (">>> _X = X.copy(); _X['GR_api'] = fa.groupby('puits')['GR_api'].transform(lambda s: (s - s.mean()) / s.std())\n>>> _a = cross_val_score(modeles['rf'], _X, y, cv=GroupKFold(6), groups=puits).mean()\n>>> bool(abs(acc_gr_norm - _a) < 0.01)\nTrue", "Remplacez GR par sa version normalisée par puits, puis refaites la validation GroupKFold(6) avec la forêt.")],
}

def write_tests(session, tests):
    d = R / 'tests' / session; d.mkdir(parents=True, exist_ok=True)
    for q, cases in tests.items():
        (d / f'{q}.py').write_text(test_file(q, cases), encoding='utf-8')

def rebuild(nbfile, data, session, tests, edit_cells, exercises):
    p = R / 'notebooks' / nbfile
    nb = json.loads(p.read_text(encoding='utf-8'))
    cells = nb['cells']
    assert 'Configuration' in ''.join(cells[1]['source'])
    cells[1] = setup_cell(data, session, list(tests))
    edit_cells(cells)
    # drop the old free-text bonus (it becomes a checked exercise)
    if cells[-1]['cell_type'] == 'markdown' and ''.join(cells[-1]['source']).startswith('## Bonus'):
        cells.pop()
    cells.insert(2, GRADER)
    cells.extend(exercises)
    nb['cells'] = cells
    p.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding='utf-8')

write_tests('s1', S1_TESTS); write_tests('s2', S2_TESTS)

rebuild('IC1_S1_pipeline_beton.ipynb', ['beton_8_constituants.csv'], 's1', S1_TESTS, lambda c: None, [
 md('''
 ## Exercices vérifiés automatiquement
 Remplacez chaque `...` par votre réponse, exécutez la cellule : la vérification indique tout de suite si c'est correct.
 Ces tests servent à vous entraîner ; la note du TP est attribuée sur le notebook rendu.

 **Q1.** Quel modèle a la plus petite MAE sur le jeu de test ? Stockez son nom (`'lin'`, `'ridge'` ou `'rf'`) dans `meilleur_modele`.
 '''),
 code('''
 meilleur_modele = ...
 grader.check("q1")
 '''),
 md('**Q2.** Calculez le R² de la forêt (`modeles[\'rf\']`) sur le jeu de test et stockez-le dans `r2_rf`.'),
 code('''
 r2_rf = ...
 grader.check("q2")
 '''),
 md('''**Q3.** Avec la courbe d'apprentissage (`tr`, `va`), calculez l'écart entre le score d'entraînement et le score de validation **à la plus grande taille** d'échantillon. Stockez-le dans `ecart_final`.
 Un grand écart indique-t-il plutôt un biais ou une variance ?'''),
 code('''
 ecart_final = ...
 grader.check("q3")
 '''),
 md('''**Q4 (bonus).** Le superplastifiant manquant signifie peut-être « pas de superplastifiant ». Refaites la forêt en imputant par **0** (`SimpleImputer(strategy='constant', fill_value=0)`, mêmes paramètres de forêt), et stockez sa MAE sur le test dans `mae_rf_zero`.
 Quelle hypothèse vous paraît la plus réaliste ?'''),
 code('''
 mae_rf_zero = ...
 grader.check("q4")
 '''),
 md('Pour tout vérifier d\'un coup :'),
 code('grader.check_all()'),
])

def s2_edit(cells):
    i = next(k for k, c in enumerate(cells) if 'cross_val_score(m, X, y, cv=StratifiedKFold' in ''.join(c['source']))
    src = ''.join(cells[i]['source'])
    src = src.replace("for nom, m in modeles.items():", "scores = {}\nfor nom, m in modeles.items():")
    src = src.replace("    print(nom, round(a, 3), round(b, 3))", "    scores[nom] = (a, b)\n    print(nom, round(a, 3), round(b, 3))")
    assert 'scores[nom]' in src
    cells[i]['source'] = src

rebuild('IC1_S2_facies_par_puits.ipynb', ['facies_diagraphies.csv'], 's2', S2_TESTS, s2_edit, [
 md('''
 ## Exercices vérifiés automatiquement
 Remplacez chaque `...` par votre réponse, exécutez la cellule : la vérification indique tout de suite si c'est correct.

 **Q1.** Pour la forêt (`'rf'`), de combien l'exactitude en k-fold aléatoire dépasse-t-elle celle de la validation par puits ? Utilisez le dictionnaire `scores` (`scores[nom] = (aléatoire, par puits)`) et stockez l'écart dans `ecart_rf`.
 Pourquoi le k-fold aléatoire est-il trop optimiste ici ?
 '''),
 code('''
 ecart_rf = ...
 grader.check("q1")
 '''),
 md('**Q2.** D\'après la matrice de confusion (puits jamais vus), quel faciès est le moins bien reconnu (plus petit rappel) ? Stockez son nom exact dans `facies_plus_confondu`.'),
 code('''
 facies_plus_confondu = ...
 grader.check("q2")
 '''),
 md('''**Q3 (bonus).** Normalisez GR **par puits** (`fa.groupby('puits')['GR_api'].transform(lambda s: (s - s.mean()) / s.std())`), remplacez la colonne `GR_api` d'une copie de `X`, puis refaites la validation `GroupKFold(6)` avec `modeles['rf']`. Stockez l'exactitude moyenne dans `acc_gr_norm`.
 La normalisation aide-t-elle ? Pourquoi ?'''),
 code('''
 acc_gr_norm = ...
 grader.check("q3")
 '''),
 md('Pour tout vérifier d\'un coup :'),
 code('grader.check_all()'),
])
print('done')
