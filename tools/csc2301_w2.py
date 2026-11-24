# CSC 2301 week 2: control flow (conditions, for/while loops, break) on a well log.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import csv, random
from make_csc2301 import R, md, code, setup_cell, save_notebook, test_file, write_tests

NB = 'CSC2301_W2_control_flow_well_log.ipynb'
DATA = 'well_log_kw1.csv'
STEP = 0.5

def make_data():
    rnd = random.Random(2302)
    # (top_m, base_m, kind): blocky sand/shale sequence
    beds, depth = [], 1500.0
    while depth < 1650:
        kind = 'shale' if not beds or beds[-1][2] == 'sand' else 'sand'
        thick = rnd.choice([4, 6, 8, 10, 12]) if kind == 'shale' else rnd.choice([3, 4, 6, 8])
        beds.append((depth, min(depth + thick, 1650.0), kind)); depth += thick
    rows, d = [], 1500.0
    while d <= 1650.0 + 1e-9:
        kind = next(k for t, b, k in beds if t <= d < b or (d >= 1650 and b >= 1650))
        if kind == 'sand':
            gr = rnd.gauss(42, 9); phi = rnd.gauss(0.19, 0.04)
        else:
            gr = rnd.gauss(108, 12); phi = rnd.gauss(0.07, 0.025)
        rows.append({'depth_m': f'{d:.1f}', 'gr_api': f'{max(gr, 15):.1f}', 'phi': f'{min(max(phi, 0.01), 0.32):.3f}'})
        d = round(d + STEP, 1)
    (R / 'data').mkdir(parents=True, exist_ok=True)
    with open(R / 'data' / DATA, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    return rows

READ = (">>> import csv as _csv\n>>> _r = list(_csv.DictReader(open('well_log_kw1.csv', encoding='utf-8')))\n"
        ">>> _d = [float(x['depth_m']) for x in _r]; _g = [float(x['gr_api']) for x in _r]; _p = [float(x['phi']) for x in _r]\n")
VSH = ">>> _v = lambda g: min(1.0, max(0.0, (g - 30) / (120 - 30)))\n"
TESTS = {
 "q1": [(">>> bool(isinstance(n_sand, int))\nTrue", "n_sand must be a whole number (an int)."),
        (READ + ">>> bool(n_sand == sum(1 for g in _g if g < 60))\nTrue", "Count the samples whose GR is strictly below 60 API.")],
 "q2": [(">>> [round(vshale(g), 3) for g in (30, 75, 120)]\n[0.0, 0.5, 1.0]", "Use (gr - 30) / (120 - 30): 30 API gives 0, 120 API gives 1."),
        (">>> [vshale(g) for g in (10, 150)]\n[0.0, 1.0]", "Clip the result: below 0 return 0, above 1 return 1.")],
 "q3": [(">>> bool(isinstance(first_shale_depth, float))\nTrue", "first_shale_depth must be a depth in metres (a float)."),
        (READ + ">>> bool(first_shale_depth == next(d for d, g in zip(_d, _g) if d > 1540 and g >= 100))\nTrue",
         "Go down the log from the top, skip depths down to 1540 m, and stop (break) at the first GR of 100 API or more.")],
 "q4": [(">>> bool(isinstance(net_pay_m, float))\nTrue", "net_pay_m must be a thickness in metres (a float)."),
        (READ + VSH + ">>> bool(abs(net_pay_m - 0.5 * sum(1 for g, p in zip(_g, _p) if _v(g) < 0.4 and p >= 0.12)) < 1e-6)\nTrue",
         "A sample is pay if vshale(GR) < 0.4 AND porosity >= 0.12. Each sample stands for 0.5 m.")],
 "q5": [(">>> bool(isinstance(n_sand_beds, int))\nTrue", "n_sand_beds must be a whole number (an int)."),
        (READ + ">>> _n = 0; _prev = False\n>>> for g in _g:\n...     s = g < 60\n...     if s and not _prev:\n...         _n += 1\n...     _prev = s\n"
                ">>> bool(n_sand_beds == _n)\nTrue",
         "Count how many times the log enters sand (GR < 60) after a non-sand sample, plus 1 if the log starts in sand.")],
}

def notebook():
    cells = [
        md(f'''
        # CSC 2301 · Week 2 — Control flow on a well log

        [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/csc2301/notebooks/{NB})

        **IUGB · BSc Mining / Petroleum Engineering** · Instructor: Laurent Kouadio

        Last week every line of a program ran once, from top to bottom. This week the program **decides**
        (`if`) and **repeats** (`for`, `while`) on its own. The data are a gamma-ray and porosity log from
        an exploration well, `KW-1` (synthetic, but realistic), sampled every 0.5 m from 1500 to 1650 m.

        **What you will practise:** comparisons and `and` / `or` / `not` · `if` / `elif` / `else` ·
        `for` with `range`, `zip` and `enumerate` · `while` · `break` and `continue` · counters and accumulators.

        Run each cell with **Shift + Enter**, from top to bottom, starting with the two setup cells.
        '''),
        setup_cell('w2', [DATA], TESTS),
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
        ## 1. Reading the log

        A **well log** records properties of the rocks along the borehole. We use two:

        | column | meaning |
        |---|---|
        | `depth_m` | measured depth, in metres |
        | `gr_api` | **gamma ray**, in API units: low in clean sand, high in shale (clay is radioactive) |
        | `phi` | **porosity**, a fraction: 0.20 means 20 % of the rock is pore space |

        We read the file into three lists of the same length: `depth[i]`, `gr[i]` and `phi[i]` describe the same sample.
        '''),
        code(f'''
        import csv

        depth, gr, phi = [], [], []
        with open("{DATA}", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                depth.append(float(r["depth_m"]))
                gr.append(float(r["gr_api"]))
                phi.append(float(r["phi"]))

        print(len(depth), "samples from", depth[0], "m to", depth[-1], "m")
        print("First sample:", depth[0], gr[0], phi[0])
        '''),
        md('''
        ## 2. Comparisons and Boolean logic

        A comparison gives `True` or `False`. Combine them with `and`, `or`, `not`.
        '''),
        code('''
        g, p = 45.0, 0.21
        print(g < 60)                  # clean enough to be sand?
        print(p >= 0.12)               # porous enough?
        print(g < 60 and p >= 0.12)    # both
        print(g > 100 or p < 0.05)     # at least one
        print(not (g < 60))
        '''),
        md('''
        ## 3. Repeating with `for`

        `range(n)` gives 0, 1, …, n−1. `zip` walks through several lists side by side, and `enumerate`
        gives the position with each value.
        '''),
        code('''
        for i in range(3):
            print(i, depth[i], gr[i])

        print("---")
        for d, g in zip(depth[:3], gr[:3]):
            print(d, g)

        print("---")
        for i, g in enumerate(gr[:3]):
            print("sample", i, "GR =", g)
        '''),
        md('''
        A loop often **accumulates** a result: a counter that goes up, a running total, a maximum so far.
        '''),
        code('''
        total = 0.0
        highest = gr[0]
        for g in gr:
            total += g             # same as total = total + g
            if g > highest:
                highest = g
        print("Mean GR:", round(total / len(gr), 1), "API; highest:", highest)
        '''),
        md('''
        ## 4. `break` and `continue`

        `break` leaves the loop at once; `continue` skips to the next value.
        Example: the first sample deeper than 1600 m with a porosity above 25 %.
        '''),
        code('''
        found = None
        for d, p in zip(depth, phi):
            if d <= 1600:
                continue           # not deep enough yet: skip
            if p > 0.25:
                found = d
                break              # stop at the first match
        print("First very porous sample below 1600 m:", found)
        '''),
        md('''
        ## 5. Repeating with `while`

        A `while` loop repeats **as long as** a condition is true. Use it when you do not know in advance
        how many times to repeat. Example: a well produces 1200 barrels a day and declines by 15 % a year.
        After how many years does it drop below 300 barrels a day, the economic limit?
        '''),
        code('''
        rate = 1200.0
        years = 0
        while rate >= 300:
            rate = rate * (1 - 0.15)
            years += 1
        print("Below the economic limit after", years, "years; rate =", round(rate), "bbl/d")
        '''),
        md('''
        ---
        ## Exercises

        Write your answer, run the cell, then run the `grader.check` cell below it.

        ### Q1. Counting sand samples

        Geologists often call a sample **sand** when its gamma ray is below 60 API.
        Store in `n_sand` the number of sand samples in the log.
        '''),
        code('''
        n_sand = ...
        n_sand
        '''),
        code('grader.check("q1")'),
        md('''
        ### Q2. Shale volume

        The **shale volume index** turns GR into a fraction between 0 (clean sand) and 1 (pure shale):

        $$V_{sh} = \\frac{GR - 30}{120 - 30}$$

        Write a function `vshale(gr)` that returns this value, **clipped** to the range 0–1:
        below 0 return 0.0, above 1 return 1.0.
        '''),
        code('''
        def vshale(gr):
            ...

        [vshale(g) for g in (20, 30, 75, 120, 140)]
        '''),
        code('grader.check("q2")'),
        md('''
        ### Q3. First shale below 1540 m

        Going down the well, find the first depth **deeper than 1540 m** where GR reaches 100 API or more.
        Store it in `first_shale_depth`. Use a loop with `break` (and `continue` if you like).
        '''),
        code('''
        first_shale_depth = ...
        first_shale_depth
        '''),
        code('grader.check("q3")'),
        md('''
        ### Q4. Net pay

        A sample is **pay** (rock that can produce oil) when its shale volume is below 0.4 **and** its
        porosity is at least 0.12. Each sample represents 0.5 m of rock.
        Store in `net_pay_m` the total pay thickness in metres (a `float`). Use your `vshale`.
        '''),
        code('''
        net_pay_m = ...
        net_pay_m
        '''),
        code('grader.check("q4")'),
        md('''
        ### Q5. How many sand beds?

        Sand samples come in **beds**: runs of consecutive sand samples (GR < 60) separated by non-sand.
        Store in `n_sand_beds` the number of separate sand beds.

        *Hint:* keep a variable that remembers whether the previous sample was sand. A new bed starts when
        the current sample is sand and the previous one was not.
        '''),
        code('''
        n_sand_beds = 0
        ...
        n_sand_beds
        '''),
        code('grader.check("q5")'),
        md('''
        ### Going further (not checked)

        * Print the top and base depth of each sand bed.
        * With `while`: how many years until the well in section 5 drops below 300 bbl/d if the decline is 25 % a year?

        ---
        **Before you leave:** run all the checks with the cell below, then save your notebook
        (**File → Download → .ipynb** in Colab).
        '''),
        code('grader.check_all()'),
    ]
    save_notebook(NB, 'w2', cells)

def build():
    rows = make_data()
    write_tests('w2', TESTS)
    notebook()
    return f'{len(rows)} log samples; {NB} written'
