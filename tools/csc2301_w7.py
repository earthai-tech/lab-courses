# CSC 2301 week 7: review and mini-project, from a raw campaign file to a short written report.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W7_review_mini_project.ipynb'
DATA = 'campaign_rc_assays.csv'

def make_data():
    rnd = random.Random(2307)
    rows = []
    for k in range(1, 9):
        hole, depth = f'RC-{k:02d}', 0.0
        zone_top = rnd.uniform(8, 30); zone_len = rnd.uniform(4, 14)
        for _ in range(rnd.randint(18, 26)):
            length = rnd.choice([1.0, 2.0, 2.0])
            mid = depth + length / 2
            mean = 2.2 if zone_top <= mid <= zone_top + zone_len else 0.3
            g = rnd.lognormvariate(0, 0.6) * mean
            s = f'{g:.2f}'
            r = rnd.random()
            if r < 0.04: s = 'NS'           # no sample
            elif r < 0.06: s = '-9.99'      # error code from the lab system
            rows.append({'hole_id': hole, 'from_m': f'{depth:.1f}', 'to_m': f'{depth + length:.1f}', 'au_gpt': s})
            depth += length
    write_csv(DATA, rows)
    return rows

REF = '''>>> import csv as _csv
>>> def _g(s):
...     try:
...         v = float(s)
...     except ValueError:
...         return None
...     return v if v >= 0 else None
>>> _all = list(_csv.DictReader(open('campaign_rc_assays.csv', encoding='utf-8')))
>>> _iv = [(r['hole_id'], float(r['from_m']), float(r['to_m']), _g(r['au_gpt'])) for r in _all]
>>> _ok = [x for x in _iv if x[3] is not None]
>>> _holes = sorted({x[0] for x in _iv})
>>> def _wm(xs):
...     return sum((t - f) * g for h, f, t, g in xs) / sum(t - f for h, f, t, g in xs)
>>> def _best(xs, c=1.0):
...     best, run = None, []
...     for x in xs + [None]:
...         if x is not None and x[3] >= c:
...             run.append(x)
...             continue
...         if run:
...             m = sum((t - f) * g for h, f, t, g in run)
...             if best is None or m > best[0]:
...                 best = (m, run[0][1], run[-1][2], _wm(run))
...         run = []
...     return None if best is None else best[1:]
'''
TESTS = {
 "q1": [(REF + ">>> bool(n_valid == len(_ok))\nTrue", "Keep the intervals whose grade is a number ≥ 0: 'NS' and the error code -9.99 are not grades."),
        (REF + ">>> bool([(x['hole_id'], x['from_m'], x['to_m'], x['au_gpt']) for x in intervals] == _ok)\nTrue",
         "intervals: list of dicts (hole_id, from_m, to_m, au_gpt) with floats, valid grades only, in file order.")],
 "q2": [(REF + ">>> _m = {}\n>>> for h, f, t, g in _iv:\n...     _m[h] = _m.get(h, 0) + t - f\n>>> bool(all(abs(metres_by_hole[h] - _m[h]) < 1e-9 for h in _m) and len(metres_by_hole) == len(_m))\nTrue",
         "Drilled metres count every interval of the file, sampled or not.")],
 "q3": [(">>> round(weighted_mean([{'from_m': 0.0, 'to_m': 2.0, 'au_gpt': 1.0}, {'from_m': 2.0, 'to_m': 3.0, 'au_gpt': 4.0}]), 6)\n2.0",
         "Length-weighted: (2 × 1 + 1 × 4) / 3 = 2."),
        (REF + ">>> bool(all(abs(hole_grades[h] - _wm([x for x in _ok if x[0] == h])) < 1e-6 for h in _holes))\nTrue",
         "hole_grades: hole_id -> weighted mean grade of that hole's valid intervals.")],
 "q4": [(">>> _b = best_intercept([{'from_m': 0.0, 'to_m': 1.0, 'au_gpt': 0.2}, {'from_m': 1.0, 'to_m': 3.0, 'au_gpt': 2.0}, {'from_m': 3.0, 'to_m': 4.0, 'au_gpt': 1.0}, {'from_m': 4.0, 'to_m': 5.0, 'au_gpt': 0.1}])\n>>> (_b[0], _b[1], round(_b[2], 6))\n(1.0, 4.0, 1.666667)",
         "Join consecutive intervals with grade ≥ 1.0 into a run; return (from_m of the first, to_m of the last, weighted mean)."),
        (REF + ">>> _r = {h: _best([x for x in _ok if x[0] == h]) for h in _holes}\n"
               ">>> _s = {h: best_intercept([x for x in intervals if x['hole_id'] == h]) for h in _holes}\n"
               ">>> bool(all((_r[h] is None and _s[h] is None) or (_s[h] is not None and all(abs(a - b) < 1e-6 for a, b in zip(_r[h], _s[h]))) for h in _holes))\nTrue",
         "When a hole has several runs, keep the one with the most metal: the largest sum of grade × length. No run: return None.")],
 "q5": [(REF + ">>> _m = {}\n>>> for h, f, t, g in _iv:\n...     _m[h] = _m.get(h, 0) + t - f\n"
               ">>> def _line(h):\n...     b = _best([x for x in _ok if x[0] == h])\n"
               "...     tail = 'best none' if b is None else f'best {b[0]:.1f}-{b[1]:.1f} m at {b[2]:.2f} g/t'\n"
               "...     return f'{h}: {_m[h]:.1f} m drilled, mean {_wm([x for x in _ok if x[0] == h]):.2f} g/t, ' + tail\n"
               ">>> _got = open('campaign_report.txt', encoding='utf-8').read().splitlines()\n"
               ">>> bool(_got == [_line(h) for h in _holes])\nTrue",
         "One line per hole, sorted by hole_id, exactly in the format shown in the question.")],
}

