# Builds IUGB MEN 4338 (Geostatistics, lecture and lab) notebooks:
# the synthetic deposits, the notebooks and their Otter-Grader tests.
# This file holds the data generators and the notebook helpers; each week lives in tools/men4338_wN.py
# (a build() function) and is called from here. Re-running it overwrites iugb/men4338/{data,notebooks,tests}/.
# Every dataset is synthetic: drawn from Gaussian random fields with a known variogram, so the
# "true" deposit is known and students can measure how good their estimates are.
import csv, json, pprint, textwrap
from pathlib import Path
import numpy as np

R = Path(__file__).resolve().parents[1] / 'iugb' / 'men4338'
REPO_RAW = 'https://raw.githubusercontent.com/earthai-tech/lab-courses/main/iugb/men4338/'
COURSE = 'MEN 4338'

# ---------------------------------------------------------------- random fields
def spherical_cov(h, a):
    h = np.minimum(np.asarray(h, float) / a, 1.0)
    return 1 - 1.5 * h + 0.5 * h ** 3

def grf(nx, ny, cell, a_major, a_minor, azimuth, seed):
    """Standard Gaussian random field (mean 0, variance 1) with an anisotropic spherical covariance.
    azimuth: direction of the major range, degrees clockwise from north. FFT (circulant embedding) method."""
    rng = np.random.default_rng(seed)
    px, py = 2 * nx, 2 * ny
    ix = np.fft.fftfreq(px) * px * cell
    iy = np.fft.fftfreq(py) * py * cell
    dx, dy = np.meshgrid(ix, iy)
    t = np.radians(azimuth)
    u = dx * np.sin(t) + dy * np.cos(t)        # along the major axis
    w = dx * np.cos(t) - dy * np.sin(t)        # along the minor axis
    h = np.sqrt((u / a_major) ** 2 + (w / a_minor) ** 2)
    c = spherical_cov(h, 1.0)
    spec = np.maximum(np.real(np.fft.fft2(c)), 0)
    noise = rng.standard_normal((py, px))
    z = np.real(np.fft.ifft2(np.sqrt(spec) * np.fft.fft2(noise)))[:ny, :nx]
    return (z - z.mean()) / z.std()

