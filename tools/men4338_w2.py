# MEN 4338 week 2: from assay intervals to composites, and declustering the clustered infill.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'MEN4338_W2_compositing_declustering.ipynb'
DATA = ['bassam_intervals.csv', 'bassam_samples.csv']

RI = (">>> import pandas as _pd, numpy as _np\n>>> _iv = _pd.read_csv('bassam_intervals.csv')\n"
      ">>> _iv['_l'] = _iv['to_m'] - _iv['from_m']\n")
RS = ">>> import pandas as _pd, numpy as _np\n>>> _s = _pd.read_csv('bassam_samples.csv')\n"
DECL = (">>> def _w(x, y, c):\n"
        "...     k = _np.floor(_np.asarray(x) / c).astype(int) * 100000 + _np.floor(_np.asarray(y) / c).astype(int)\n"
        "...     _, inv, cnt = _np.unique(k, return_inverse=True, return_counts=True)\n"
        "...     w = 1.0 / cnt[inv]\n"
        "...     return w / w.sum()\n")
TESTS = {
 "q1": [(RI + ">>> bool(_np.allclose(intervals['length_m'], _iv['_l']))\nTrue", "Add the column intervals['length_m'] = to_m - from_m."),
        (RI + ">>> bool(int(n_missing) == int(_iv['au_gpt'].isna().sum()))\nTrue", "n_missing counts the empty au_gpt cells: intervals['au_gpt'].isna().sum()."),
        (RI + ">>> bool(abs(sampled_m - _iv.loc[_iv['au_gpt'].notna(), '_l'].sum()) < 1e-6)\nTrue",
         "sampled_m is the total length of the intervals that have an assay (not the missing ones).")],
 "q2": [(RI + ">>> _ok = _iv.dropna(subset=['au_gpt'])\n>>> _c = (_ok['au_gpt'] * _ok['_l']).groupby(_ok['hole_id']).sum() / _ok['_l'].groupby(_ok['hole_id']).sum()\n"
         ">>> bool(len(composites) == len(_c) and _np.allclose(composites.sort_index().to_numpy(), _c.sort_index().to_numpy()))\nTrue",
         "composites: one length-weighted grade per hole, ignoring the missing intervals (weights = length_m of the assayed intervals)."),
        (RS + ">>> bool(abs(max_diff - (composites.reindex(_s['hole_id']).to_numpy() - _s['au_gpt'].to_numpy()).__abs__().max()) < 1e-9)\nTrue",
         "max_diff = largest absolute difference between your composites and the au_gpt column of bassam_samples.csv (match them by hole_id)."),
        (">>> bool(max_diff < 0.002)\nTrue", "Your composites should match bassam_samples.csv to the third decimal.")],
 "q3": [(">>> import numpy as _np\n>>> _w = cell_weights(_np.array([10., 20., 30., 160.]), _np.array([10., 15., 20., 40.]), 100)\n"
         ">>> bool(_np.allclose(_w, [1/6, 1/6, 1/6, 1/2]))\nTrue",
         "Three samples share one 100 m cell (1/3 each), one is alone (weight 1); then divide by the sum so the weights add up to 1."),
        (RS + DECL + ">>> bool(_np.allclose(cell_weights(_s['x'].to_numpy(), _s['y'].to_numpy(), 50), _w(_s['x'], _s['y'], 50)))\nTrue",
         "Cells start at x = 0, y = 0: cell index = floor(x / cell_size), floor(y / cell_size).")],
 "q4": [(RS + ">>> bool(abs(naive_mean - _s['au_gpt'].mean()) < 1e-9)\nTrue", "naive_mean is the plain mean of all samples."),
        (RS + DECL + ">>> bool(abs(declus_mean - (_w(_s['x'], _s['y'], 50) * _s['au_gpt']).sum()) < 1e-9)\nTrue",
         "declus_mean = sum(weights * au) with the 50 m cell weights."),
        (">>> bool(declus_mean < naive_mean)\nTrue", "The infill holes sit on rich ground: declustering should lower the mean.")],
 "q5": [(">>> import numpy as _np\n>>> bool(_np.allclose(cell_sizes, _np.arange(25, 201, 25)))\nTrue", "cell_sizes = np.arange(25, 201, 25)."),
        (RS + DECL + ">>> _m = [(_w(_s['x'], _s['y'], c) * _s['au_gpt']).sum() for c in range(25, 201, 25)]\n>>> bool(_np.allclose(declus_means, _m))\nTrue",
         "declus_means[k] is the declustered mean with cell size cell_sizes[k]."),
        (">>> import numpy as _np\n>>> bool(best_cell == cell_sizes[int(_np.argmin(declus_means))])\nTrue",
         "When the clusters are on high grades, choose the cell size giving the lowest declustered mean.")],
}

