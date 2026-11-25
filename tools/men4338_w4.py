# MEN 4338 week 4: directional variograms, variogram map and geometric anisotropy.
from make_men4338 import md, code, setup_cell, save_notebook, write_tests, otter_cell, header, question, closing, toolbox_cell

NB = 'MEN4338_W4_anisotropy_directional_variograms.ipynb'
DATA = ['bassam_samples.csv']

RS = (">>> import pandas as _pd, numpy as _np\n>>> _s = _pd.read_csv('bassam_samples.csv')\n"
      ">>> _g = _s[_s['campaign'] == 'grid']\n>>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', 'au_gpt'))\n")
REF = (">>> def _dv(x, y, v, lag, nlags, az, atol):\n"
       "...     i, j = _np.triu_indices(len(v), 1)\n"
       "...     dx, dy = x[j] - x[i], y[j] - y[i]; d = _np.hypot(dx, dy)\n"
       "...     a = _np.degrees(_np.arctan2(dx, dy)) % 180; df = _np.abs(a - az % 180)\n"
       "...     keep = _np.minimum(df, 180 - df) <= atol; sq = 0.5 * (v[j] - v[i]) ** 2\n"
       "...     g = []\n"
       "...     for k in range(1, nlags + 1):\n"
       "...         m = keep & (_np.abs(d - k * lag) < lag / 2)\n"
       "...         g.append(sq[m].mean() if m.any() else _np.nan)\n"
       "...     return _np.array(g)\n")
TESTS = {
 "q1": [(">>> import numpy as _np\n>>> bool(_np.allclose(azimuth_of(_np.array([0., 1, 1, -1, 0, -1]), _np.array([1., 1, 0, 1, -1, -1])), [0, 45, 90, 135, 0, 45]))\nTrue",
         "Azimuth = degrees clockwise from north of the vector (dx, dy): np.degrees(np.arctan2(dx, dy)), folded into [0, 180) with % 180."),
        (">>> bool(abs(float(azimuth_of(-1.0, 0.0)) - 90) < 1e-9)\nTrue", "A pair is the same in both directions: west (270°) folds back to 90°.")],
 "q2": [(RS + REF + ">>> bool(_np.allclose(dir_variogram(_x, _y, _v, 50, 10, 60, 22.5)[1], _dv(_x, _y, _v, 50, 10, 60, 22.5), equal_nan=True))\nTrue",
         "dir_variogram must keep only the pairs whose azimuth is within atol of the direction (remember 175° and 5° are only 10° apart)."),
        (RS + REF + ">>> bool(_np.allclose(dir_variogram(_x, _y, _v, 50, 10, 170, 15)[1], _dv(_x, _y, _v, 50, 10, 170, 15), equal_nan=True))\nTrue",
         "Check the angular difference near 0/180°: use min(diff, 180 - diff)."),
        (RS + ">>> _o = dir_variogram(_x, _y, _v, 50, 10, 0, 90)\n>>> _i, _j = _np.triu_indices(len(_v), 1); _d = _np.hypot(_x[_j] - _x[_i], _y[_j] - _y[_i])\n"
         ">>> bool(int(_o[2][0]) == int((_np.abs(_d - 50) < 25).sum()))\nTrue", "With atol = 90 every pair is kept: the result must equal the omnidirectional variogram.")],
 "q3": [(RS + REF + ">>> bool(sorted(dir_gammas) == [0, 45, 90, 135] and all(_np.allclose(dir_gammas[a], _dv(_x, _y, _v, 50, 10, a, 22.5), equal_nan=True) for a in (0, 45, 90, 135)))\nTrue",
         "dir_gammas maps each azimuth (0, 45, 90, 135) to its semivariance array: lag 50 m, 10 lags, tolerance 22.5°.")],
 "q4": [(">>> import numpy as _np\n>>> _m = {a: _np.nanmean(dir_gammas[a][:4]) for a in dir_gammas}\n>>> bool(major_az == min(_m, key=_m.get))\nTrue",
         "major_az: the direction whose variogram rises the slowest, i.e. the smallest mean semivariance over the first 4 lags."),
        (">>> bool(minor_az == (major_az + 90) % 180)\nTrue", "minor_az is perpendicular to major_az (add 90°, modulo 180)."),
        (">>> import numpy as _np\n>>> _m = {a: _np.nanmean(dir_gammas[a][:4]) for a in dir_gammas}\n>>> bool(abs(continuity_ratio - _m[minor_az] / _m[major_az]) < 1e-9)\nTrue",
         "continuity_ratio = mean of the first 4 lags in the minor direction / same in the major direction.")],
 "q5": [(RS + ">>> _i, _j = _np.triu_indices(len(_v), 1)\n>>> _dx = _np.concatenate([_x[_j] - _x[_i], _x[_i] - _x[_j]]); _dy = _np.concatenate([_y[_j] - _y[_i], _y[_i] - _y[_j]])\n"
         ">>> _sq = _np.tile(0.5 * (_v[_j] - _v[_i]) ** 2, 2)\n>>> _ix = _np.floor((_dx + 300) / 50).astype(int); _iy = _np.floor((_dy + 300) / 50).astype(int)\n"
         ">>> _k = (_ix >= 0) & (_ix < 12) & (_iy >= 0) & (_iy < 12)\n>>> _s1 = _np.zeros((12, 12)); _n1 = _np.zeros((12, 12))\n"
         ">>> _np.add.at(_s1, (_iy[_k], _ix[_k]), _sq[_k]); _np.add.at(_n1, (_iy[_k], _ix[_k]), 1)\n"
         ">>> _vm = _np.where(_n1 > 0, _s1 / _np.maximum(_n1, 1), _np.nan)\n>>> bool(vmap.shape == (12, 12) and _np.allclose(vmap, _vm, equal_nan=True))\nTrue",
         "vmap[row, col]: mean of 0.5*(z_i - z_j)^2 for the separation vectors (both signs) falling in cell row = floor((dy+300)/50), col = floor((dx+300)/50); NaN where empty."),
        (">>> bool(len(ax_vm.images) >= 1)\nTrue", "Draw vmap with ax_vm.imshow(..., origin='lower', extent=[-300, 300, -300, 300]).")],
}

