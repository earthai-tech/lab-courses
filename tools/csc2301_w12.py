# CSC 2301 week 12: algorithms, linear and binary search, sorting, interpolation in a temperature survey.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W12_algorithms_search_interp.ipynb'
DATA = 'temperature_survey_gt1.csv'
FILES = [DATA, 'well_log_kw2.csv']   # kw2 from week 8

def make_data():
    rnd = random.Random(2312)
    rows, d = [], 0.0
    while d <= 3000:
        t = 27.0 + 0.031 * min(d, 1800) + 0.021 * max(0.0, d - 1800) + rnd.gauss(0, 0.4)
        rows.append({'depth_m': f'{d:.0f}', 'temp_c': f'{t:.1f}'})
        d += rnd.choice([100, 150, 200, 250])
    if rows[-1]['depth_m'] != '3000':
        t = 27.0 + 0.031 * 1800 + 0.021 * 1200
        rows.append({'depth_m': '3000', 'temp_c': f'{t:.1f}'})
    write_csv(DATA, rows)
    return rows

LOG = (">>> import numpy as _np\n>>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', skiprows=1)\n")
TAB = (">>> import numpy as _np\n>>> _t = _np.loadtxt('temperature_survey_gt1.csv', delimiter=',', skiprows=1)\n")
TESTS = {
 "q1": [(">>> [find_first([45, 60, 120, 98, 130], 100), find_first([45, 60], 100), find_first([], 5)]\n[2, -1, -1]",
         "Return the position of the FIRST value greater than the threshold, or -1 when there is none."),
        (LOG + ">>> bool(first_shale == int(_np.argmax(_a[:, 1] > 100)))\nTrue",
         "first_shale = find_first(gr, 100) with gr the GR column of well_log_kw2.csv, as a list.")],
 "q2": [(">>> import bisect as _bi, random as _r\n>>> _d = [2100 + 0.5 * k for k in range(601)]\n"
         ">>> _q = [2099.0, 2100.0, 2400.0, 2401.0] + [_r.uniform(2090, 2410) for _ in range(300)]\n"
         ">>> bool(all(depth_index(_d, x) == _bi.bisect_left(_d, x) for x in _q))\nTrue",
         "depth_index(depths, d): index of the first depth >= d (0 if d is above the first, len(depths) if below the last). "
         "Compare with bisect.bisect_left."),
        (">>> import inspect as _in\n>>> bool('while' in _in.getsource(depth_index) and 'bisect' not in _in.getsource(depth_index))\nTrue",
         "Write the binary search yourself with lo, hi and a while loop; do not call bisect inside the function.")],
 "q3": [(">>> _v = [2.31, 2.05, 2.62, 2.05, 1.98]\n>>> (selection_sort(_v), _v)\n([1.98, 2.05, 2.05, 2.31, 2.62], [2.31, 2.05, 2.62, 2.05, 1.98])",
         "Return a NEW sorted list (smallest first) and leave the input list unchanged: work on a copy, values[:]."),
        (">>> [selection_sort([]), selection_sort([7])]\n[[], [7]]", "An empty list and a one-element list are already sorted."),
        (">>> import inspect as _in\n>>> _s = _in.getsource(selection_sort)\n>>> bool('sorted(' not in _s and '.sort(' not in _s and 'min(' not in _s)\nTrue",
         "Write the algorithm yourself: no sorted(), .sort() or min() inside selection_sort.")],
 "q4": [(">>> [round(interp(5, 0, 10, 10, 30), 6), round(interp(0, 0, 10, 10, 30), 6), round(interp(2.5, 2, 1, 4, 0), 6)]\n[20.0, 10.0, 0.75]",
         "y = y0 + (x - x0) × (y1 - y0) / (x1 - x0).")],
 "q5": [(TAB + ">>> _q = [0.0, 1234.0, 1800.0, 2250.0, 2999.0, 3000.0] + list(_t[:, 0])\n"
               ">>> bool(all(abs(temperature_at(x, list(_t[:, 0]), list(_t[:, 1])) - _np.interp(x, _t[:, 0], _t[:, 1])) < 1e-9 for x in _q))\nTrue",
         "Find the interval with depth_index, then interp between its two ends. A depth equal to a table depth gives that temperature."),
        (TAB + ">>> bool(abs(t_2250 - _np.interp(2250, _t[:, 0], _t[:, 1])) < 1e-9)\nTrue", "t_2250 = temperature_at(2250, depths, temps)."),
        (">>> try:\n...     temperature_at(3500.0, [0.0, 1000.0], [27.0, 58.0])\n... except ValueError:\n...     print('ValueError')\nValueError",
         "Outside the surveyed depths, do not guess: raise ValueError.")],
}