def notebook():
    cells = [
        header(7, 'Review and mini-project: a drilling campaign report', NB, '''
        Halfway through the course: time to put everything together. A reverse-circulation (RC) drilling campaign
        of 8 holes has just been assayed (synthetic data). Your manager wants a **one-page report**: metres drilled,
        mean grade and the best mineralised intercept of each hole.

        Each question reuses one week of the course: reading files and types (W1), loops and decisions (W2),
        functions (W3), strings and formatting (W4), dictionaries (W5), handling bad data (W6).
        Work in small steps and check each result before moving on.
        '''),
        setup_cell('w7', [DATA], TESTS),
        otter_cell(),
        md('''
        ## The brief

        * `au_gpt` is the gold grade in g/t. The lab wrote `NS` (no sample) or the error code `-9.99` for some intervals:
          these are **not** grades.
        * **Metres drilled** count every interval; **grades** use only valid intervals, **weighted by length**.
        * An **intercept** is a run of **consecutive** valid intervals with grade ≥ 1.0 g/t. Geologists report the best one
          as, for example, *"12.0–18.0 m at 2.41 g/t"*. The best is the one with the most metal (grade × length).

        Start by looking at the file.
        '''),
        code(f'''
        import csv

        with open("{DATA}", encoding="utf-8") as f:
            raw = list(csv.DictReader(f))
        print(len(raw), "rows")
        for r in raw[:6]:
            print(r)
        print({{r["au_gpt"] for r in raw if not r["au_gpt"].replace(".", "").isdigit()}})
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Clean intervals

        Build `intervals`: a list of dictionaries with keys `hole_id`, `from_m`, `to_m`, `au_gpt` (floats), only
        for the rows with a **valid** grade (a number ≥ 0), in file order. Store their number in `n_valid`.
        A `safe_float` like last week's helps.
        ''', '''
        intervals = []
        ...
        n_valid = len(intervals)
        n_valid
        '''),
        *question('q2', '''
        ### Q2. Metres drilled per hole

        Build `metres_by_hole`: hole_id → total length drilled, using **all** rows of the file (`raw`), sampled or not.
        ''', '''
        metres_by_hole = {}
        ...
        metres_by_hole
        '''),
        *question('q3', '''
        ### Q3. Mean grade per hole

        Write `weighted_mean(rows)` that returns the length-weighted mean grade of a list of interval dictionaries,
        then build `hole_grades`: hole_id → weighted mean of that hole's valid intervals.
        ''', '''
        def weighted_mean(rows):
            ...

        hole_grades = {}
        ...
        hole_grades
        '''),
        *question('q4', '''
        ### Q4. Best intercept

        Write `best_intercept(rows, cutoff=1.0)` for the valid intervals of **one hole** (in depth order). It joins
        consecutive intervals with grade ≥ `cutoff` into runs and returns the run with the most metal as a tuple
        `(from_m, to_m, weighted_mean_grade)`, or `None` if no interval reaches the cut-off.

        *Hint:* build the current run in a list; when an interval is below the cut-off (or the hole ends), the run is
        finished: compare it with the best so far and start a new one. Reuse `weighted_mean`.
        ''', '''
        def best_intercept(rows, cutoff=1.0):
            ...

        best_intercept([r for r in intervals if r["hole_id"] == "RC-01"])
        '''),
        *question('q5', '''
        ### Q5. The report

        Write `campaign_report.txt` with one line per hole, **sorted by hole_id**, exactly in this format:

        ```
        RC-01: 44.0 m drilled, mean 0.83 g/t, best 14.0-22.0 m at 2.35 g/t
        ```

        (1 decimal for metres and depths, 2 for grades). For a hole without intercept, end the line with `best none`.
        ''', '''
        lines = []
        ...
        with open("campaign_report.txt", "w", encoding="utf-8") as f:
            f.write("\\n".join(lines) + "\\n")
        print(open("campaign_report.txt", encoding="utf-8").read())
        '''),
        *closing('''
        ### Going further (not checked)

        * Change the cut-off to 0.5 g/t and to 2.0 g/t. How do the intercepts change? Why do companies like to
          choose the cut-off that gives the most impressive headline?
        * Add the share of intervals not sampled (`NS`) to each line: is any hole less reliable than the others?
        '''),
    ]
    save_notebook(NB, 'w7', cells)

def build():
    rows = make_data()
    write_tests('w7', TESTS)
    notebook()
    return f'{len(rows)} RC intervals; {NB} written'
