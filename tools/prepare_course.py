"""Copy a course's notebooks + data into lab-courses and make them Colab-ready.

Usage:
    python tools/prepare_course.py SRC_NOTEBOOKS SRC_DATA DEST  (DEST e.g. inphb/ic1)

For every notebook it:
  * adds an "Open in Colab" badge under the title,
  * inserts a setup cell that finds each CSV locally (../data) or downloads it
    from this repo on GitHub, so the notebook runs unchanged in Colab or Jupyter,
  * clears outputs and execution counts (small files, clean diffs).
Original files are never modified.
"""
import json, re, shutil, sys
from pathlib import Path

REPO = "earthai-tech/lab-courses"
BRANCH = "main"

def main(src_nb, src_data, dest):
    root = Path(__file__).resolve().parents[1]
    out = root / dest
    (out / "notebooks").mkdir(parents=True, exist_ok=True)
    (out / "data").mkdir(parents=True, exist_ok=True)
    data_files = sorted(p.name for p in Path(src_data).glob("*") if p.is_file())
    for name in data_files:
        shutil.copy2(Path(src_data) / name, out / "data" / name)
    for nb_path in sorted(Path(src_nb).glob("*.ipynb")):
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        code = "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")
        used = [f for f in data_files if re.search(re.escape(f), code)]
        rel = f"{dest}/notebooks/{nb_path.name}"
        badge = (f"[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
                 f"(https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{rel})")
        first = nb["cells"][0]
        if first["cell_type"] == "markdown" and "colab-badge" not in "".join(first["source"]):
            src = "".join(first["source"]).split("\n", 1)
            first["source"] = src[0] + "\n\n" + badge + "\n" + (src[1] if len(src) > 1 else "")
        setup = [
            "# Configuration : Colab ou Jupyter local. Exécutez cette cellule en premier.\n",
            "import os, shutil, urllib.request\n",
            f"DONNEES = {used!r}\n",
            f"URL = 'https://raw.githubusercontent.com/{REPO}/{BRANCH}/{dest}/data/'\n",
            "for f in DONNEES:\n",
            "    if os.path.exists(f):\n",
            "        continue\n",
            "    if os.path.exists(os.path.join('..', 'data', f)):\n",
            "        shutil.copy(os.path.join('..', 'data', f), f)   # kit hors ligne / dépôt cloné\n",
            "    else:\n",
            "        urllib.request.urlretrieve(URL + f, f)            # Colab : téléchargement\n",
            "    print('OK', f)\n",
        ]
        if used and not any("raw.githubusercontent.com" in "".join(c["source"]) for c in nb["cells"]):
            nb["cells"].insert(1, {"cell_type": "code", "metadata": {}, "execution_count": None,
                                   "outputs": [], "source": setup})
        for c in nb["cells"]:
            if c["cell_type"] == "code":
                c["outputs"], c["execution_count"] = [], None
        nb.setdefault("metadata", {})["colab"] = {"provenance": []}
        (out / "notebooks" / nb_path.name).write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(nb_path.name, "->", used)

if __name__ == "__main__":
    main(*sys.argv[1:4])