def notebook():
    cells = [
        header(4, 'Directional variograms and anisotropy', NB, '''
        Gold in a shear zone, sand in a channel, a weathering front: geology is rarely the same in every direction.
        If grades stay similar over longer distances along one direction, the variogram rises more slowly in that
        direction: this is **anisotropy**. Missing it leads to estimates smeared across the structure.

        **What you will practise:** azimuths and the angular tolerance · directional variograms · the variogram map ·
        major and minor directions · the anisotropy ratio.
        '''),
        setup_cell('w4', DATA, TESTS),
        otter_cell(),
        toolbox_cell('variogram'),
        md('''
        The toolbox cell above contains a complete `exp_variogram` (your week 3 function, extended with a direction).
        This week you build the directional part yourself.

        ## 1. Azimuths

        In mining, directions are **azimuths**: degrees clockwise from north. For a pair separated by
        $(\\Delta x, \\Delta y)$ the azimuth is `np.degrees(np.arctan2(dx, dy))`. Note the order: `dx` first,
        because we measure from north (the $y$ axis), not from east. A pair has no "front": 30° and 210° are the same
        direction, so azimuths are folded into $[0, 180)$.
        '''),
        code('''
        import pandas as pd
        import matplotlib.pyplot as plt

        samples = pd.read_csv("bassam_samples.csv")
        grid = samples[samples["campaign"] == "grid"]
        x, y, au = grid["x"].to_numpy(), grid["y"].to_numpy(), grid["au_gpt"].to_numpy()
        print(np.degrees(np.arctan2(1, 1)), np.degrees(np.arctan2(1, -1)) % 180)   # NE = 45, SE = 135
        '''),
        md('''
        ## 2. Directional variograms

        A directional variogram keeps only the pairs whose azimuth is within an **angular tolerance** (typically
        ±22.5°) of the chosen direction. Too narrow and there are too few pairs; too wide and the directions mix.
        '''),
        code('''
        fig, ax = plt.subplots(figsize=(7, 4))
        h, g, n = exp_variogram(x, y, au, 50, 10)
        ax.plot(h, g, "k.-", label="omnidirectional")
        for az in [0, 90]:
            h, g, n = exp_variogram(x, y, au, 50, 10, azimuth=az, atol=22.5)
            ax.plot(h, g, "o-", label=f"N{az:03d}")
        ax.axhline(au.var(ddof=1), ls="--", color="grey")
        ax.set_xlabel("h (m)"); ax.set_ylabel("γ(h)"); ax.legend(); plt.show()
        '''),
        md('''
        North–south and east–west look alike here. That does not mean there is no anisotropy: the structure
        may be oblique. We need to test more directions, or look at all of them at once with a **variogram map**.

        ## 3. Geometric anisotropy

        When the sill is the same in every direction but the range changes, the anisotropy is **geometric**. It is
        described by the azimuth of the **major** direction (longest range), the major range $a_{max}$ and the minor
        range $a_{min}$ (perpendicular). The ratio $a_{min}/a_{max}$ is the anisotropy ratio. Plotted around a circle,
        the ranges draw an **ellipse**.

        ---
        ## Exercises (grid holes: `x`, `y`, `au`)
        '''),
        *question('q1', '''
        ### Q1. Azimuth of a pair

        Write `azimuth_of(dx, dy)` returning the azimuth in degrees in $[0, 180)$. It must work on numbers and arrays.
        ''', '''
        def azimuth_of(dx, dy):
            ...

        azimuth_of(np.array([0., 1, 1, -1]), np.array([1., 1, 0, 1]))   # expect 0, 45, 90, 135
        '''),
        *question('q2', '''
        ### Q2. Your directional variogram

        Write `dir_variogram(x, y, v, lag, nlags, azimuth, atol)` returning `(h, gamma, npairs)` like `exp_variogram`,
        but keeping only the pairs whose azimuth is within `atol` degrees of `azimuth`.
        Careful near north: a pair at 178° is only 2° from 0°.
        ''', '''
        def dir_variogram(x, y, v, lag, nlags, azimuth, atol):
            ...

        dir_variogram(x, y, au, 50, 10, 60, 22.5)[1]
        '''),
        *question('q3', '''
        ### Q3. Four directions

        Build the dictionary `dir_gammas` mapping the azimuths 0, 45, 90 and 135 to their semivariance arrays (lag
        50 m, 10 lags, tolerance 22.5°). Plot the four variograms on one figure.
        ''', '''
        dir_gammas = {}
        ...

        fig, ax = plt.subplots(figsize=(7, 4))
        for az, g in dir_gammas.items():
            ax.plot(np.arange(1, 11) * 50, g, "o-", label=f"N{az:03d}")
        ax.legend(); ax.set_xlabel("h (m)"); plt.show()
        '''),
        *question('q4', '''
        ### Q4. Major and minor directions

        The major direction is the one whose variogram rises the slowest. Use the mean of the first 4 lags of each
        direction: store the azimuth with the smallest mean in `major_az`, the perpendicular direction in `minor_az`,
        and `continuity_ratio` = (mean of the first 4 lags along `minor_az`) / (same along `major_az`).
        Does `major_az` agree with the elongation of the rich zone on the week 1 map?
        ''', '''
        major_az = ...
        minor_az = ...
        continuity_ratio = ...
        major_az, minor_az, continuity_ratio
        '''),
        *question('q5', '''
        ### Q5. The variogram map

        Compute the variogram map on a 12 × 12 grid of 50 m cells covering separations from −300 to +300 m in
        $\\Delta x$ and $\\Delta y$. Use **both** orientations of each pair, $(\\Delta x, \\Delta y)$ and
        $(-\\Delta x, -\\Delta y)$. Cell `[row, col]` with `row = floor((dy + 300) / 50)`, `col = floor((dx + 300) / 50)`
        holds the mean of $\\frac12(z_i - z_j)^2$ of its pairs (NaN if empty). Store it in `vmap` and draw it in
        `fig_vm, ax_vm` with `imshow(vmap, origin="lower", extent=[-300, 300, -300, 300])`.
        The low values (dark) draw an ellipse elongated along the major direction.

        *Hint:* `np.add.at(sums, (rows, cols), values)` adds values into a 2D array cell by cell.
        ''', '''
        vmap = ...

        fig_vm, ax_vm = plt.subplots(figsize=(5.5, 5))
        ...
        plt.show()
        '''),
        *closing('''
        ### Going further (not checked)

        * Repeat Q3 with 8 directions (every 22.5°) and an angular tolerance of 11.25°. Is the major direction
          sharper?
        * For the major and minor directions, read the distance where each variogram reaches the sill: what is
          the anisotropy ratio $a_{min}/a_{max}$?
        '''),
    ]
    save_notebook(NB, 'w4', cells)

def build():
    write_tests('w4', TESTS)
    notebook()
    return f'{NB} written'
