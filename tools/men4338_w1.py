# MEN 4338 week 1: regionalised variables and exploratory data analysis of the Bassam gold samples.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing

NB = 'MEN4338_W1_eda_bassam_gold.ipynb'
DATA = ['bassam_samples.csv']

READ = ">>> import pandas as _pd, numpy as _np\n>>> _s = _pd.read_csv('bassam_samples.csv')\n>>> _a = _s['au_gpt'].to_numpy()\n"
TESTS = {
 "q1": [(READ + ">>> bool(n_samples == len(_s))\nTrue", "n_samples is the number of rows (holes) in the file: len(df)."),
        (READ + ">>> bool(abs(mean_au - _a.mean()) < 1e-9 and abs(median_au - _np.median(_a)) < 1e-9)\nTrue",
         "mean_au = df['au_gpt'].mean(), median_au = df['au_gpt'].median()."),
        (">>> bool(mean_au > median_au)\nTrue", "For a positively skewed variable the mean is above the median: check your two values.")],
 "q2": [(READ + ">>> bool(abs(var_au - _a.var(ddof=1)) < 1e-9 and abs(std_au - _a.std(ddof=1)) < 1e-9)\nTrue",
         "Use the sample variance and standard deviation (pandas .var() and .std(), i.e. ddof=1)."),
        (">>> bool(abs(cv_au - std_au / mean_au) < 1e-12)\nTrue", "cv_au = std_au / mean_au (no unit, not a percentage).")],
 "q3": [(READ + ">>> _q = _np.percentile(_a, [10, 25, 50, 75, 90])\n>>> bool(_np.allclose(quantiles, _q))\nTrue",
         "quantiles = np.percentile(au, [10, 25, 50, 75, 90])."),
        (READ + ">>> bool(abs(iqr_au - (_np.percentile(_a, 75) - _np.percentile(_a, 25))) < 1e-9)\nTrue",
         "iqr_au is the 75th percentile minus the 25th percentile."),
        (READ + ">>> _l = _np.log(_a)\n>>> bool(abs(log_mean - _l.mean()) < 1e-9 and abs(log_var - _l.var(ddof=1)) < 1e-9)\nTrue",
         "log_mean and log_var are the mean and the sample variance (ddof=1) of np.log(au)."),
        (">>> import numpy as _np\n>>> bool(abs(lognormal_mean - _np.exp(log_mean + log_var / 2)) < 1e-12)\nTrue",
         "Lognormal mean: exp(log_mean + log_var / 2).")],
 "q4": [(READ + ">>> bool(abs(cap_value - _np.percentile(_a, 99)) < 1e-9)\nTrue", "cap_value = np.percentile(au, 99)."),
        (READ + ">>> bool(_np.allclose(au_capped, _np.minimum(_a, _np.percentile(_a, 99))))\nTrue",
         "au_capped keeps every value but replaces those above cap_value by cap_value: np.minimum(au, cap_value)."),
        (READ + ">>> _c = _np.minimum(_a, _np.percentile(_a, 99))\n>>> bool(abs(metal_removed - (1 - _c.sum() / _a.sum())) < 1e-9)\nTrue",
         "metal_removed = 1 - sum(capped) / sum(original): a fraction, not a percentage."),
        (READ + ">>> bool(n_capped == int((_a > _np.percentile(_a, 99)).sum()))\nTrue", "n_capped counts the values strictly above cap_value.")],
 "q5": [(READ + ">>> bool(abs(prop_above_1 - (_a > 1.0).mean()) < 1e-12)\nTrue",
         "prop_above_1 is the share of samples with au_gpt > 1.0: (au > 1.0).mean()."),
        (">>> bool(len(ax_map.collections) >= 1 and ax_map.get_aspect() in (1.0, 'equal'))\nTrue",
         "Draw the samples with ax_map.scatter(x, y, c=au, ...) and use ax_map.set_aspect('equal')."),
        (">>> bool('m' in ax_map.get_xlabel() and 'm' in ax_map.get_ylabel())\nTrue", "Label both axes with their unit, e.g. 'East (m)' and 'North (m)'.")],
}

