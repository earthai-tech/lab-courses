# CSC 2301 week 11: modules, imports and a small reusable geotools module with docstrings.
# Built by tools/make_csc2301.py, which imports this file and calls build().
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'CSC2301_W11_modules_geotools.ipynb'
FILES = ['block_model_pit1.csv']   # from week 3

GT = ">>> import importlib as _il, geotools as _gt\n>>> _gt = _il.reload(_gt)\n"
READ = (">>> import csv as _csv\n>>> _b = list(_csv.DictReader(open('block_model_pit1.csv', encoding='utf-8')))\n"
        ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) * float(r['density_t_m3']) for r in _b]\n"
        ">>> _g = [float(r['au_gpt']) for r in _b]\n")
TESTS = {
 "q1": [(GT + ">>> _gt.GOLD_OZ_G\n31.1035", "geotools.py must define the constant GOLD_OZ_G = 31.1035 (grams in one troy ounce)."),
        (GT + ">>> (round(_gt.block_tonnes(10, 10, 5, 2.7), 6), round(_gt.gold_ounces(1350, 2.0), 3))\n(1350.0, 86.807)",
         "Copy your week 3 block_tonnes and gold_ounces into geotools.py; gold_ounces must use GOLD_OZ_G."),
        (GT + ">>> bool(_gt.block_tonnes.__doc__ and _gt.gold_ounces.__doc__)\nTrue",
         "Each function needs a docstring: a \"\"\"text\"\"\" line right under the def.")],
 "q2": [(GT + ">>> [round(_gt.vshale(g), 3) for g in (10, 30, 75, 120, 150)]\n[0.0, 0.0, 0.5, 1.0, 1.0]",
         "vshale(gr, gr_clean=30.0, gr_shale=120.0): (gr - gr_clean) / (gr_shale - gr_clean), clipped to 0–1."),
        (GT + ">>> round(_gt.vshale(77.5, gr_clean=25, gr_shale=130), 3)\n0.5", "The clean and shale lines are parameters with default values."),
        (GT + ">>> bool(_gt.vshale.__doc__)\nTrue", "Give vshale a docstring too.")],
 "q3": [(READ + ">>> bool(abs(total_t - sum(_t)) < 1e-6)\nTrue", "total_t: the tonnes of all 120 blocks, using geotools.block_tonnes (values from the file are text)."),
        (READ + ">>> bool(abs(total_oz - sum(t * g / 31.1035 for t, g in zip(_t, _g))) < 1e-6)\nTrue",
         "total_oz: the ounces of all blocks, using geotools.gold_ounces on each block.")],
 "q4": [(READ + ">>> import statistics as _st\n>>> bool(abs(median_grade - _st.median(_g)) < 1e-12 and abs(stdev_grade - _st.stdev(_g)) < 1e-12)\nTrue",
         "Use the standard-library module statistics: statistics.median and statistics.stdev on the grades."),
        (READ + ">>> from collections import Counter as _C\n>>> bool(rock_counts == _C(r['rock'] for r in _b))\nTrue",
         "rock_counts = Counter(...) of the rock column: from collections import Counter.")],
 "q5": [(">>> _src = open('report.py', encoding='utf-8').read()\n>>> bool('geotools' in _src and '__main__' in _src)\nTrue",
         "report.py must import geotools and call main() under if __name__ == \"__main__\":"),
        (READ + ">>> _oz = sum(t * g / 31.1035 for t, g in zip(_t, _g))\n"
                ">>> bool(open('pit1_report.txt', encoding='utf-8').read().strip() == f'Pit 1: {len(_b)} blocks, {sum(_t):.0f} t, {_oz:.1f} oz')\nTrue",
         "Run the script with %run report.py; it writes one line: Pit 1: 120 blocks, <tonnes, 0 decimals> t, <ounces, 1 decimal> oz")],
}

