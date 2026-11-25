# CSC 2301 week 9: plotting with matplotlib, a well-log display, a histogram and a collar map.
# Built by tools/make_csc2301.py, which imports this file and calls build().
from make_csc2301 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'CSC2301_W9_matplotlib_logs_maps.ipynb'
FILES = ['well_log_kw2.csv', 'drillholes_assays.csv', 'collars.csv']   # from weeks 8, 1 and 5

TESTS = {
 "q1": [(">>> bool(len(fig_log.axes) == 2)\nTrue", "fig_log needs two panels side by side: plt.subplots(1, 2, sharey=True)."),
        (">>> import numpy as _np\n>>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', skiprows=1)\n"
         ">>> bool(len(ax_gr.lines) >= 1 and _np.allclose(ax_gr.lines[0].get_xdata(), _a[:, 1]) and _np.allclose(ax_gr.lines[0].get_ydata(), _a[:, 0]))\nTrue",
         "In a log display the value is on x and the depth on y: ax_gr.plot(gr, depth)."),
        (">>> bool(len(ax_rhob.lines) >= 1)\nTrue", "Plot rhob against depth in ax_rhob.")],
 "q2": [(">>> bool(ax_gr.yaxis_inverted())\nTrue", "Depth increases downwards: ax_gr.invert_yaxis() (shared y: once is enough)."),
        (">>> bool('API' in ax_gr.get_xlabel() and 'g/cm' in ax_rhob.get_xlabel() and 'epth' in ax_gr.get_ylabel())\nTrue",
         "Label every axis with its unit: GR (API), RHOB (g/cm³), Depth (m)."),
        (">>> bool(fig_log.texts or fig_log._suptitle is not None or ax_gr.get_title() != '')\nTrue", "Give the figure a title, e.g. fig_log.suptitle('Well KW-2').")],
 "q3": [(">>> import csv as _csv, numpy as _np\n>>> _g = [int(r['au_ppb']) / 1000 for r in _csv.DictReader(open('drillholes_assays.csv', encoding='utf-8'))]\n"
         ">>> _c, _e = _np.histogram(_g, bins=_np.arange(0, 10.5, 0.5))\n>>> bool(_np.array_equal(_np.asarray(counts), _c))\nTrue",
         "counts comes from ax_hist.hist(grades, bins=np.arange(0, 10.5, 0.5)): it returns (counts, edges, patches)."),
        (">>> bool('g/t' in ax_hist.get_xlabel() and ax_hist.get_ylabel() != '')\nTrue", "Label the x axis with the unit (g/t) and the y axis (number of intervals).")],
 "q4": [(">>> bool(len(ax_map.collections) >= 1 and len(ax_map.collections[0].get_offsets()) == 6)\nTrue", "Draw the 6 collars with ax_map.scatter(easting, northing)."),
        (">>> bool(len(ax_map.texts) == 6)\nTrue", "Write each hole name next to its point with ax_map.annotate (or ax_map.text)."),
        (">>> bool(ax_map.get_aspect() in (1.0, 'equal'))\nTrue", "A map must not stretch distances: ax_map.set_aspect('equal').")],
 "q5": [(">>> import os\n>>> bool(os.path.exists('well_kw2.png') and os.path.getsize('well_kw2.png') > 20000)\nTrue",
         "Save the log figure: fig_log.savefig('well_kw2.png', dpi=150, bbox_inches='tight').")],
}

