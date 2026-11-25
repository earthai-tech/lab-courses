# CSC 2301 week 4: strings and text files, cleaning a messy laboratory report.
# Built by tools/make_csc2301.py, which imports this file and calls build().
import random
from make_csc2301 import R, md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'CSC2301_W4_strings_files_lab_report.ipynb'
DATA = 'lab_report_raw.txt'

def make_data():
    rnd = random.Random(2304)
    lines = ['ASSAY REPORT - BATCH 2024-117 - FIRE ASSAY AU (50 g)',
             'Laboratory: example assay lab     Client: student exploration project',
             'sample ; hole ; from-to (m) ; Au ; remark',
             '-' * 60]
    n = 0
    for h in (2, 3, 5, 7):
        depth = 0.0
        for _ in range(rnd.randint(9, 13)):
            n += 1
            length = rnd.choice([1.0, 1.5, 2.0])
            hole = rnd.choice([f'DH-{h:02d}', f'dh-{h:02d}', f' DH{h:02d}', f'dh {h:02d} ', f'DH-0{h}'])
            g = rnd.lognormvariate(0, 1.0) * 0.9
            r = rnd.random()
            if r < 0.10:
                au = '<0.01'
            elif r < 0.16:
                au = 'n.d.'
            elif r < 0.45:
                au = f'{g:.2f}'.replace('.', ',') + ' g/t'
            else:
                au = f'{g:.2f}'
            remark = rnd.choice(['', '', '', 'duplicate OK', 'RE-ASSAY', 'low recovery'])
            sep = rnd.choice([' ; ', ';', ' ;', '; '])
            lines.append(sep.join([f'S{n:04d}', hole, f'{depth:.1f}-{depth + length:.1f}', au, remark]))
            depth += length
        lines.append('')
    lines += ['-' * 60, 'n.d. = not determined (sample lost). <0.01 = below detection limit.', 'END OF REPORT']
    (R / 'data').mkdir(parents=True, exist_ok=True)
    (R / 'data' / DATA).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return n

REF = '''>>> def _hole(s):
...     d = ''.join(c for c in s if c.isdigit())
...     return 'DH-' + d.zfill(2)
>>> def _grade(s):
...     s = s.strip().lower().replace('g/t', '').strip().replace(',', '.')
...     if s in ('', 'n.d.'):
...         return None
...     if s.startswith('<'):
...         return float(s[1:]) / 2
...     return float(s)
>>> _rows = []
>>> for _l in open('lab_report_raw.txt', encoding='utf-8'):
...     _p = [x.strip() for x in _l.split(';')]
...     if len(_p) == 5 and _p[0].startswith('S0'):
...         _a, _b = _p[2].split('-')
...         _rows.append((_hole(_p[1]), float(_a), float(_b), _grade(_p[3])))
'''
TESTS = {
 "q1": [(">>> [clean_hole_id(s) for s in ('DH-03', 'dh-03', ' DH03', 'dh 03 ')]\n['DH-03', 'DH-03', 'DH-03', 'DH-03']",
         "Keep only the digits, then rebuild the name as 'DH-' + two digits."),
        (">>> clean_hole_id('DH-7')\n'DH-07'", "Pad the number to two digits: str.zfill(2) or f'{int(n):02d}'.")],
 "q2": [(">>> [parse_grade(s) for s in ('1.25', '1,25', ' 0,80 g/t ')]\n[1.25, 1.25, 0.8]",
         "Remove spaces and the unit 'g/t', replace the decimal comma by a point, then convert with float()."),
        (">>> parse_grade('<0.01')\n0.005", "Below detection limit '<0.01' counts as half the limit: 0.005."),
        (">>> [parse_grade(s) for s in ('n.d.', '')]\n[None, None]", "Not determined ('n.d.') or empty: return None, not 0.")],
 "q3": [(REF + ">>> bool(n_samples == len(_rows))\nTrue", "Count only the sample lines: they start with 'S0' and have 5 fields separated by ';'."),
        (REF + ">>> bool(n_missing == sum(1 for r in _rows if r[3] is None))\nTrue", "n_missing counts the samples whose grade is None.")],
 "q4": [(">>> bool(isinstance(samples, list) and isinstance(samples[0], dict))\nTrue", "samples must be a list of dictionaries."),
        (REF + ">>> bool(sorted(samples[0]) == ['au_gpt', 'from_m', 'hole_id', 'to_m'])\nTrue",
         "Each dictionary has exactly the keys hole_id, from_m, to_m, au_gpt."),
        (REF + ">>> bool([(s['hole_id'], s['from_m'], s['to_m'], s['au_gpt']) for s in samples] == _rows)\nTrue",
         "Same samples, in file order, with clean hole ids, depths as floats and grades from parse_grade.")],
 "q5": [(">>> import csv as _c\n>>> _w = list(_c.DictReader(open('lab_report_clean.csv', encoding='utf-8')))\n>>> bool(list(_w[0]) == ['hole_id', 'from_m', 'to_m', 'au_gpt'])\nTrue",
         "Write lab_report_clean.csv with the header hole_id,from_m,to_m,au_gpt."),
        (REF + ">>> import csv as _c\n>>> _w = list(_c.DictReader(open('lab_report_clean.csv', encoding='utf-8')))\n"
               ">>> bool(len(_w) == sum(1 for r in _rows if r[3] is not None))\nTrue",
         "Write only the samples that have a grade (leave out the None ones)."),
        (">>> summary_line('DH-03', 12, 1.2345)\n'DH-03: 12 samples, mean 1.23 g/t'", "Use an f-string with :.2f for the mean.")],
}

