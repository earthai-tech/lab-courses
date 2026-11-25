# CSC 2301 week 6: errors, exceptions, debugging and testing on daily well production records.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import datetime, random
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, write_csv

NB = 'CSC2301_W6_errors_testing_production.ipynb'
DATA = 'production_daily_kw1.csv'

def make_data():
    rnd = random.Random(2306)
    rows, day = [], datetime.date(2024, 1, 1)
    oil, wc = 950.0, 0.08
    for k in range(120):
        oil *= 0.997; wc = min(0.9, wc + 0.0025)
        o = oil * (1 - wc) / (1 - 0.08) * rnd.uniform(0.95, 1.05)
        w = o * wc / (1 - wc)
        so, sw = f'{o:.1f}', f'{w:.1f}'
        r = rnd.random()
        if r < 0.04: so = 'N/A'            # meter not read
        elif r < 0.07: sw = ''             # missing
        elif r < 0.09: so = f'-{o:.1f}'    # sign error
        elif r < 0.11: sw = f'{w:.1f}'.replace('.', ',')  # decimal comma
        elif k in (40, 41): so, sw = '0.0', '0.0'          # well shut in
        rows.append({'date': day.isoformat(), 'oil_bbl': so, 'water_bbl': sw})
        day += datetime.timedelta(days=1)
    write_csv(DATA, rows)
    return rows

REF = '''>>> import csv as _csv
>>> def _f(s):
...     try:
...         return float(s)
...     except ValueError:
...         return None
>>> _rows = list(_csv.DictReader(open('production_daily_kw1.csv', encoding='utf-8')))
>>> _ok = [(r['date'], _f(r['oil_bbl']), _f(r['water_bbl'])) for r in _rows]
>>> _ok = [(d, o, w) for d, o, w in _ok if o is not None and w is not None and o >= 0 and w >= 0]
'''
TESTS = {
 "q1": [(">>> [safe_float(s) for s in ('12.5', ' 3 ', '-4.0')]\n[12.5, 3.0, -4.0]", "Return float(s) when the conversion works."),
        (">>> [safe_float(s) for s in ('N/A', '', '1,5', 'abc')]\n[None, None, None, None]",
         "Catch the ValueError with try/except and return None. Do not use a bare except.")],
 "q2": [(">>> [water_cut(90.0, 10.0), water_cut(50.0, 50.0), water_cut(0.0, 20.0)]\n[0.1, 0.5, 1.0]", "Water cut = water / (oil + water)."),
        (">>> try:\n...     water_cut(0.0, 0.0)\n... except ValueError:\n...     print('ValueError')\nValueError",
         "When oil + water is 0 the water cut is undefined: raise ValueError (not ZeroDivisionError)."),
        (">>> try:\n...     water_cut(-5.0, 10.0)\n... except ValueError:\n...     print('ValueError')\nValueError", "A negative volume is impossible: raise ValueError.")],
 "q3": [(REF + ">>> bool(n_days == len(_rows))\nTrue", "n_days counts every data line of the file."),
        (REF + ">>> bool(n_bad == len(_rows) - len(_ok))\nTrue",
         "A day is bad when oil or water cannot be read as a number (safe_float gives None) or is negative.")],
 "q4": [(">>> average_positive([2.0, -1.0, 4.0, 0.0])\n3.0", "Average only the values that are > 0: (2 + 4) / 2 = 3."),
        (">>> average_positive([5.0])\n5.0", "One value: the average is that value."),
        (">>> print(average_positive([-1.0, 0.0]))\nNone", "No positive value: return None instead of dividing by zero.")],
 "q5": [(REF + ">>> bool(abs(cum_oil_bbl - sum(o for d, o, w in _ok)) < 1e-6)\nTrue", "Add the oil of the valid days only."),
        (REF + ">>> _wc = [(w / (o + w), d) for d, o, w in _ok if o + w > 0]\n>>> bool(worst_day == max(_wc)[1])\nTrue",
         "worst_day is the date (text) with the highest water cut among valid days with oil + water > 0.")],
}

