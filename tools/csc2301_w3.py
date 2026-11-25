# CSC 2301 week 3: functions (parameters, return values, defaults, several results) on a block model.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W3_functions_block_model.ipynb'
DATA = 'block_model_pit1.csv'

def make_data():
    rnd = random.Random(2303)
    rows = []
    for i in range(12):
        for j in range(10):
            # a richer zone in the middle of the pit, lognormal grades around it
            centre = ((i - 6) ** 2 + (j - 4) ** 2) ** 0.5
            mean = 1.6 if centre < 3 else 0.6 if centre < 5 else 0.25
            rock = 'oxide' if j < 3 else 'fresh'
            rows.append({'block_id': f'B{i:02d}{j:02d}', 'x_m': 10 * i + 5, 'y_m': 10 * j + 5,
                         'dx_m': 10, 'dy_m': 10, 'dz_m': 5,
                         'density_t_m3': f'{(2.15 if rock == "oxide" else 2.70) + rnd.gauss(0, 0.04):.2f}',
                         'au_gpt': f'{rnd.lognormvariate(0, 0.8) * mean:.2f}', 'rock': rock})
    write_csv(DATA, rows)
    return rows

READ = (">>> import csv as _csv\n>>> _b = list(_csv.DictReader(open('block_model_pit1.csv', encoding='utf-8')))\n"
        ">>> _t = lambda r: float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) * float(r['density_t_m3'])\n")
TESTS = {
 "q1": [(">>> bool(callable(block_tonnes))\nTrue", "Define a function called block_tonnes."),
        (">>> round(block_tonnes(10, 10, 5, 2.7), 6)\n1350.0", "Tonnes = length × width × height × density (10 × 10 × 5 × 2.7 = 1350)."),
        (">>> round(block_tonnes(2, 3, 4, 1.0), 6)\n24.0", "Use all four parameters in the order (length, width, height, density).")],
 "q2": [(">>> round(gold_ounces(1000, 31.1035), 6)\n1000.0", "Grams of gold = tonnes × grade (g/t); one troy ounce is 31.1035 g."),
        (">>> round(gold_ounces(1350, 2.0), 3)\n86.807", "Divide the grams by 31.1035, do not round inside the function.")],
 "q3": [(">>> round(hydrostatic_mpa(1000), 4)\n10.1043", "With the default density 1.03 g/cm³: P = depth × density × 9.81 ÷ 1000."),
        (">>> round(hydrostatic_mpa(2000, 1.20), 4)\n23.544", "The second parameter, density, must replace the default when it is given.")],
 "q4": [(">>> bool(isinstance(block_summary({'dx_m': '10', 'dy_m': '10', 'dz_m': '5', 'density_t_m3': '2.70', 'au_gpt': '2.00'}), tuple))\nTrue",
         "block_summary must return a tuple: return tonnes, ounces"),
        (">>> [round(v, 3) for v in block_summary({'dx_m': '10', 'dy_m': '10', 'dz_m': '5', 'density_t_m3': '2.70', 'au_gpt': '2.00'})]\n[1350.0, 86.807]",
         "Read the values from the row (they are text: convert with float), then reuse block_tonnes and gold_ounces.")],
 "q5": [(">>> bool(isinstance(ore_tonnes, float) and isinstance(ore_ounces, float))\nTrue", "ore_tonnes and ore_ounces must be floats."),
        (READ + ">>> _o = [r for r in _b if float(r['au_gpt']) >= 0.5]\n"
                ">>> bool(abs(ore_tonnes - sum(_t(r) for r in _o)) < 1e-3)\nTrue", "Add the tonnes of the blocks whose grade is at least the 0.5 g/t cut-off."),
        (READ + ">>> _o = [r for r in _b if float(r['au_gpt']) >= 0.5]\n"
                ">>> bool(abs(ore_ounces - sum(_t(r) * float(r['au_gpt']) / 31.1035 for r in _o)) < 1e-3)\nTrue",
         "Add the ounces of the same ore blocks (grade ≥ 0.5 g/t).")],
}