# ---------------------------------------------------------------- datasets
def write_csv(name, rows):
    (R / 'data').mkdir(parents=True, exist_ok=True)
    with open(R / 'data' / name, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def intervals_for_holes(holes, rng, grade_key, bench=10.0, sigma=0.35, missing=0.012, decimals=3):
    """Split each hole's bench into 1, 1.5 or 2 m intervals whose grades scatter around the hole grade.
    Returns interval rows and the length-weighted composite of each hole (unsampled intervals ignored)."""
    rows, comps = [], {}
    for hid, g in holes:
        depth, parts = 0.0, []
        while depth < bench - 1e-9:
            length = min(float(rng.choice([1.0, 1.5, 2.0, 2.0])), bench - depth)
            parts.append((depth, depth + length)); depth += length
        vals = g * rng.lognormal(-sigma ** 2 / 2, sigma, len(parts))
        num = den = 0.0
        for (a, b), v in zip(parts, vals):
            ns = rng.random() < missing
            val = '' if ns else round(float(v), decimals)
            rows.append({'hole_id': hid, 'from_m': f'{a:.1f}', 'to_m': f'{b:.1f}', grade_key: val})
            if not ns:
                num += val * (b - a); den += b - a
        comps[hid] = round(num / den, decimals)
    return rows, comps

def bassam():
    """Bassam gold prospect: 1200 m x 1000 m bench, 10 m truth grid, 50 m RC grid + 25 m infill on the rich zone."""
    nx, ny, cell = 120, 100, 10.0
    z = grf(nx, ny, cell, 420, 120, 45, seed=4338)
    au = np.exp(-0.1 + 0.45 * z)
    xs = (np.arange(nx) + 0.5) * cell
    ys = (np.arange(ny) + 0.5) * cell
    write_csv('bassam_truth_grid.csv', [{'x': f'{xs[i]:.0f}', 'y': f'{ys[j]:.0f}', 'au_gpt': round(float(au[j, i]), 3)}
                                         for j in range(ny) for i in range(nx)])
    rng = np.random.default_rng(43381)
    # where to infill: the richest 250 m x 250 m window
    k = 25
    best, bi, bj = -1, 0, 0
    for j in range(0, ny - k, 5):
        for i in range(0, nx - k, 5):
            m = au[j:j + k, i:i + k].mean()
            if m > best: best, bi, bj = m, i, j
    pts = []
    for gy in np.arange(25, 1000, 50):
        for gx in np.arange(25, 1200, 50):
            pts.append(('grid', gx + rng.uniform(-5, 5), gy + rng.uniform(-5, 5)))
    for gy in np.arange(bj * cell + 12.5, (bj + k) * cell, 25):
        for gx in np.arange(bi * cell + 12.5, (bi + k) * cell, 25):
            ox, oy = (gx - 25) % 50, (gy - 25) % 50
            if min(ox, 50 - ox) < 10 and min(oy, 50 - oy) < 10:
                continue                                  # already a grid hole there
            pts.append(('infill', gx + rng.uniform(-3, 3), gy + rng.uniform(-3, 3)))
    holes, meta = [], []
    for n, (camp, x, y) in enumerate(pts, 1):
        i, j = min(int(x // cell), nx - 1), min(int(y // cell), ny - 1)
        g = au[j, i] * rng.lognormal(-0.12 ** 2 / 2, 0.12)       # small-scale variability (nugget)
        hid = f'BR-{n:03d}'
        holes.append((hid, g)); meta.append((hid, camp, x, y))
    rows, comps = intervals_for_holes(holes, rng, 'au_gpt')
    write_csv('bassam_intervals.csv', rows)
    write_csv('bassam_samples.csv', [{'hole_id': h, 'campaign': c, 'x': f'{x:.1f}', 'y': f'{y:.1f}', 'au_gpt': comps[h]}
                                     for h, c, x, y in meta])
    return len(meta), len(rows)

def copper_south():
    """Week 7 review prospect: copper (%), 800 m x 600 m, isotropic, 60 m grid with an infill line."""
    nx, ny, cell = 80, 60, 10.0
    z = grf(nx, ny, cell, 220, 220, 0, seed=7338)
    cu = np.exp(-0.9 + 0.55 * z)
    rng = np.random.default_rng(73381)
    pts = [(x + rng.uniform(-5, 5), y + rng.uniform(-5, 5)) for y in np.arange(30, 600, 60) for x in np.arange(30, 800, 60)]
    pts += [(x + rng.uniform(-3, 3), 330 + rng.uniform(-3, 3)) for x in np.arange(45, 800, 30)]
    holes, meta = [], []
    for n, (x, y) in enumerate(pts, 1):
        g = cu[min(int(y // cell), ny - 1), min(int(x // cell), nx - 1)] * rng.lognormal(-0.02, 0.2)
        holes.append((f'CS-{n:03d}', g)); meta.append((f'CS-{n:03d}', x, y))
    rows, comps = intervals_for_holes(holes, rng, 'cu_pct', sigma=0.25)
    write_csv('copper_south_intervals.csv', rows)
    write_csv('copper_south_collars.csv', [{'hole_id': h, 'x': f'{x:.1f}', 'y': f'{y:.1f}'} for h, x, y in meta])
    return len(meta)

def porosity_field():
    """Week 11: porosity at 48 wells of a 4 km x 3 km field, with a regional trend (deeper, tighter rock to the north-east)."""
    nx, ny, cell = 80, 60, 50.0
    z = grf(nx, ny, cell, 900, 900, 0, seed=11338)
    rng = np.random.default_rng(113381)
    rows = []
    for n in range(1, 49):
        x, y = rng.uniform(150, 3850), rng.uniform(150, 2850)
        trend = 0.245 - 0.012 * x / 1000 - 0.010 * y / 1000
        phi = trend + 0.012 * z[int(y // cell), int(x // cell)] + rng.normal(0, 0.003)
        rows.append({'well': f'PW-{n:02d}', 'x': f'{x:.0f}', 'y': f'{y:.0f}', 'phi': round(float(phi), 4)})
    write_csv('porosity_wells.csv', rows)
    return len(rows)

def kossou():
    """Final project deposit: gold, 1000 m x 800 m, anisotropy towards N120, 50 m grid + 25 m infill, raw intervals."""
    nx, ny, cell = 100, 80, 10.0
    z = grf(nx, ny, cell, 280, 110, 120, seed=14338)
    au = np.exp(0.05 + 0.5 * z)
    rng = np.random.default_rng(143381)
    pts = [(x + rng.uniform(-6, 6), y + rng.uniform(-6, 6)) for y in np.arange(25, 800, 50) for x in np.arange(25, 1000, 50)]
    k = 20                                   # infill the richest 200 m x 200 m window
    best, cx, cy = -1, 0, 0
    for j in range(0, ny - k, 5):
        for i in range(0, nx - k, 5):
            m = au[j:j + k, i:i + k].mean()
            if m > best: best, cx, cy = m, (i + k / 2) * cell, (j + k / 2) * cell
    pts += [(x + rng.uniform(-3, 3), y + rng.uniform(-3, 3)) for y in np.arange(cy - 87.5, cy + 88, 25)
            for x in np.arange(cx - 87.5, cx + 88, 25) if 0 < x < 1000 and 0 < y < 800]
    holes, meta = [], []
    for n, (x, y) in enumerate(pts, 1):
        g = au[min(int(y // cell), ny - 1), min(int(x // cell), nx - 1)] * rng.lognormal(-0.15 ** 2 / 2, 0.15)
        holes.append((f'KS-{n:03d}', g)); meta.append((f'KS-{n:03d}', x, y))
    rows, comps = intervals_for_holes(holes, rng, 'au_gpt', bench=8.0)
    write_csv('kossou_intervals.csv', rows)
    write_csv('kossou_collars.csv', [{'hole_id': h, 'x': f'{x:.1f}', 'y': f'{y:.1f}'} for h, x, y in meta])
    return len(meta)

def make_data():
    return {'bassam': bassam(), 'copper_south': copper_south(), 'porosity': porosity_field(), 'kossou': kossou()}

# ---------------------------------------------------------------- tests
def test_file(name, cases):
    return "OK_FORMAT = True\n\ntest = " + pprint.pformat({
        "name": name, "points": 1,
        "suites": [{"cases": [{"code": textwrap.dedent(c).strip("\n"), "hidden": False, "locked": False,
                               "failure_message": m} for c, m in cases],
                    "scored": True, "setup": "", "teardown": "", "type": "doctest"}]}, width=100, sort_dicts=False) + "\n"

def write_tests(week, tests):
    d = R / 'tests' / week; d.mkdir(parents=True, exist_ok=True)
    for q, cases in tests.items():
        (d / f'{q}.py').write_text(test_file(q, cases), encoding='utf-8')

# ---------------------------------------------------------------- notebook cells
def md(s): return {"cell_type": "markdown", "metadata": {}, "source": textwrap.dedent(s).strip("\n")}
def code(s): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": textwrap.dedent(s).strip("\n")}

def setup_cell(week, data_files, tests):
    files = [("data/" + d, d) for d in data_files] + [(f"tests/{week}/{q}.py", f"tests/{q}.py") for q in tests]
    return code(f'''
    # Setup: run this cell first (Colab or local Jupyter).
    # It fetches the data and the answer checks: from the repository (../data, ../tests)
    # if you downloaded it, otherwise from GitHub.
    import os, shutil, urllib.request
    URL = '{REPO_RAW}'
    FILES = {files!r}
    os.makedirs('tests', exist_ok=True)
    for source, target in FILES:
        if os.path.exists(target):
            continue
        local = os.path.join('..', source)
        if os.path.exists(local):
            shutil.copy(local, target)                      # offline kit / cloned repo
        else:
            urllib.request.urlretrieve(URL + source, target)  # Colab: download
    print('Ready:', ', '.join(t for _, t in FILES))
    ''')

def otter_cell():
    return code('''
    # Automatic answer checks (Otter-Grader)
    try:
        import otter
    except ImportError:
        %pip install -q otter-grader
        import otter
    grader = otter.Notebook(tests_dir="tests")
    ''')

def header(week, title, nb, intro):
    badge = (f"[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
             f"(https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/{nb})")
    return {"cell_type": "markdown", "metadata": {}, "source": "\n\n".join([
        f"# {COURSE} · Week {week} — {title}", badge,
        "**IUGB · BSc Mining Engineering · Geostatistics (lecture & lab)** · Instructor: Laurent Kouadio",
        textwrap.dedent(intro).strip("\n"),
        "Run each cell with **Shift + Enter**, from top to bottom, starting with the two setup cells."])}

def question(q, text, starter):
    return [md(text), code(starter), code(f'grader.check("{q}")')]

def closing(going_further):
    tail = ("---\n**Before you leave:** run all the checks with the cell below, then save your notebook\n"
            "(**File → Download → .ipynb** in Colab).")
    return [{"cell_type": "markdown", "metadata": {}, "source": textwrap.dedent(going_further).strip("\n") + "\n\n" + tail},
            code('grader.check_all()')]

def save_notebook(name, prefix, cells):
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                        "language_info": {"name": "python"}, "colab": {"provenance": []}},
          "nbformat": 4, "nbformat_minor": 5}
    for i, c in enumerate(nb["cells"]):
        c["id"] = f"{prefix}-{i:02d}"
    (R / 'notebooks').mkdir(parents=True, exist_ok=True)
    (R / 'notebooks' / name).write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding='utf-8')

# ---------------------------------------------------------------- shared toolbox
# Functions written by the students in earlier weeks, given ready-made in later notebooks.
TOOLBOX = {
 'variogram': '''
def exp_variogram(x, y, v, lag, nlags, azimuth=None, atol=22.5):
    """Experimental semivariogram. Lag class k (1..nlags) holds the pairs with |d - k*lag| < lag/2.
    With an azimuth (degrees clockwise from north), only pairs within +/- atol of that direction are kept.
    Returns mean distance, semivariance and number of pairs of each class (NaN where a class is empty)."""
    x, y, v = (np.asarray(a, float) for a in (x, y, v))
    i, j = np.triu_indices(len(v), 1)
    dx, dy = x[j] - x[i], y[j] - y[i]
    d = np.hypot(dx, dy)
    keep = np.ones(len(d), bool)
    if azimuth is not None:
        az = np.degrees(np.arctan2(dx, dy)) % 180
        diff = np.abs(az - azimuth % 180)
        keep = np.minimum(diff, 180 - diff) <= atol
    sq = 0.5 * (v[j] - v[i]) ** 2
    hm, g, n = np.full(nlags, np.nan), np.full(nlags, np.nan), np.zeros(nlags, int)
    for k in range(1, nlags + 1):
        m = keep & (np.abs(d - k * lag) < lag / 2)
        n[k - 1] = m.sum()
        if n[k - 1]:
            hm[k - 1], g[k - 1] = d[m].mean(), sq[m].mean()
    return hm, g, n
''',
 'models': '''
def spherical(h, c0, c, a):
    """Spherical model: nugget c0, partial sill c, range a. gamma(0) = 0."""
    h = np.asarray(h, float)
    r = np.minimum(h / a, 1.0)
    return np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** 3), 0.0)

def aniso_h(dx, dy, azimuth, a_major, a_minor):
    """Distance rescaled to the major range: an anisotropic model becomes model(aniso_h(...), c0, c, a_major)."""
    t = np.radians(azimuth)
    u = dx * np.sin(t) + dy * np.cos(t)
    w = dx * np.cos(t) - dy * np.sin(t)
    return np.sqrt(u ** 2 + (w * a_major / a_minor) ** 2)
''',
 'declus': '''
def cell_weights(x, y, cell_size):
    """Cell declustering weights (sum to 1); cells start at the origin."""
    key = np.floor(np.asarray(x) / cell_size).astype(int) * 100000 + np.floor(np.asarray(y) / cell_size).astype(int)
    _, inv, cnt = np.unique(key, return_inverse=True, return_counts=True)
    w = 1.0 / cnt[inv]
    return w / w.sum()
''',
 'idw': '''
def idw_estimate(x0, y0, x, y, v, power=2, nmax=12):
    """Inverse-distance estimate at (x0, y0) from the nmax closest samples."""
    d = np.hypot(x - x0, y - y0)
    k = np.argsort(d)[:nmax]
    if d[k[0]] < 1e-9:
        return float(v[k[0]])
    w = 1.0 / d[k] ** power
    return float((w * v[k]).sum() / w.sum())
''',
 'kriging': '''
def ok_point(x0, y0, x, y, v, gamma, nmax=16):
    """Ordinary kriging at (x0, y0) with the nmax nearest data.
    gamma(dx, dy) is the variogram model, a function of the separation vector.
    Returns (estimate, kriging variance)."""
    d = np.hypot(x - x0, y - y0)
    idx = np.argsort(d)[:nmax]
    xs, ys, vs = x[idx], y[idx], v[idx]
    n = len(idx)
    A = np.ones((n + 1, n + 1)); A[n, n] = 0
    A[:n, :n] = gamma(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])
    b = np.ones(n + 1); b[:n] = gamma(xs - x0, ys - y0)
    sol = np.linalg.solve(A, b)
    w, mu = sol[:n], sol[n]
    return float(w @ vs), float(w @ b[:n] + mu)
''',
    'block': '''
def discretise(xc, yc, size, n):
    """n x n points at the centres of the sub-cells of a square block of side size centred on (xc, yc)."""
    o = (np.arange(n) + 0.5) / n * size - size / 2
    px, py = np.meshgrid(xc + o, yc + o)
    return px.ravel(), py.ravel()

def gamma_bar(gamma, size, n=5):
    """Average variogram within a square block."""
    px, py = discretise(0, 0, size, n)
    return float(gamma(px[:, None] - px[None, :], py[:, None] - py[None, :]).mean())

def ok_block(xc, yc, size, x, y, v, gamma, nd=4, nmax=16):
    """Ordinary block kriging of a size x size block centred on (xc, yc). Returns (estimate, block kriging variance)."""
    k = np.argsort(np.hypot(x - xc, y - yc))[:nmax]
    xs, ys = x[k], y[k]; m = len(k)
    px, py = discretise(xc, yc, size, nd)
    A = np.ones((m + 1, m + 1)); A[m, m] = 0
    A[:m, :m] = gamma(xs[:, None] - xs[None, :], ys[:, None] - ys[None, :])
    b = np.ones(m + 1); b[:m] = gamma(xs[:, None] - px[None, :], ys[:, None] - py[None, :]).mean(axis=1)
    s = np.linalg.solve(A, b)
    return float(s[:m] @ v[k]), float(s[:m] @ b[:m] + s[m] - gamma_bar(gamma, size, nd))
''',
}

def toolbox_cell(*parts, note='Toolbox from earlier weeks: run this cell.'):
    body = "\n".join(textwrap.dedent(TOOLBOX[p]).strip("\n") + "\n" for p in parts)
    return code(f"# {note}\nimport numpy as np\n\n" + body)

if __name__ == '__main__':
    import importlib.util, sys
    print(make_data())
    sys.modules.setdefault('make_men4338', sys.modules[__name__])
    for extra in sorted(Path(__file__).parent.glob('men4338_w*.py'), key=lambda p: int(p.stem.split('_w')[1])):
        spec = importlib.util.spec_from_file_location(extra.stem, extra)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        print(mod.build())