def notebook():
    cells = [
        header(11, 'Modules: reusable code in a file', NB, '''
        Since week 3 you have rewritten `block_tonnes`, `gold_ounces` and `vshale` in several notebooks. Engineers
        put the functions they trust in a **module**, a `.py` file, and **import** it wherever they need it:
        one place to fix a bug, one place to test. This week you build `geotools.py`, your own small toolbox.

        **What you will practise:** `import`, `from … import`, `as` · the standard library (`math`, `statistics`,
        `collections`) · writing a module with `%%writefile` · docstrings and `help` · `importlib.reload` ·
        scripts and `if __name__ == "__main__":`.
        '''),
        setup_cell('w11', FILES, TESTS),
        otter_cell(),
        md('''
        ## 1. Three ways to import
        '''),
        code('''
        import math                      # the module: use math.sqrt
        from statistics import mean      # one name from a module
        import numpy as np               # a module with a short alias

        print(math.sqrt(2), math.pi)
        print(mean([2.1, 2.5, 2.3]))
        print(np.array([1, 2, 3]) * 2)
        '''),
        code('''
        help(math.hypot)                 # every good function has a docstring
        print([n for n in dir(math) if not n.startswith("_")][:12])
        '''),
        md('''
        ## 2. Your own module

        A module is just a `.py` file. In a notebook, the magic `%%writefile name.py` **must be the first line** of
        the cell: it saves the rest of the cell as a file instead of running it.
        '''),
        code('''
        %%writefile units.py
        """Unit conversions used in mining and petroleum engineering."""

        FT_PER_M = 3.28084

        def m_to_ft(m):
            """Convert metres to feet."""
            return m * FT_PER_M

        def psi_to_mpa(psi):
            """Convert pounds per square inch to megapascals."""
            return psi * 0.00689476
        '''),
        code('''
        import units

        print(units.m_to_ft(1500))
        print(units.psi_to_mpa(3000))
        help(units)
        '''),
        md('''
        **Changed the file?** Python imports a module only once per session. After editing, reload it:
        `import importlib; importlib.reload(units)` (or restart the runtime).

        ## 3. Scripts and `__name__`

        When a file is **run** (`python report.py`, or `%run report.py` in a notebook), its `__name__` is
        `"__main__"`. When it is **imported**, `__name__` is the module name. So code under
        `if __name__ == "__main__":` runs only when the file is used as a script.
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Start `geotools.py`

        Complete the cell and run it to write `geotools.py`. It must contain the constant `GOLD_OZ_G = 31.1035` and
        your week 3 functions `block_tonnes` and `gold_ounces` (which must use `GOLD_OZ_G`), each with a docstring.
        ''', '''
        %%writefile geotools.py
        """geotools: small helpers for mining and petroleum calculations."""

        GOLD_OZ_G = 31.1035      # grams in one troy ounce

        def block_tonnes(length_m, width_m, height_m, density_t_m3):
            """Tonnage of a rectangular block."""
            ...

        def gold_ounces(tonnes, grade_gpt):
            ...
        '''),
        *question('q2', '''
        ### Q2. Add `vshale`

        `%%writefile -a` **appends** to the file. Add `vshale(gr, gr_clean=30.0, gr_shale=120.0)` that returns
        $(GR - GR_{clean}) / (GR_{shale} - GR_{clean})$ clipped to 0–1 (your week 2 function, now with parameters
        and default values), with a docstring that says what the parameters are.
        ''', '''
        %%writefile -a geotools.py

        def vshale(gr, gr_clean=30.0, gr_shale=120.0):
            ...
        '''),
        *question('q3', '''
        ### Q3. Use the module

        Reload `geotools`, read `block_model_pit1.csv` with `csv.DictReader`, and store in `total_t` the tonnes and in
        `total_oz` the ounces of **all** blocks, using `geotools.block_tonnes` and `geotools.gold_ounces`.
        ''', '''
        import csv, importlib
        import geotools
        importlib.reload(geotools)

        with open("block_model_pit1.csv", encoding="utf-8") as f:
            blocks = list(csv.DictReader(f))

        total_t = 0.0
        total_oz = 0.0
        ...
        total_t, total_oz
        '''),
        *question('q4', '''
        ### Q4. The standard library does it for you

        With the grades of the blocks (floats), store in `median_grade` and `stdev_grade` the median and the
        sample standard deviation (module `statistics`), and in `rock_counts` a `Counter` of the `rock` column
        (`from collections import Counter`). No loop needed.
        ''', '''
        import statistics
        from collections import Counter

        grades = [float(b["au_gpt"]) for b in blocks]
        median_grade = ...
        stdev_grade = ...
        rock_counts = ...
        median_grade, stdev_grade, rock_counts
        '''),
        *question('q5', '''
        ### Q5. A script that uses your module

        Complete `report.py`: its `main()` reads the block model, uses `geotools` to compute the totals and writes
        **one line** to `pit1_report.txt`, in this format:

        ```
        Pit 1: 120 blocks, 123456 t, 1234.5 oz
        ```

        (your numbers will differ: tonnes with 0 decimals, ounces with 1). Then run it with `%run report.py`.
        ''', '''
        %%writefile report.py
        """Write the Pit 1 summary line to pit1_report.txt."""
        import csv
        import geotools

        def main():
            ...

        if __name__ == "__main__":
            main()
        ''')[:2],
        code('''
        %run report.py
        print(open("pit1_report.txt", encoding="utf-8").read())
        '''),
        code('grader.check("q5")'),
        *closing('''
        ### Going further (not checked)

        * Add `hydrostatic_mpa` and `distance_m` from weeks 3 and 5 to `geotools.py`, then `help(geotools)`.
        * Download `geotools.py` and import it in your week 10 notebook: does `weighted_by_hole` get shorter?
        '''),
    ]
    save_notebook(NB, 'w11', cells)

def build():
    write_tests('w11', TESTS)
    notebook()
    return f'{NB} written (reuses week 3 data)'