def notebook():
    cells = [
        header(3, 'Functions: reusable engineering formulas', NB, '''
        Engineers use the same formulas again and again: tonnage of a block, metal content, pressure at depth.
        A **function** gives a formula a name, so you write it once, test it once and reuse it everywhere.
        The data are a small **block model** of an open-pit gold mine (synthetic): 120 blocks of 10 m × 10 m × 5 m,
        each with a density and a gold grade.

        **What you will practise:** `def` and `return` · parameters and arguments · default values ·
        returning several results · docstrings · calling a function from another function · local variables.
        '''),
        setup_cell('w3', [DATA], TESTS),
        otter_cell(),
        md('''
        ## 1. Why functions?

        Without a function, the tonnage formula is copied every time it is needed, and every copy is a chance
        to make a mistake. With a function, the formula lives in **one place**.
        '''),
        code('''
        def block_volume(length_m, width_m, height_m):
            """Volume of a rectangular block, in m³."""
            return length_m * width_m * height_m

        v = block_volume(10, 10, 5)
        print(v, "m³")
        help(block_volume)      # the docstring is the function's user manual
        '''),
        md('''
        * `def` starts the definition; the **parameters** are the names in brackets.
        * When you **call** the function, the **arguments** (10, 10, 5) are given to the parameters in order.
        * `return` sends the result back. A function without `return` gives `None`.
        * Variables created inside a function are **local**: they disappear when the function ends.
        '''),
        code('''
        def stripping_ratio(waste_t, ore_t):
            ratio = waste_t / ore_t     # 'ratio' only exists inside the function
            return ratio

        print(stripping_ratio(4_500_000, 1_500_000))   # 3 t of waste per t of ore
        # print(ratio)   # would fail: NameError, ratio is local
        '''),
        md('''
        ## 2. Default values and keyword arguments

        A parameter can have a **default value**, used when the caller does not give one.
        Arguments can also be passed **by name**, which makes long calls easier to read.
        '''),
        code('''
        def mud_weight_ppg(density_g_cm3=1.20):
            """Drilling mud density in pounds per gallon (1 g/cm³ = 8.345 ppg)."""
            return density_g_cm3 * 8.345

        print(round(mud_weight_ppg(), 2))                     # uses the default 1.20
        print(round(mud_weight_ppg(1.45), 2))                 # positional argument
        print(round(mud_weight_ppg(density_g_cm3=1.45), 2))   # keyword argument
        '''),
        md('''
        ## 3. Returning several results

        `return a, b` returns a **tuple**. The caller can unpack it into two names.
        '''),
        code('''
        def min_max(values):
            return min(values), max(values)

        low, high = min_max([0.2, 1.4, 3.1, 0.8])
        print(low, high)
        '''),
        md('''
        ## 4. The block model
        '''),
        code(f'''
        import csv

        with open("{DATA}", encoding="utf-8") as f:
            blocks = list(csv.DictReader(f))

        print(len(blocks), "blocks")
        print(blocks[0])
        '''),
        md('''
        ---
        ## Exercises

        ### Q1. Tonnage of a block

        Write `block_tonnes(length_m, width_m, height_m, density_t_m3)` that returns the tonnage of a block.
        You may reuse `block_volume` from section 1.
        '''),
        *question('q1', '', '''
        def block_tonnes(length_m, width_m, height_m, density_t_m3):
            ...

        block_tonnes(10, 10, 5, 2.7)
        ''')[1:],
        *question('q2', '''
        ### Q2. Gold content in ounces

        Gold is sold in **troy ounces**: 1 oz = 31.1035 g. A grade of 1 g/t means 1 gram of gold per tonne of rock.
        Write `gold_ounces(tonnes, grade_gpt)` that returns the ounces of gold in `tonnes` of rock at `grade_gpt`.
        ''', '''
        def gold_ounces(tonnes, grade_gpt):
            ...

        gold_ounces(1350, 2.0)
        '''),
        *question('q3', '''
        ### Q3. A default value: pressure at depth

        The **hydrostatic pressure** of a column of fluid, in MPa, is

        $$P = \\frac{\\text{depth (m)} \\times \\text{density (g/cm³)} \\times 9.81}{1000}$$

        Write `hydrostatic_mpa(depth_m, density_g_cm3=1.03)`. The default 1.03 g/cm³ is sea water;
        drillers pass the mud density instead.
        ''', '''
        def hydrostatic_mpa(depth_m, density_g_cm3=1.03):
            ...

        hydrostatic_mpa(1000), hydrostatic_mpa(2000, 1.20)
        '''),
        *question('q4', '''
        ### Q4. One function calling two others

        Write `block_summary(row)` that takes **one row** of the block model (a dictionary read from the CSV)
        and returns a tuple `(tonnes, ounces)`. Reuse `block_tonnes` and `gold_ounces`; remember that values
        read from a CSV file are text.
        ''', '''
        def block_summary(row):
            ...

        block_summary(blocks[0])
        '''),
        *question('q5', '''
        ### Q5. Ore above the cut-off

        A block is **ore** when its grade is at least the **cut-off grade**, here 0.5 g/t. Below, it is waste.
        Using your functions, store in `ore_tonnes` the total tonnes of ore and in `ore_ounces` the total
        ounces of gold they contain (both floats).
        ''', '''
        CUTOFF = 0.5
        ore_tonnes = 0.0
        ore_ounces = 0.0
        ...
        ore_tonnes, ore_ounces
        '''),
        *closing('''
        ### Going further (not checked)

        * Turn the cut-off into a parameter: write `ore_above(blocks, cutoff)` that returns `(tonnes, ounces)`,
          and print the results for cut-offs of 0.3, 0.5, 0.8 and 1.0 g/t. This table is a **grade–tonnage curve**.
        * Add a docstring to each of your functions and read it back with `help()`.
        '''),
    ]
    save_notebook(NB, 'w3', cells)

def build():
    rows = make_data()
    write_tests('w3', TESTS)
    notebook()
    return f'{len(rows)} blocks; {NB} written'
