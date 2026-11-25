# CSC 2301 week 5: lists, tuples, sets and dictionaries, organising drill-hole data by hole.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W5_lists_dicts_drillholes.ipynb'
ASSAYS = 'drillholes_assays.csv'   # from week 1
COLLARS = 'collars.csv'

def make_data():
    rnd = random.Random(2305)
    rows = []
    for k in range(1, 7):
        rows.append({'hole_id': f'DH-{k:02d}', 'easting_m': f'{512000 + rnd.uniform(0, 900):.1f}',
                     'northing_m': f'{745000 + rnd.uniform(0, 700):.1f}', 'elevation_m': f'{rnd.uniform(180, 240):.1f}',
                     'azimuth_deg': rnd.choice([0, 45, 90, 135, 180]), 'dip_deg': rnd.choice([-60, -60, -75, -90])})
    write_csv(COLLARS, rows)
    return rows

RA = ">>> import csv as _csv\n>>> _a = list(_csv.DictReader(open('drillholes_assays.csv', encoding='utf-8')))\n"
RC = ">>> import csv as _csv\n>>> _c = list(_csv.DictReader(open('collars.csv', encoding='utf-8')))\n"
TESTS = {
 "q1": [(">>> bool(isinstance(collars, dict) and len(collars) == 6)\nTrue", "collars must be a dictionary with one entry per hole (6 holes)."),
        (RC + ">>> bool(all(collars[r['hole_id']] == (float(r['easting_m']), float(r['northing_m']), float(r['elevation_m'])) for r in _c))\nTrue",
         "Each value is a tuple of three floats: (easting, northing, elevation).")],
 "q2": [(">>> bool(isinstance(grades_by_hole, dict) and all(isinstance(v, list) for v in grades_by_hole.values()))\nTrue",
         "grades_by_hole maps each hole_id to a list."),
        (RA + ">>> bool(all(grades_by_hole[h] == [int(r['au_ppb']) / 1000 for r in _a if r['hole_id'] == h] for h in {r['hole_id'] for r in _a}))\nTrue",
         "Each list holds the grades of that hole in g/t (au_ppb / 1000), in file order.")],
 "q3": [(RA + ">>> _n = {}\n>>> for r in _a:\n...     _n[r['lithology']] = _n.get(r['lithology'], 0) + 1\n>>> bool(lith_counts == _n)\nTrue",
         "Count the intervals of each lithology: dictionary lithology -> count. dict.get(key, 0) helps.")],
 "q4": [(">>> bool(isinstance(holes_with_vein, list))\nTrue", "holes_with_vein must be a list."),
        (RA + ">>> bool(holes_with_vein == sorted({r['hole_id'] for r in _a if r['lithology'] == 'quartz vein'}))\nTrue",
         "The holes that cut at least one 'quartz vein', each listed once and sorted. A set removes repeats.")],
 "q5": [(">>> round(distance_m((0.0, 0.0, 0.0), (3.0, 4.0, 12.0)), 6)\n5.0", "Horizontal distance only: use easting and northing, ignore elevation."),
        (RC + ">>> _p = {r['hole_id']: (float(r['easting_m']), float(r['northing_m'])) for r in _c}\n"
              ">>> _d = lambda a, b: ((_p[a][0] - _p[b][0]) ** 2 + (_p[a][1] - _p[b][1]) ** 2) ** 0.5\n"
              ">>> bool(nearest_to_dh01 == min((h for h in _p if h != 'DH-01'), key=lambda h: _d('DH-01', h)))\nTrue",
         "nearest_to_dh01 is the hole_id closest to DH-01 (not DH-01 itself).")],
}