def notebook():
    cells = [
        header(1, 'Regionalised variables and exploratory data analysis', NB, '''
        Geostatistics answers one question: **what is the grade where we have not drilled?** Before estimating
        anything, an engineer looks hard at the data: how many samples, how they are spread in space, how the
        grades are distributed, and whether a few very rich samples dominate the picture.

        This semester we follow one deposit, the **Bassam gold prospect** (synthetic but realistic): a 10 m mining
        bench, 1200 m × 1000 m, drilled with reverse-circulation (RC) holes on a 50 m grid, plus an infill
        campaign at 25 m on the richest zone. Because the data are simulated, we also know the true grades
        everywhere: later we will measure how good each estimation method really is.

        **What you will practise:** loading data with pandas · location map · histogram and log-histogram ·
        mean, median, variance, coefficient of variation · quantiles · the lognormal model · top-cutting (capping).
        '''),
        setup_cell('w1', DATA, TESTS),
        otter_cell(),
        md('''
        ## 1. A regionalised variable

        A grade $z(\\mathbf{x})$ depends on the location $\\mathbf{x} = (x, y)$: it is a **regionalised variable**.
        Two samples close together tend to be similar, samples far apart are not. Classical statistics ignores
        location; geostatistics uses it. First, the data.
        '''),
        code('''
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv("bassam_samples.csv")
        print(df.shape)
        df.head()
        '''),
        md('''
        Each row is one RC hole: its 10 m bench **composite** grade `au_gpt` (g/t gold), the coordinates of the hole
        in the mine grid (`x` east, `y` north, metres) and the `campaign` it belongs to (`grid` or `infill`).
        '''),
        code('''
        df.describe()
        '''),
        code('''
        df["campaign"].value_counts()
        '''),
        md('''
        ## 2. Where are the data?

        Always start with a **location map**. Clusters of samples are a warning: if the infill holes were drilled
        because the grades were good, they over-represent the rich zone.
        '''),
        code('''
        fig, ax = plt.subplots(figsize=(7, 6))
        for camp, marker in [("grid", "o"), ("infill", "^")]:
            d = df[df["campaign"] == camp]
            ax.scatter(d["x"], d["y"], s=14, marker=marker, label=camp)
        ax.set_aspect("equal")
        ax.set_xlabel("East (m)"); ax.set_ylabel("North (m)")
        ax.legend(); ax.set_title("Bassam RC holes")
        plt.show()
        '''),
        md('''
        ## 3. The distribution of grades

        Gold grades are **positively skewed**: many low values, a few very high ones. The histogram of the
        logarithm is often close to a bell curve: the grades are then said to be **lognormal**.
        '''),
        code('''
        au = df["au_gpt"].to_numpy()
        fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
        axes[0].hist(au, bins=40); axes[0].set_xlabel("Au (g/t)"); axes[0].set_title("Grades")
        axes[1].hist(np.log(au), bins=40); axes[1].set_xlabel("ln Au"); axes[1].set_title("Log of grades")
        plt.tight_layout(); plt.show()
        print("skewness:", round(df["au_gpt"].skew(), 2))
        '''),
        md('''
        Summary statistics you will use all semester:

        | statistic | formula | meaning |
        |---|---|---|
        | mean | $\\bar z = \\frac{1}{n}\\sum z_i$ | central value, sensitive to high grades |
        | median | 50th percentile | central value, robust |
        | variance | $s^2 = \\frac{1}{n-1}\\sum (z_i - \\bar z)^2$ | spread (g/t)² |
        | coefficient of variation | $CV = s / \\bar z$ | relative spread; CV > 1 means very erratic grades |

        A **probability plot** shows the same thing: lognormal data fall on a straight line when the grade axis is logarithmic.
        '''),
        code('''
        from scipy import stats
        fig, ax = plt.subplots(figsize=(5, 4))
        stats.probplot(np.log(au), dist="norm", plot=ax)
        ax.set_title("Normal probability plot of ln Au")
        plt.show()
        '''),
        md('''
        ---
        ## Exercises

        Use `df` and `au` from above. Run `grader.check("q…")` under each answer.
        '''),
        *question('q1', '''
        ### Q1. First numbers

        Store the number of samples in `n_samples`, the mean grade in `mean_au` and the median grade in `median_au`.
        Which one is larger, and why?
        ''', '''
        n_samples = ...
        mean_au = ...
        median_au = ...
        n_samples, mean_au, median_au
        '''),
        *question('q2', '''
        ### Q2. Spread

        Compute the sample variance `var_au`, the standard deviation `std_au` and the coefficient of variation
        `cv_au` of the grades.
        ''', '''
        var_au = ...
        std_au = ...
        cv_au = ...
        var_au, std_au, cv_au
        '''),
        *question('q3', '''
        ### Q3. Quantiles and the lognormal model

        * `quantiles`: the 10th, 25th, 50th, 75th and 90th percentiles of the grades (one call to `np.percentile`).
        * `iqr_au`: the inter-quartile range (75th − 25th percentile).
        * `log_mean`, `log_var`: mean and sample variance of $\\ln z$.
        * `lognormal_mean`: the mean predicted by the lognormal model, $e^{\\mu + \\sigma^2/2}$ with
          $\\mu$ = `log_mean` and $\\sigma^2$ = `log_var`. Compare it with `mean_au`.
        ''', '''
        quantiles = ...
        iqr_au = ...
        log_mean = ...
        log_var = ...
        lognormal_mean = ...
        quantiles, iqr_au, lognormal_mean, mean_au
        '''),
        *question('q4', '''
        ### Q4. Capping the outliers

        A few extreme assays can inflate the estimated metal. A common practice is to **cap** (top-cut) grades at a
        high percentile. Cap at the 99th percentile:

        * `cap_value`: the 99th percentile of the grades,
        * `au_capped`: the grades with every value above `cap_value` replaced by `cap_value`,
        * `n_capped`: how many samples were capped,
        * `metal_removed`: the fraction of the total metal removed, $1 - \\sum z^{cap} / \\sum z$.
        ''', '''
        cap_value = ...
        au_capped = ...
        n_capped = ...
        metal_removed = ...
        cap_value, n_capped, metal_removed
        '''),
        *question('q5', '''
        ### Q5. Where is the gold?

        Store in `prop_above_1` the share of samples above 1 g/t. Then make a map of the samples coloured by grade
        in `fig_map, ax_map`: `ax_map.scatter(x, y, c=au, cmap="viridis")`, a colour bar, equal aspect, and both axes
        labelled with their unit. Where is the rich zone? Does it match the infill holes?
        ''', '''
        prop_above_1 = ...

        fig_map, ax_map = plt.subplots(figsize=(7, 6))
        ...
        plt.show()
        prop_above_1
        '''),
        *closing('''
        ### Going further (not checked)

        * Compare the mean grade of the `grid` holes with that of the `infill` holes. Which one better represents the whole bench?
        * Plot the histogram with `bins=np.logspace(-1, 1, 40)` and `ax.set_xscale("log")`.
        '''),
    ]
    save_notebook(NB, 'w1', cells)

def build():
    write_tests('w1', TESTS)
    notebook()
    return f'{NB} written'
