# Builds IUGB CSC 2301 (Principles of Computer Programming) week 1:
# the synthetic drill-hole dataset, the starter notebook and its Otter-Grader tests.
# Re-running it overwrites iugb/csc2301/{data,notebooks,tests}/ for week 1.
import csv, json, pprint, random, textwrap
from pathlib import Path

R = Path(__file__).resolve().parents[1] / 'iugb' / 'csc2301'
REPO_RAW = 'https://raw.githubusercontent.com/earthai-tech/lab-courses/main/iugb/csc2301/'
NB = 'CSC2301_W1_python_basics.ipynb'
DATA = 'drillholes_assays.csv'

# ---------------------------------------------------------------- data
def make_data():
    rnd = random.Random(2301)
    rows = []
    holes = {'DH-01': 0.4, 'DH-02': 1.1, 'DH-03': 2.3, 'DH-04': 0.7, 'DH-05': 1.6, 'DH-06': 0.25}
    for hole, mean_gpt in holes.items():
        depth = 0.0
        for _ in range(rnd.randint(14, 20)):
            length = rnd.choice([1.0, 1.5, 2.0, 2.0, 2.0])
            lith = rnd.choices(['saprolite', 'granite', 'quartz vein', 'schist'], [2, 4, 1, 3])[0]
            boost = 3.5 if lith == 'quartz vein' else 1.0
            gpt = rnd.lognormvariate(0, 0.9) * mean_gpt * boost
            rows.append({'hole_id': hole, 'from_m': f'{depth:.1f}', 'to_m': f'{depth + length:.1f}',
                         'au_ppb': round(gpt * 1000), 'lithology': lith})
            depth += length
    (R / 'data').mkdir(parents=True, exist_ok=True)
    with open(R / 'data' / DATA, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    return rows

# ---------------------------------------------------------------- tests
def test_file(name, cases):
    return "OK_FORMAT = True\n\ntest = " + pprint.pformat({
        "name": name, "points": 1,
        "suites": [{"cases": [{"code": textwrap.dedent(c).strip("\n"), "hidden": False, "locked": False,
                               "failure_message": m} for c, m in cases],
                    "scored": True, "setup": "", "teardown": "", "type": "doctest"}]}, width=100, sort_dicts=False) + "\n"

READ = ">>> import csv as _csv\n>>> _rows = list(_csv.DictReader(open('drillholes_assays.csv', encoding='utf-8')))\n"
TESTS = {
 "q1": [(">>> bool(isinstance(n_intervals, int))\nTrue", "n_intervals must be a whole number (an int)."),
        (READ + ">>> bool(n_intervals == len(_rows))\nTrue", "Count every assay interval in the file, not the header line.")],
 "q2": [(">>> bool(callable(ppb_to_gpt))\nTrue", "Define a function called ppb_to_gpt."),
        (">>> bool(abs(ppb_to_gpt(1000) - 1.0) < 1e-9 and abs(ppb_to_gpt(250) - 0.25) < 1e-9)\nTrue", "1 g/t is 1000 ppb: divide by 1000."),
        (">>> bool(ppb_to_gpt(0) == 0)\nTrue", "0 ppb should give 0 g/t.")],
 "q3": [(">>> bool(isinstance(mean_dh03, float))\nTrue", "mean_dh03 must be a number with decimals (a float)."),
        (READ + ">>> _s = [r for r in _rows if r['hole_id'] == 'DH-03']\n"
                ">>> _l = [float(r['to_m']) - float(r['from_m']) for r in _s]\n"
                ">>> _m = sum(int(r['au_ppb']) / 1000 * l for r, l in zip(_s, _l)) / sum(_l)\n"
                ">>> bool(abs(mean_dh03 - _m) < 1e-3)\nTrue",
         "Use only DH-03, convert ppb to g/t, and weight each grade by its interval length (to_m - from_m).")],
 "q4": [(">>> [classify(g) for g in (0.1, 0.49)]\n['waste', 'waste']", "Below 0.5 g/t the rock is 'waste'."),
        (">>> [classify(g) for g in (0.5, 1.2, 1.99)]\n['low grade', 'low grade', 'low grade']", "From 0.5 up to (not including) 2.0 g/t it is 'low grade'. Check the boundary at 0.5."),
        (">>> [classify(g) for g in (2.0, 7.5)]\n['high grade', 'high grade']", "2.0 g/t and above is 'high grade'. Check the boundary at 2.0.")],
 "q5": [(">>> bool(isinstance(hole_means, dict) and len(hole_means) == 6)\nTrue", "hole_means must be a dictionary with one entry per hole (6 holes)."),
        (READ + ">>> _w = {}; _t = {}\n"
                ">>> for r in _rows:\n...     l = float(r['to_m']) - float(r['from_m'])\n"
                "...     _w[r['hole_id']] = _w.get(r['hole_id'], 0) + int(r['au_ppb']) / 1000 * l\n"
                "...     _t[r['hole_id']] = _t.get(r['hole_id'], 0) + l\n"
                ">>> bool(all(abs(hole_means[h] - _w[h] / _t[h]) < 1e-3 for h in _w))\nTrue",
         "Each value should be the length-weighted mean grade in g/t of that hole (same method as Q3)."),
        (">>> bool(richest_hole == max(hole_means, key=hole_means.get))\nTrue", "richest_hole should be the hole_id with the highest mean in hole_means.")],
}

def write_tests():
    d = R / 'tests' / 'w1'; d.mkdir(parents=True, exist_ok=True)
    for q, cases in TESTS.items():
        (d / f'{q}.py').write_text(test_file(q, cases), encoding='utf-8')

# ---------------------------------------------------------------- notebook
def md(s): return {"cell_type": "markdown", "metadata": {}, "source": textwrap.dedent(s).strip("\n")}
def code(s): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": textwrap.dedent(s).strip("\n")}

def notebook():
    files = [("data/" + DATA, DATA)] + [(f"tests/w1/{q}.py", f"tests/{q}.py") for q in TESTS]
    cells = [
        md(f'''
        # CSC 2301 · Week 1 — Python basics with drill-hole data

        [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/csc2301/notebooks/{NB})

        **IUGB · Bachelor of Science in Mining / Petroleum Engineering** · Instructor: Laurent Kouadio

        In this first lab you will use Python the way an engineer does on a real project: read measurements
        from a file, convert units, summarise them and make a simple decision. The data are gold assays from
        six exploration drill holes (synthetic, but realistic).

        **What you will practise:** variables and types · arithmetic · lists and `for` loops · reading a CSV file ·
        writing functions · `if` / `elif` / `else` · dictionaries.

        **How to work:** run each cell with **Shift + Enter**, from top to bottom. Start with the two setup cells below.
        '''),
        code(f'''
        # Setup: run this cell first (Colab or local Jupyter).
        # It fetches the data and the answer checks: from the repository (../data, ../tests)
        # if you downloaded it, otherwise from GitHub.
        import os, shutil, urllib.request
        URL = '{REPO_RAW}'
        FILES = {files!r}
        os.makedirs('tests', exist_ok=True)
        for source, target in FILES:
            if os.path.exists(target):
                continue
            local = os.path.join('..', source)
            if os.path.exists(local):
                shutil.copy(local, target)                      # offline kit / cloned repo
            else:
                urllib.request.urlretrieve(URL + source, target)  # Colab: download
        print('Ready:', ', '.join(t for _, t in FILES))
        '''),
        code('''
        # Automatic answer checks (Otter-Grader)
        try:
            import otter
        except ImportError:
            %pip install -q otter-grader
            import otter
        grader = otter.Notebook(tests_dir="tests")
        '''),
        md('''
        ## 1. Variables and arithmetic

        A variable is a name for a value. Python has a few basic **types**: `int` (whole numbers),
        `float` (numbers with decimals), `str` (text) and `bool` (`True` / `False`).

        Example: the mass of rock in a block of ore is *volume × density*.
        '''),
        code('''
        length_m = 20      # int
        width_m = 10
        height_m = 5
        density = 2.7      # float, tonnes per cubic metre
        rock_type = "granite"   # str

        volume_m3 = length_m * width_m * height_m
        tonnes = volume_m3 * density
        print("Volume:", volume_m3, "m3")
        print("Mass:", tonnes, "t of", rock_type)
        print(type(volume_m3), type(tonnes), type(rock_type))
        '''),
        md('''
        Gold grades are often reported in **ppb** (parts per billion) by the laboratory, and in **g/t**
        (grams per tonne) by mining engineers. 1 g/t = 1000 ppb. If the block above grades 1.8 g/t,
        how much gold does it hold?
        '''),
        code('''
        grade_gpt = 1.8
        gold_g = tonnes * grade_gpt
        print(f"Gold in the block: {gold_g:.0f} g, or {gold_g / 31.1035:.1f} troy ounces")
        '''),
        md('''
        ## 2. Lists and loops

        A **list** holds several values in order. A `for` loop repeats an action for each value.
        '''),
        code('''
        grades = [0.2, 1.4, 3.1, 0.8, 0.05]   # g/t, five samples from one hole

        print("First sample:", grades[0])
        print("Last sample:", grades[-1])
        print("Number of samples:", len(grades))

        total = 0
        for g in grades:
            total = total + g
        print("Mean grade:", total / len(grades))
        print("Same with built-ins:", sum(grades) / len(grades), "max:", max(grades))
        '''),
        md('''
        ## 3. Reading the drill-hole file

        The file `drillholes_assays.csv` has one line per **assay interval**: a slice of core
        between two depths, sent to the lab. The columns are:

        | column | meaning |
        |---|---|
        | `hole_id` | drill hole name, e.g. `DH-01` |
        | `from_m`, `to_m` | top and bottom of the interval, in metres |
        | `au_ppb` | gold content, in ppb |
        | `lithology` | rock type |

        Python's `csv` module reads each line as a **dictionary** (`dict`): column name → value.
        Everything read from a file is text, so we convert the numbers ourselves.
        '''),
        code(f'''
        import csv

        rows = []
        with open("{DATA}", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append({{
                    "hole_id": r["hole_id"],
                    "from_m": float(r["from_m"]),
                    "to_m": float(r["to_m"]),
                    "au_ppb": int(r["au_ppb"]),
                    "lithology": r["lithology"],
                }})

        for r in rows[:3]:
            print(r)
        '''),
        md('''
        ## 4. Functions and decisions

        A **function** packages a calculation so you can reuse it. `if` / `elif` / `else` lets the program choose.
        '''),
        code('''
        def interval_length(row):
            """Length of an assay interval, in metres."""
            return row["to_m"] - row["from_m"]

        def describe_depth(depth_m):
            if depth_m < 10:
                return "near surface"
            elif depth_m < 30:
                return "shallow"
            else:
                return "deep"

        first = rows[0]
        print(first["hole_id"], "interval length:", interval_length(first), "m")
        print("Depth 25 m is", describe_depth(25))
        '''),
        md('''
        ---
        ## Exercises

        Write your answer in each cell, then run `grader.check("q…")` below it.
        A green message means the check passed; otherwise read the hint and try again.
        You can run a check as many times as you like.

        ### Q1. Counting

        How many assay intervals are in the file? Store the answer in `n_intervals` (an `int`). Use `rows`.
        '''),
        code('''
        n_intervals = ...
        n_intervals
        '''),
        code('grader.check("q1")'),
        md('''
        ### Q2. Unit conversion

        Write a function `ppb_to_gpt(ppb)` that converts a grade in ppb to g/t (1 g/t = 1000 ppb).
        '''),
        code('''
        def ppb_to_gpt(ppb):
            ...

        ppb_to_gpt(1850)
        '''),
        code('grader.check("q2")'),
        md('''
        ### Q3. Mean grade of one hole

        Intervals do not all have the same length, so a plain average is biased. Engineers use the
        **length-weighted mean**:

        $$\\bar g = \\frac{\\sum_i g_i \\, \\ell_i}{\\sum_i \\ell_i}$$

        where $g_i$ is the grade in g/t and $\\ell_i$ the length of interval *i*.
        Compute it for hole `DH-03` and store it in `mean_dh03` (a `float`).
        Use a loop, `interval_length` and your `ppb_to_gpt`.
        '''),
        code('''
        mean_dh03 = ...
        mean_dh03
        '''),
        code('grader.check("q3")'),
        md('''
        ### Q4. Ore or waste?

        Write a function `classify(grade_gpt)` that returns:

        * `"waste"` if the grade is below 0.5 g/t,
        * `"low grade"` from 0.5 up to (but not including) 2.0 g/t,
        * `"high grade"` from 2.0 g/t.
        '''),
        code('''
        def classify(grade_gpt):
            ...

        [classify(g) for g in (0.3, 1.0, 4.2)]
        '''),
        code('grader.check("q4")'),
        md('''
        ### Q5. Which hole is the richest?

        Build a dictionary `hole_means` that maps each `hole_id` to its length-weighted mean grade in g/t
        (as in Q3, but for every hole). Then store in `richest_hole` the `hole_id` with the highest mean.

        *Hint:* `max(d, key=d.get)` returns the key of a dictionary `d` with the largest value.
        '''),
        code('''
        hole_means = {}
        ...
        richest_hole = ...
        hole_means, richest_hole
        '''),
        code('grader.check("q5")'),
        md('''
        ### Going further (not checked)

        * How many intervals of each class (Q4) does each hole contain?
        * Is gold richer in one lithology? Compute the mean grade per `lithology`.

        ---
        **Before you leave:** run all the checks at once with the cell below, then save your notebook
        (**File → Download → .ipynb** in Colab).
        '''),
        code('grader.check_all()'),
    ]
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                        "language_info": {"name": "python"}, "colab": {"provenance": []}},
          "nbformat": 4, "nbformat_minor": 5}
    for i, c in enumerate(nb["cells"]):
        c["id"] = f"w1-{i:02d}"
    (R / 'notebooks').mkdir(parents=True, exist_ok=True)
    (R / 'notebooks' / NB).write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding='utf-8')

if __name__ == '__main__':
    rows = make_data()
    write_tests()
    notebook()
    print(len(rows), 'intervals;', NB, 'written')
