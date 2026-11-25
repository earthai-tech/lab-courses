# CSC 2301 week 10: data tables with pandas (read, select, new columns, groupby, merge) on drill-hole data.
# Built by tools/make_csc2301.py, which imports this file and calls build().
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'CSC2301_W10_pandas_drillholes.ipynb'
FILES = ['drillholes_assays.csv', 'collars.csv']   # from weeks 1 and 5

READ = (">>> import pandas as _pd\n>>> _a = _pd.read_csv('drillholes_assays.csv')\n"
        ">>> _a['length_m'] = _a['to_m'] - _a['from_m']; _a['au_gpt'] = _a['au_ppb'] / 1000\n")
TESTS = {
 "q1": [(">>> import pandas as _pd\n>>> bool(isinstance(assays, _pd.DataFrame) and isinstance(collars, _pd.DataFrame))\nTrue",
         "Read both files with pd.read_csv."),
        (READ + ">>> bool(n_rows == len(_a) and n_holes == _a['hole_id'].nunique())\nTrue", "n_rows = len(assays); n_holes = number of different hole_id values (.nunique()).")],
 "q2": [(READ + ">>> bool(__import__('numpy').allclose(assays['length_m'], _a['length_m']) and __import__('numpy').allclose(assays['au_gpt'], _a['au_gpt']))\nTrue",
         "New columns: assays['length_m'] = to_m - from_m; assays['au_gpt'] = au_ppb / 1000.")],
 "q3": [(READ + ">>> bool(len(high_grade) == int((_a['au_gpt'] >= 2).sum()) and (high_grade['au_gpt'] >= 2).all())\nTrue",
         "high_grade: the rows with au_gpt >= 2, selected with a mask: assays[assays['au_gpt'] >= 2]."),
        (READ + ">>> bool(abs(granite_mean - _a.loc[_a['lithology'] == 'granite', 'au_gpt'].mean()) < 1e-9)\nTrue",
         "granite_mean: the (simple) mean au_gpt of the granite intervals.")],
 "q4": [(READ + ">>> _a['metal'] = _a['au_gpt'] * _a['length_m']\n>>> _s = _a.groupby('hole_id')[['metal', 'length_m']].sum()\n"
               ">>> _w = _s['metal'] / _s['length_m']\n>>> bool(__import__('numpy').allclose(weighted_by_hole.sort_index().values, _w.sort_index().values))\nTrue",
         "Per hole: sum of (au_gpt × length_m) divided by sum of length_m. groupby('hole_id') then .sum().")],
 "q5": [(READ + ">>> _c = _pd.read_csv('collars.csv')\n>>> _m = _a.merge(_c, on='hole_id')\n"
               ">>> bool(len(summary) == 6 and {'easting_m', 'northing_m', 'mean_gpt'} <= set(summary.columns))\nTrue",
         "summary: one row per hole with hole_id, easting_m, northing_m and mean_gpt (the weighted mean)."),
        (">>> bool(summary['mean_gpt'].is_monotonic_decreasing)\nTrue", "Sort summary from the richest hole to the poorest: sort_values('mean_gpt', ascending=False)."),
        (">>> import os\n>>> bool(os.path.exists('hole_summary.csv'))\nTrue", "Save it with summary.to_csv('hole_summary.csv', index=False).")],
}

def notebook():
    cells = [
        header(10, 'Data tables with pandas', NB, '''
        In weeks 1–7 you read files with the `csv` module and wrote loops to group and summarise. **pandas** does
        the same work on whole tables in a few lines, and is the tool used in industry for tabular data.
        The data are the week 1 assays and the week 5 collars: you will redo, in a few lines, what took a
        whole lab then.

        **What you will practise:** `read_csv` · `head`, `info`, `describe` · selecting columns and rows ·
        new columns · Boolean selection · `groupby` · `merge` · `sort_values` · `to_csv`.
        '''),
        setup_cell('w10', FILES, TESTS),
        otter_cell(),
        md('''
        ## 1. A DataFrame is a table

        Rows are records, columns are variables. Each column is a NumPy array with a name.
        '''),
        code('''
        import pandas as pd

        df = pd.read_csv("drillholes_assays.csv")
        df.head()
        '''),
        code('''
        df.info()
        df.describe()
        '''),
        md('''
        ## 2. Selecting
        '''),
        code('''
        df["au_ppb"].head(3)                 # one column (a Series)
        df[["hole_id", "au_ppb"]].head(3)    # several columns (a DataFrame)
        df[df["lithology"] == "quartz vein"] # rows that meet a condition
        '''),
        code('''
        df.loc[df["au_ppb"] > 5000, ["hole_id", "from_m", "au_ppb"]]   # rows AND columns
        '''),
        md('''
        ## 3. Grouping: split, apply, combine

        `groupby` splits the table by a key, applies a calculation to each group and combines the results.
        '''),
        code('''
        df.groupby("lithology")["au_ppb"].agg(["count", "mean", "max"]).round(0)
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Load the tables

        Read `drillholes_assays.csv` into `assays` and `collars.csv` into `collars`. Store the number of rows of
        `assays` in `n_rows` and the number of different holes in `n_holes`.
        ''', '''
        assays = ...
        collars = ...
        n_rows = ...
        n_holes = ...
        n_rows, n_holes
        '''),
        *question('q2', '''
        ### Q2. New columns

        Add to `assays` the columns `length_m` (to_m − from_m) and `au_gpt` (au_ppb / 1000). No loop.
        ''', '''
        ...
        assays.head()
        '''),
        *question('q3', '''
        ### Q3. Selecting rows

        Store in `high_grade` the intervals with `au_gpt >= 2`, and in `granite_mean` the mean `au_gpt` of the granite
        intervals.
        ''', '''
        high_grade = ...
        granite_mean = ...
        len(high_grade), granite_mean
        '''),
        *question('q4', '''
        ### Q4. Weighted mean per hole with `groupby`

        Store in `weighted_by_hole` a Series: hole_id → length-weighted mean grade in g/t. *Hint:* add a column
        `metal = au_gpt × length_m`, sum `metal` and `length_m` per hole, then divide.
        Compare with your week 1 answer to Q5.
        ''', '''
        weighted_by_hole = ...
        weighted_by_hole.round(3)
        '''),
        *question('q5', '''
        ### Q5. Merge, sort and save

        Build `summary`: one row per hole with the columns `hole_id`, `easting_m`, `northing_m` and `mean_gpt`
        (from `weighted_by_hole`), sorted from the richest hole to the poorest. Save it as `hole_summary.csv`
        without the index.

        *Hint:* `weighted_by_hole.rename("mean_gpt").reset_index()` turns the Series into a table you can
        `merge` with `collars` on `hole_id`.
        ''', '''
        summary = ...
        summary
        '''),
        *closing('''
        ### Going further (not checked)

        * `pd.read_csv` can read the week 4 raw report too: try `sep=";"`, `skiprows`, `decimal=","`. What still has to
          be cleaned by hand?
        * Plot `summary` on a map, the point size proportional to `mean_gpt`: `summary.plot.scatter(...)`.
        '''),
    ]
    save_notebook(NB, 'w10', cells)

def build():
    write_tests('w10', TESTS)
    notebook()
    return f'{NB} written (reuses earlier data)'