def notebook():
    cells = [
        header(2, 'Compositing and declustering', NB, '''
        The laboratory does not return one grade per hole: it returns one assay per **interval** of core or RC chips,
        with different lengths, and sometimes no assay at all (lost or unsampled interval). Before any statistics we
        bring the data to a common **support** by compositing. Then we deal with the second trap seen in week 1: the
        infill holes are clustered on the rich zone, so the plain average over-estimates the deposit. **Declustering**
        gives each sample a weight that reflects the area it represents.

        **What you will practise:** `groupby` and length-weighted means · missing values · composite checks ·
        cell declustering · choosing the cell size.
        '''),
        setup_cell('w2', DATA, TESTS),
        otter_cell(),
        md('''
        ## 1. The raw intervals
        '''),
        code('''
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        intervals = pd.read_csv("bassam_intervals.csv")
        samples = pd.read_csv("bassam_samples.csv")
        print(intervals.shape)
        intervals.head(8)
        '''),
        md('''
        Each hole samples the same 10 m bench (`from_m` 0 to `to_m` 10) in intervals of 1, 1.5 or 2 m. An empty
        `au_gpt` cell means *not sampled* (NaN). Never replace it by 0: that would invent barren rock.

        ## 2. Compositing

        A **composite** is the length-weighted mean of the intervals over a fixed length (here the whole bench):

        $$z_c = \\frac{\\sum_i z_i \\, \\ell_i}{\\sum_i \\ell_i}$$

        summed over the **assayed** intervals only. One hole by hand:
        '''),
        code('''
        h = intervals[intervals["hole_id"] == "BR-001"].copy()
        h["length"] = h["to_m"] - h["from_m"]
        print(h)
        print("composite:", (h["au_gpt"] * h["length"]).sum() / h["length"].sum())
        '''),
        md('''
        Why weight by length? A 2 m interval represents twice as much rock as a 1 m interval. A plain average of the
        intervals gives the same importance to both and is biased when lengths and grades are related.

        ## 3. Declustering

        With **cell declustering**, the area is divided into square cells; every cell that contains data gets the
        same total weight, shared equally between its samples. A sample alone in its cell weighs more than a
        sample in a crowded cell:

        $$w_i \\propto \\frac{1}{n_{cell(i)}}, \\qquad \\sum_i w_i = 1$$

        The cell size matters: too small and every sample is alone (no declustering), too large and everything
        falls in one cell. A common choice is the spacing of the regular grid.
        '''),
        code('''
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.scatter(samples["x"], samples["y"], s=8, c=samples["campaign"].eq("infill"), cmap="coolwarm")
        for v in range(0, 1201, 100): ax.axvline(v, lw=0.3, color="grey")
        for v in range(0, 1001, 100): ax.axhline(v, lw=0.3, color="grey")
        ax.set_aspect("equal"); ax.set_title("100 m declustering cells")
        plt.show()
        '''),
        md('''
        ---
        ## Exercises
        '''),
        *question('q1', '''
        ### Q1. Interval lengths and missing assays

        Add a column `length_m` to `intervals`. Store in `n_missing` the number of intervals without an assay and in
        `sampled_m` the total length (m) of the intervals that do have one.
        ''', '''
        intervals["length_m"] = ...
        n_missing = ...
        sampled_m = ...
        n_missing, sampled_m
        '''),
        *question('q2', '''
        ### Q2. Composite every hole

        Build `composites`, a pandas Series indexed by `hole_id` holding the length-weighted composite of each hole
        (ignore the missing intervals). Then check it against `samples`: store in `max_diff` the largest absolute
        difference between your composites and the `au_gpt` column of `bassam_samples.csv`.

        *Hint:* drop the missing rows with `dropna(subset=["au_gpt"])`, compute `au_gpt * length_m`, then
        `groupby("hole_id").sum()`. Use `composites.reindex(samples["hole_id"])` to line them up.
        ''', '''
        ok = ...
        composites = ...
        max_diff = ...
        max_diff
        '''),
        *question('q3', '''
        ### Q3. Cell declustering weights

        Write `cell_weights(x, y, cell_size)` returning a NumPy array of weights, one per sample, that sum to 1.
        Cells start at the origin: the cell of a sample is `(floor(x / cell_size), floor(y / cell_size))`.

        *Hint:* build one key per sample, e.g. `ix * 100000 + iy`, then `np.unique(key, return_inverse=True, return_counts=True)`.
        ''', '''
        def cell_weights(x, y, cell_size):
            ...

        cell_weights(np.array([10., 20., 30., 160.]), np.array([10., 15., 20., 40.]), 100)
        '''),
        *question('q4', '''
        ### Q4. Declustered mean

        Store the plain mean of `samples["au_gpt"]` in `naive_mean` and the declustered mean with 50 m cells
        (the grid spacing) in `declus_mean`. By how much did the clustering bias the mean?
        ''', '''
        naive_mean = ...
        declus_mean = ...
        naive_mean, declus_mean
        '''),
        *question('q5', '''
        ### Q5. Which cell size?

        Compute the declustered mean for `cell_sizes = np.arange(25, 201, 25)` and store the results in a list or
        array `declus_means`. Plot them against the cell size. Since the clusters sit on high grades, keep the cell
        size that gives the **lowest** mean in `best_cell`. (Cells larger than about four times the grid spacing
        start to mix unrelated areas, which is why we stop at 200 m.)
        ''', '''
        cell_sizes = ...
        declus_means = ...
        best_cell = ...

        plt.plot(cell_sizes, declus_means, "o-")
        plt.axhline(naive_mean, ls="--", color="grey")
        plt.xlabel("cell size (m)"); plt.ylabel("declustered mean (g/t)")
        plt.show()
        best_cell
        '''),
        *closing('''
        ### Going further (not checked)

        * Draw the histogram of the grades with and without the 50 m weights (`plt.hist(au, weights=w)`).
        * Polygonal declustering: weight each sample by the area of its nearest-neighbour polygon (approximate it
          by counting, for each sample, the 10 m cells of the bench closest to it).
        '''),
    ]
    save_notebook(NB, 'w2', cells)

def build():
    write_tests('w2', TESTS)
    notebook()
    return f'{NB} written'
