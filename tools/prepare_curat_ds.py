# Copies the CURAT "Data Sciences, visualisation et Big Data" student notebooks
# (Documents\Lab\CURAT\04_Cours\S*/*.ipynb, not the _build teacher copies) into
# curat/data-science/notebooks/, adds the Colab badge and, where missing, a cell
# that installs the course packages on Colab only. Outputs are cleared.
#   python tools/prepare_curat_ds.py <path to 04_Cours>
import json, sys
from pathlib import Path

SRC = Path(sys.argv[1])
DST = Path(__file__).resolve().parents[1] / 'curat' / 'data-science' / 'notebooks'
COLAB = 'https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/curat/data-science/notebooks/'
PKGS = {  # packages Colab lacks, per session
    'S3': 'pystac-client rioxarray',
    'S4': 'pystac-client odc-stac',
    'S5': 'pystac-client odc-stac rioxarray',
    'S6': 'pystac-client',
    'S7': 'pystac-client odc-stac rioxarray folium mapclassify',
    'S8': 'pystac-client odc-stac rioxarray k-diagram',
    'S9': 'pystac-client odc-stac',
    'S10': 'pystac-client odc-stac',
}

def install_cell(pkgs):
    return {"cell_type": "code", "metadata": {}, "id": "colab-install", "execution_count": None, "outputs": [], "source": (
        "# Google Colab : installe les paquets du cours (environ 1 minute).\n"
        "# Dans l'environnement conda du cours (environment.yml), rien à faire.\n"
        "import sys\n"
        "if \"google.colab\" in sys.modules:\n"
        f"    %pip install -q {pkgs}")}

DST.mkdir(parents=True, exist_ok=True)
for nb_path in sorted(SRC.glob('S*/*.ipynb'), key=lambda p: int(p.parent.name[1:])):
    session = nb_path.parent.name
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    cells = nb['cells']
    for c in cells:
        if c['cell_type'] == 'code':
            c['outputs'], c['execution_count'] = [], None
    first = ''.join(cells[0]['source'])
    if 'colab-badge' not in first:
        title, _, rest = first.partition('\n')
        cells[0]['source'] = f"{title}\n\n[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)]({COLAB}{nb_path.name})\n{rest}"
    has_pip = any('%pip' in ''.join(c['source']) for c in cells if c['cell_type'] == 'code')
    if not has_pip and session in PKGS:
        cells.insert(1, install_cell(PKGS[session]))
    nb.setdefault('metadata', {})['colab'] = {"provenance": []}
    (DST / nb_path.name).write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(session, nb_path.name, len(cells), 'cells')