def notebook():
    cells = [
        header(4, 'Strings and files: cleaning a lab report', NB, '''
        Data rarely arrive clean. Laboratories send text reports typed by people: hole names written five
        different ways, decimal commas, units glued to numbers, "below detection limit" codes.
        This week you turn such a report into a clean table that a program can trust.

        **What you will practise:** string methods (`strip`, `lower`, `upper`, `replace`, `split`, `startswith`,
        `isdigit`) · slicing · f-strings · reading a text file line by line · writing a CSV file.
        '''),
        setup_cell('w4', [DATA], TESTS),
        otter_cell(),
        md('''
        ## 1. Look at the raw file first

        Always open a data file and **read it with your eyes** before writing code.
        '''),
        code(f'''
        with open("{DATA}", encoding="utf-8") as f:
            text = f.read()
        print(text[:900])
        '''),
        md('''
        What do you notice? The header lines, the separator `;` with or without spaces, hole names such as
        `dh-03`, ` DH03` or `dh 03 `, grades like `1,25 g/t`, `<0.01` or `n.d.`, empty lines and a footer.

        ## 2. Strings are sequences of characters
        '''),
        code('''
        s = "  dh-03 "
        print(repr(s.strip()))          # remove spaces at both ends
        print(s.strip().upper())        # DH-03
        print("1,25".replace(",", "."))  # decimal comma -> point
        print("S0012;DH-03;0.0-1.5;0.42;".split(";"))
        print("DH-03"[3:])              # slicing: from position 3 to the end -> '03'
        print("7".zfill(2), "abc12".isdigit(), "12".isdigit())
        '''),
        md('''
        Strings never change in place: `s.upper()` gives a **new** string, so store it: `s = s.upper()`.

        ## 3. f-strings for clean output
        '''),
        code('''
        hole, n, mean = "DH-05", 11, 0.98765
        print(f"{hole}: {n} samples, mean {mean:.2f} g/t")
        print(f"{'hole':<8}{'mean':>8}")      # align left / right in 8 characters
        print(f"{hole:<8}{mean:>8.3f}")
        '''),
        md('''
        ## 4. Reading a file line by line

        A `for` loop over an open file gives one line at a time, **with** its end-of-line character `\\n`.
        '''),
        code(f'''
        with open("{DATA}", encoding="utf-8") as f:
            for i, line in enumerate(f):
                print(i, repr(line))
                if i == 6:
                    break
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. One name per hole

        Write `clean_hole_id(s)` that turns any spelling of a hole name into the standard form `DH-` followed by
        two digits: `'dh-03'`, `' DH03'`, `'dh 03 '` all become `'DH-03'`, and `'DH-7'` becomes `'DH-07'`.

        *Hint:* keep only the characters that are digits.
        ''', '''
        def clean_hole_id(s):
            ...

        [clean_hole_id(s) for s in ("DH-03", "dh-03", " DH03", "dh 03 ", "DH-7")]
        '''),
        *question('q2', '''
        ### Q2. A grade you can compute with

        Write `parse_grade(s)` that returns the grade as a float in g/t:

        * `'1.25'`, `'1,25'` and `' 0,80 g/t '` → 1.25, 1.25, 0.8
        * `'<0.01'` (below the detection limit) → half the limit, **0.005**, a common convention
        * `'n.d.'` or an empty string → `None` (unknown is not zero!)
        ''', '''
        def parse_grade(s):
            ...

        [parse_grade(s) for s in ("1.25", "1,25", " 0,80 g/t ", "<0.01", "n.d.", "")]
        '''),
        *question('q3', '''
        ### Q3. Count the samples

        Read the file line by line. A **sample line** starts with `S0` and has 5 fields separated by `;`
        (after stripping each field). Store in `n_samples` the number of sample lines and in `n_missing`
        the number whose grade is `None` according to `parse_grade`.
        ''', '''
        n_samples = 0
        n_missing = 0
        ...
        n_samples, n_missing
        '''),
        *question('q4', '''
        ### Q4. Build a clean table

        Build `samples`: a list with one dictionary per sample line, in file order, with the keys
        `hole_id` (clean), `from_m` and `to_m` (floats, from the `from-to` field) and `au_gpt`
        (from `parse_grade`, may be `None`).
        ''', '''
        samples = []
        ...
        samples[:3]
        '''),
        *question('q5', '''
        ### Q5. Write the clean file and a summary line

        1. Write `lab_report_clean.csv` with the header `hole_id,from_m,to_m,au_gpt` and one line per sample
           **that has a grade** (leave out the `None` ones). The `csv.DictWriter` from the course is the easiest way.
        2. Write `summary_line(hole, n, mean)` that returns for example `'DH-03: 12 samples, mean 1.23 g/t'`
           (mean with 2 decimals).
        ''', '''
        import csv
        ...

        def summary_line(hole, n, mean):
            ...

        summary_line("DH-03", 12, 1.2345)
        '''),
        *closing('''
        ### Going further (not checked)

        * Print one `summary_line` per hole, using only the samples with a grade.
        * Some lines have the remark `RE-ASSAY`. Count them and print their sample numbers.
        '''),
    ]
    save_notebook(NB, 'w4', cells)

def build():
    n = make_data()
    write_tests('w4', TESTS)
    notebook()
    return f'{n} lab samples; {NB} written'
