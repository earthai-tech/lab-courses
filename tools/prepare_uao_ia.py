# Copies the UAO "IA appliquée aux géosciences (I)" student notebook
# (Documents\Lab\UAO\M1\M1_TD_TP\M1_TD_TP_enonces.ipynb, never the _corrige)
# into uao/ia-geosciences-1/notebooks/, adds the Colab badge and lets the
# setup cell fetch the data from this repository on Colab. Outputs are cleared.
#   python tools/prepare_uao_ia.py <path to M1_TD_TP_enonces.ipynb>
import json, sys
from pathlib import Path

SRC = Path(sys.argv[1])
assert 'corrige' not in SRC.name.lower(), 'never publish the worked solutions'
DST = Path(__file__).resolve().parents[1] / 'uao' / 'ia-geosciences-1' / 'notebooks' / SRC.name
REPO = 'earthai-tech/lab-courses'
COLAB = f'https://colab.research.google.com/github/{REPO}/blob/main/uao/ia-geosciences-1/notebooks/{SRC.name}'
RAW = f'https://raw.githubusercontent.com/{REPO}/main/uao/ia-geosciences-1/data'

nb = json.loads(SRC.read_text(encoding='utf-8'))
for c in nb['cells']:
    if c['cell_type'] == 'code':
        c['outputs'], c['execution_count'] = [], None

old = """elif SUR_COLAB:                        # Colab sans Drive : téléversement direct
    DOSSIER = '/content'
    if not os.path.exists(f'{DOSSIER}/{NOM}'):
        from google.colab import files
        print('Choisissez le fichier', NOM, 'sur votre ordinateur...')
        files.upload()
else:                                  # Jupyter local, sans Internet
    DOSSIER = next((d for d in ['.', 'donnees', '../M1_TP_donnees'] if os.path.exists(f'{d}/{NOM}')), '.')"""
new = f"""elif SUR_COLAB:                        # Colab sans Drive : téléchargement depuis le dépôt du cours
    DOSSIER = '/content'
    if not os.path.exists(f'{{DOSSIER}}/{{NOM}}'):
        try:
            import urllib.request
            urllib.request.urlretrieve(f'{RAW}/{{NOM}}', f'{{DOSSIER}}/{{NOM}}')
        except Exception:                # pas d'accès au dépôt : téléversement direct
            from google.colab import files
            print('Choisissez le fichier', NOM, 'sur votre ordinateur...')
            files.upload()
else:                                  # Jupyter local, sans Internet
    DOSSIER = next((d for d in ['.', 'donnees', '../data', '../M1_TP_donnees'] if os.path.exists(f'{{d}}/{{NOM}}')), '.')"""
setup = next(c for c in nb['cells'] if c['cell_type'] == 'code')
src = ''.join(setup['source'])
assert old in src, 'setup cell changed: update this script'
setup['source'] = src.replace(old, new)

first = nb['cells'][0]
if 'colab-badge' not in ''.join(first['source']):
    badge = f'[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)]({COLAB})\n\n'
    first['source'] = badge + ''.join(first['source'])
for i, c in enumerate(nb['cells']):
    c.setdefault('id', f'cell-{i}')
DST.parent.mkdir(parents=True, exist_ok=True)
DST.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote', DST)