def notebook():
    cells = [
        header(9, 'Plotting with matplotlib: logs, histograms and maps', NB, '''
        A good figure shows in one second what a table hides. Engineers draw the same few figures again and again:
        a **log display** (values against depth), a **histogram** (how values are distributed) and a **map**.
        This week you build each one with matplotlib, using the data of weeks 1, 5 and 8.

        **What you will practise:** `plt.subplots` and the figure/axes objects · `plot`, `scatter`, `hist` ·
        axis labels with units, titles, legends · inverting an axis · equal aspect · saving a figure.
        '''),
        setup_cell('w9', FILES, TESTS),
        otter_cell(),
        md('''
        ## 1. Figure and axes

        `fig, ax = plt.subplots()` gives a **figure** (the page) and an **axes** (one plot area). You draw on the axes.
        '''),
        code('''
        import csv
        import numpy as np
        import matplotlib.pyplot as plt

        years = np.arange(0, 10)
        rate = 1200 * 0.85 ** years

        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.plot(years, rate, marker="o", label="oil rate")
        ax.axhline(300, color="grey", linestyle="--", label="economic limit")
        ax.set_xlabel("Time (years)")
        ax.set_ylabel("Rate (bbl/d)")
        ax.set_title("Production decline, 15 % per year")
        ax.legend()
        plt.show()
        '''),
        md('''
        **Rules for engineering figures:** every axis has a label **with its unit**; one message per figure;
        no 3-D effects; colours only when they mean something.

        ## 2. The data
        '''),
        code('''
        table = np.loadtxt("well_log_kw2.csv", delimiter=",", skiprows=1)
        depth, gr, rhob = table[:, 0], table[:, 1], table[:, 2]

        with open("drillholes_assays.csv", encoding="utf-8") as f:
            grades = [int(r["au_ppb"]) / 1000 for r in csv.DictReader(f)]
        with open("collars.csv", encoding="utf-8") as f:
            collars = list(csv.DictReader(f))
        print(len(depth), "log samples;", len(grades), "assays;", len(collars), "collars")
        '''),
        md('''
        ---
        ## Exercises

        Keep the names given (`fig_log`, `ax_gr`…): the checks look at those objects.
        '''),
        *question('q1', '''
        ### Q1. A two-track log display

        Create `fig_log, (ax_gr, ax_rhob) = plt.subplots(1, 2, sharey=True, figsize=(6, 8))`.
        Plot GR against depth in `ax_gr` and RHOB against depth in `ax_rhob` (value on **x**, depth on **y**).
        ''', '''
        fig_log, (ax_gr, ax_rhob) = plt.subplots(1, 2, sharey=True, figsize=(6, 8))
        ...
        plt.show()
        '''),
        *question('q2', '''
        ### Q2. Make it readable

        Depth must increase **downwards**: invert the y axis. Label the axes `GR (API)`, `RHOB (g/cm³)` and
        `Depth (m)`, and add a title with `fig_log.suptitle(...)`. Then display `fig_log` again.
        ''', '''
        ...
        fig_log
        '''),
        *question('q3', '''
        ### Q3. Histogram of the gold grades

        Create `fig_hist, ax_hist = plt.subplots()` and draw a histogram of `grades` with bins every 0.5 g/t
        from 0 to 10: `bins=np.arange(0, 10.5, 0.5)`. Keep what `hist` returns: `counts, edges, patches = ax_hist.hist(...)`.
        Label both axes. What does the shape tell you about gold grades?
        ''', '''
        fig_hist, ax_hist = plt.subplots(figsize=(6, 3.5))
        counts, edges, patches = ...
        plt.show()
        '''),
        *question('q4', '''
        ### Q4. Collar map

        Create `fig_map, ax_map = plt.subplots()`. Draw the 6 collars with **one** `ax_map.scatter(easting, northing)`,
        write each hole name next to its point (`ax_map.annotate(name, (x, y))`), label the axes in metres and
        set an **equal aspect** so that 100 m east looks as long as 100 m north.
        ''', '''
        fig_map, ax_map = plt.subplots(figsize=(6, 5))
        ...
        plt.show()
        '''),
        *question('q5', '''
        ### Q5. Save for the report

        Save the log figure as `well_kw2.png` at 150 dpi with `bbox_inches="tight"`. Download it from the Colab
        file panel to check it.
        ''', '''
        ...
        '''),
        *closing('''
        ### Going further (not checked)

        * Shade the sand intervals in `ax_gr` with `ax_gr.fill_betweenx(depth, gr, 60, where=gr < 60, color="gold")`.
        * Colour the collar points by the mean grade of each hole, with a colour bar (`plt.colorbar`).
        '''),
    ]
    save_notebook(NB, 'w9', cells)

def build():
    write_tests('w9', TESTS)
    notebook()
    return f'{NB} written (reuses earlier data)'