def notebook():
    cells = [
        header(12, 'Algorithms: searching, sorting, interpolating', NB, f'''
        An **algorithm** is a precise recipe that a computer can follow. Python already has `sorted`, `bisect`
        and `np.interp`, but an engineer must know **how** they work and **how fast** they are, to choose well
        and to trust the result. This week you write the classic ones yourself and compare them with the library.
        The data are the week 8 log of well KW-2 and a temperature survey of geothermal well GT-1 (`{DATA}`,
        synthetic), measured at irregular depths.

        **What you will practise:** linear search · binary search · counting steps (complexity) ·
        selection sort · linear interpolation · comparing your code with the library.
        '''),
        setup_cell('w12', FILES, TESTS),
        otter_cell(),
        md('''
        ## 1. How many steps?

        To find a value in a list, a **linear search** looks at each element in turn: up to *n* steps.
        If the list is **sorted** (depths always are), a **binary search** looks at the middle, throws away the
        half that cannot contain the answer, and repeats: about log₂(*n*) steps. For a million samples:
        a million steps against twenty.
        '''),
        code('''
        import math

        for n in [10, 1_000, 1_000_000, 1_000_000_000]:
            print(f"n = {n:>13,}   linear: up to {n:>13,} steps   binary: about {math.ceil(math.log2(n)):>2} steps")
        '''),
        md('''
        ## 2. Binary search by hand

        Keep a window `[lo, hi)` that surely contains the answer, and halve it until it is empty.
        '''),
        code('''
        depths = [100, 250, 400, 550, 700, 850, 1000]
        target = 620
        lo, hi = 0, len(depths)
        while lo < hi:
            mid = (lo + hi) // 2
            print(f"lo={lo} hi={hi} mid={mid} depths[mid]={depths[mid]}")
            if depths[mid] < target:
                lo = mid + 1          # the answer is to the right of mid
            else:
                hi = mid              # mid may be the answer: keep it
        print("first depth >=", target, "is at index", lo, "->", depths[lo])
        '''),
        md('''
        ## 3. The data
        '''),
        code(f'''
        import csv
        import numpy as np

        log = np.loadtxt("well_log_kw2.csv", delimiter=",", skiprows=1)
        log_depth = list(log[:, 0])
        gr = list(log[:, 1])

        with open("{DATA}", encoding="utf-8") as f:
            survey = list(csv.DictReader(f))
        depths = [float(r["depth_m"]) for r in survey]
        temps = [float(r["temp_c"]) for r in survey]
        print(len(gr), "log samples;", len(depths), "temperature stations")
        print(list(zip(depths, temps))[:5])
        '''),
        md('''
        ---
        ## Exercises

        Write the algorithms with loops; the checks compare your answers with the library versions.
        '''),
        *question('q1', '''
        ### Q1. Linear search

        Write `find_first(values, threshold)` that returns the **position** of the first value greater than
        `threshold`, or `-1` if there is none. Then store in `first_shale` the index of the first GR sample above
        100 API in well KW-2. What depth is it?
        ''', '''
        def find_first(values, threshold):
            ...

        first_shale = ...
        first_shale, log_depth[first_shale]
        '''),
        *question('q2', '''
        ### Q2. Binary search

        Write `depth_index(depths, d)` for a **sorted** list: it returns the index of the first depth `>= d`
        (0 if `d` is above the first depth, `len(depths)` if `d` is deeper than the last). Use the `lo` / `hi` method
        of section 2. Check yourself against `bisect.bisect_left(depths, d)`.
        ''', '''
        def depth_index(depths, d):
            ...

        import bisect
        depth_index(log_depth, 2250.2), bisect.bisect_left(log_depth, 2250.2)
        '''),
        *question('q3', '''
        ### Q3. Selection sort

        Write `selection_sort(values)` that returns a **new** list sorted from smallest to largest, without changing
        `values` and without `sorted`, `.sort()` or `min`. Method: for each position `i`, find the smallest value in
        `i…end`, and swap it into position `i`.
        ''', '''
        def selection_sort(values):
            result = values[:]       # a copy
            ...
            return result

        selection_sort([2.31, 2.05, 2.62, 2.05, 1.98])
        '''),
        *question('q4', '''
        ### Q4. Linear interpolation

        Between two measured points $(x_0, y_0)$ and $(x_1, y_1)$, the straight-line estimate at $x$ is

        $$y = y_0 + (x - x_0)\\,\\frac{y_1 - y_0}{x_1 - x_0}$$

        Write `interp(x, x0, y0, x1, y1)`.
        ''', '''
        def interp(x, x0, y0, x1, y1):
            ...

        interp(5, 0, 10, 10, 30)    # 20.0
        '''),
        *question('q5', '''
        ### Q5. Temperature at any depth

        Write `temperature_at(depth, depths, temps)` that estimates the temperature at `depth` from the survey:
        find the surrounding stations with `depth_index`, then use `interp`. A depth equal to a station gives that
        station's temperature; a depth outside the survey raises `ValueError`. Store in `t_2250` the temperature at
        2250 m, and compare with `np.interp(2250, depths, temps)`.
        ''', '''
        def temperature_at(depth, depths, temps):
            ...

        t_2250 = ...
        t_2250, np.interp(2250, depths, temps)
        '''),
        *closing('''
        ### Going further (not checked)

        * Count the comparisons made by `selection_sort` for 10, 100 and 1000 values. How does the count grow?
          Time it against `sorted` with `%timeit`.
        * Fit a straight line to the survey with `np.polyfit(depths, temps, 1)`: what is the geothermal gradient
          in °C/km? Is one line enough, or are there two?
        '''),
    ]
    save_notebook(NB, 'w12', cells)

def build():
    rows = make_data()
    write_tests('w12', TESTS)
    notebook()
    return f'{len(rows)} temperature stations; {NB} written'