def notebook():
    cells = [
        header(6, 'Errors, debugging and testing', NB, '''
        Every programmer writes bugs; good engineers **find them fast** and **stop them coming back**.
        This week you read error messages, handle bad data without crashing, fix a broken function, and
        test your code with `assert`. The data are 120 days of oil and water production from well KW-1
        (synthetic), recorded by hand: some days are missing, misspelt or impossible.

        **What you will practise:** reading a traceback · the common exceptions · `try` / `except` / `else` ·
        `raise` · `assert` · a simple debugging method (print, isolate, fix, test).
        '''),
        setup_cell('w6', [DATA], TESTS),
        otter_cell(),
        md('''
        ## 1. Read the error from the bottom

        A **traceback** lists the calls that led to the error. The **last line** says what went wrong;
        the line above it says where. Run the cell and read it.
        '''),
        code('''
        def daily_total(oil, water):
            return oil + water

        import traceback
        try:
            daily_total("812.4", 95.0)    # one value is text: TypeError
        except TypeError:
            traceback.print_exc()         # shows the traceback without stopping "Run all"
        '''),
        md('''
        | exception | typical cause |
        |---|---|
        | `SyntaxError` | a typo: missing `:` or bracket |
        | `NameError` | a name not defined yet (cell not run?) |
        | `TypeError` | wrong type: `"3" + 1` |
        | `ValueError` | right type, wrong value: `float("N/A")` |
        | `ZeroDivisionError` | dividing by 0 |
        | `KeyError` / `IndexError` | missing key / position past the end |

        ## 2. Handling an error: `try` / `except`
        '''),
        code('''
        for s in ["812.4", "N/A", "95,0"]:
            try:
                value = float(s)
            except ValueError:
                print(repr(s), "is not a number")
            else:
                print(repr(s), "->", value)
        '''),
        md('''
        Catch **only the error you expect** (`except ValueError`), never a bare `except:`: it would also hide
        your own bugs.

        ## 3. Raising an error yourself

        When a function receives impossible input, **stop loudly** with `raise` rather than return a wrong number.
        '''),
        code('''
        def gor(gas_scf, oil_bbl):
            """Gas-oil ratio in scf/bbl."""
            if oil_bbl <= 0:
                raise ValueError(f"oil must be positive, got {oil_bbl}")
            return gas_scf / oil_bbl

        print(gor(450_000, 900))
        try:
            gor(450_000, 0)
        except ValueError as e:
            print("Refused:", e)
        '''),
        md('''
        ## 4. Testing with `assert`

        `assert condition` does nothing when the condition is true, and raises `AssertionError` when it is false.
        A **test** is a few asserts on cases where you know the answer by hand.
        '''),
        code('''
        def test_gor():
            assert gor(1000, 10) == 100
            assert gor(0, 5) == 0
            try:
                gor(1000, 0)
                assert False, "gor should refuse oil = 0"
            except ValueError:
                pass
            print("all gor tests passed")

        test_gor()
        '''),
        md('''
        ## 5. The data
        '''),
        code(f'''
        import csv

        with open("{DATA}", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        print(len(rows), "days")
        for r in rows[:12]:
            print(r)
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. A conversion that never crashes

        Write `safe_float(s)` that returns `float(s)` when possible and `None` when `s` is not a valid number
        (`'N/A'`, `''`, `'1,5'`…). Use `try` / `except ValueError`.
        ''', '''
        def safe_float(s):
            ...

        [safe_float(s) for s in ("12.5", "N/A", "", "1,5")]
        '''),
        *question('q2', '''
        ### Q2. Water cut, with honest errors

        The **water cut** is the fraction of water in the produced liquid: water / (oil + water).
        Write `water_cut(oil, water)` that returns it, and **raises `ValueError`** if a volume is negative or if
        oil + water is 0 (the well produced nothing: the water cut is undefined).
        ''', '''
        def water_cut(oil, water):
            ...

        water_cut(90.0, 10.0)
        '''),
        *question('q3', '''
        ### Q3. How bad is the file?

        Store in `n_days` the number of days in the file and in `n_bad` the number of **bad days**: oil or water
        cannot be read (`safe_float` gives `None`) **or** is negative.
        ''', '''
        n_days = 0
        n_bad = 0
        ...
        n_days, n_bad
        '''),
        *question('q4', '''
        ### Q4. Debug this function

        A colleague wrote `average_positive(values)`, which should return the mean of the values **greater
        than 0**, or `None` when there are none. It has **several bugs**. Run it, compare with what you expect by hand,
        and fix it. Add `print` lines inside the loop if it helps, then remove them.
        ''', '''
        def average_positive(values):
            for v in values:
                total = 0
                count = 0
                if v >= 0:
                    total += v
                    count += 1
            return total / len(values)

        average_positive([2.0, -1.0, 4.0, 0.0])    # should be 3.0
        '''),
        *question('q5', '''
        ### Q5. Results from the clean days

        Using only the **valid** days (oil and water readable and not negative):

        * `cum_oil_bbl`: the cumulative oil production, in barrels;
        * `worst_day`: the date (as text, e.g. `'2024-03-14'`) with the highest water cut, among valid days with
          oil + water > 0. Your `water_cut` can be used here; the shut-in days would make it raise an error.
        ''', '''
        cum_oil_bbl = 0.0
        worst_day = None
        ...
        cum_oil_bbl, worst_day
        '''),
        *closing('''
        ### Going further (not checked)

        * Write `test_water_cut()` with at least four asserts, including the two error cases, and run it.
        * Why is it better that `water_cut(0, 0)` raises an error than returns 0?
        '''),
    ]
    save_notebook(NB, 'w6', cells)

def build():
    rows = make_data()
    write_tests('w6', TESTS)
    notebook()
    return f'{len(rows)} production days; {NB} written'