def notebook():
    cells = [
        header(5, 'Lists, tuples and dictionaries: organising data by hole', NB, '''
        A drilling campaign produces two kinds of records: **collars** (where each hole starts: coordinates,
        direction) and **intervals** (what was found down the hole). To answer questions such as "which holes cut a
        quartz vein?" or "which hole is closest to DH-01?", you organise the records in the right container.

        **What you will practise:** lists (append, slicing, sorting) · tuples and unpacking · sets ·
        dictionaries (keys, values, `get`, `items`) · a dictionary of lists · choosing the right structure.
        '''),
        setup_cell('w5', [ASSAYS, COLLARS], TESTS),
        otter_cell(),
        md('''
        ## 1. Four containers

        | container | written | order | change? | duplicates | typical use |
        |---|---|---|---|---|---|
        | list | `[1.2, 0.4, 1.2]` | yes | yes | yes | a sequence of measurements |
        | tuple | `(512300.0, 745210.5)` | yes | **no** | yes | a fixed record: a coordinate |
        | set | `{"granite", "schist"}` | no | yes | **no** | "which different values?" |
        | dict | `{"DH-01": 0.42}` | insertion | yes | keys unique | look up a value by its name |
        '''),
        code('''
        grades = [0.2, 1.4, 3.1, 0.8]
        grades.append(0.05)
        print(grades[1:3], sorted(grades, reverse=True)[:2])

        collar = (512300.0, 745210.5, 212.0)     # a tuple cannot be modified
        e, n, z = collar                         # unpacking
        print(e, n, z)

        liths = {"granite", "schist", "granite"}
        print(liths, "schist" in liths)

        mean_grade = {"DH-01": 0.42, "DH-02": 1.05}
        mean_grade["DH-03"] = 2.31               # add a key
        for hole, g in mean_grade.items():
            print(hole, g)
        print(mean_grade.get("DH-09", "no data"))
        '''),
        md('''
        ## 2. The two files
        '''),
        code(f'''
        import csv

        with open("{ASSAYS}", encoding="utf-8") as f:
            assays = list(csv.DictReader(f))
        with open("{COLLARS}", encoding="utf-8") as f:
            collar_rows = list(csv.DictReader(f))

        print(len(assays), "intervals;", len(collar_rows), "collars")
        print(collar_rows[0])
        '''),
        md('''
        ## 3. The "group by" pattern

        Very often you need **one list per key**. Start with an empty dictionary; for each record, create the
        list the first time you meet its key, then append.
        '''),
        code('''
        intervals_by_lith = {}
        for r in assays:
            lith = r["lithology"]
            if lith not in intervals_by_lith:
                intervals_by_lith[lith] = []
            intervals_by_lith[lith].append(r["hole_id"])

        for lith, holes in intervals_by_lith.items():
            print(f"{lith:<12} {len(holes):>3} intervals")
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Collars as tuples

        Build `collars`: a dictionary mapping each `hole_id` to a tuple of three floats
        `(easting_m, northing_m, elevation_m)`.
        ''', '''
        collars = {}
        ...
        collars
        '''),
        *question('q2', '''
        ### Q2. A dictionary of lists

        Build `grades_by_hole`: each `hole_id` maps to the **list** of its grades in g/t (`au_ppb / 1000`),
        in file order.
        ''', '''
        grades_by_hole = {}
        ...
        {h: len(v) for h, v in grades_by_hole.items()}
        '''),
        *question('q3', '''
        ### Q3. Counting with a dictionary

        Build `lith_counts`: lithology → number of intervals of that lithology.
        ''', '''
        lith_counts = {}
        ...
        lith_counts
        '''),
        *question('q4', '''
        ### Q4. A set to remove repeats

        Gold is often in **quartz veins**. Store in `holes_with_vein` the **sorted list** of the holes that cut at
        least one `quartz vein` interval, each hole once.
        ''', '''
        holes_with_vein = ...
        holes_with_vein
        '''),
        *question('q5', '''
        ### Q5. The nearest hole

        1. Write `distance_m(c1, c2)` that takes two collar tuples and returns the **horizontal** distance between
           them in metres: $\\sqrt{(E_1-E_2)^2 + (N_1-N_2)^2}$ (ignore the elevation).
        2. Store in `nearest_to_dh01` the hole_id closest to `DH-01` (not DH-01 itself).
        ''', '''
        def distance_m(c1, c2):
            ...

        nearest_to_dh01 = ...
        nearest_to_dh01
        '''),
        *closing('''
        ### Going further (not checked)

        * Build a **distance table**: a dictionary whose keys are tuples `(hole_a, hole_b)` and whose values are distances.
          Why can a tuple be a dictionary key but a list cannot?
        * Which lithology has the highest mean grade? Combine `grades_by_hole`'s idea with `lith_counts`.
        '''),
    ]
    save_notebook(NB, 'w5', cells)

def build():
    rows = make_data()
    write_tests('w5', TESTS)
    notebook()
    return f'{len(rows)} collars; {NB} written'
