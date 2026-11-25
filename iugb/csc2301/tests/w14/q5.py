OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _L = _pd.read_csv('well_log_kw3.csv').replace(-999.25, "
                                '_np.nan)\n'
                                ">>> _L['vsh'] = ((_L['gr_api'] - 20) / (140 - 20)).clip(0, 1)\n"
                                ">>> _L['phi'] = ((2.65 - _L['rhob_g_cc']) / (2.65 - 1.0)).clip(0, "
                                '0.40)\n'
                                ">>> _L['pay'] = (_L['vsh'] < 0.35) & (_L['phi'] >= 0.12) & "
                                "(_L['rt_ohmm'] >= 15)\n"
                                '>>> def _zones(d, p, min_m=1.0):\n'
                                '...     out, top, last = [], None, None\n'
                                '...     for x, q in list(zip(d, p)) + [(None, False)]:\n'
                                '...         if q and top is None:\n'
                                '...             top = x\n'
                                '...         if not q and top is not None:\n'
                                '...             if last + 0.5 - top >= min_m:\n'
                                '...                 out.append((top, last + 0.5))\n'
                                '...             top = None\n'
                                '...         last = x\n'
                                '...     return out\n'
                                ">>> _Z = _zones(list(_L['depth_m']), list(_L['pay']))\n"
                                '>>> _net = sum(b - t for t, b in _Z)\n'
                                ">>> _phi_pay = _L.loc[_L['pay'], 'phi'].mean()\n"
                                '>>> _r = _np.random.default_rng(999); _n = 400_000\n'
                                '>>> _S = _r.triangular(2, 4, 7, _n) * 1e6 * _net * '
                                '_np.clip(_r.normal(_phi_pay, 0.02, _n), 0.05, 0.35) * (1 - '
                                '_r.uniform(0.25, 0.45, _n)) / 1.2 * 6.2898 / 1e6\n'
                                '>>> _P = _np.percentile(_S, [10, 50, 90])\n'
                                '>>> bool(len(stoiip) == 100_000 and p90 < p50 < p10 and all(abs(a '
                                '/ b - 1) < 0.02 for a, b in zip((p90, p50, p10), _P)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': '100 000 draws: area triangular(2, 4, 7) km², h = '
                                           'net_pay_m, phi normal(phi_pay, 0.02) clipped '
                                           '0.05–0.35, Sw uniform(0.25, 0.45), Bo 1.2. P90 is the '
                                           '10th percentile.'},
                       {'code': '>>> import numpy as _np, pandas as _pd\n'
                                ">>> _L = _pd.read_csv('well_log_kw3.csv').replace(-999.25, "
                                '_np.nan)\n'
                                ">>> _L['vsh'] = ((_L['gr_api'] - 20) / (140 - 20)).clip(0, 1)\n"
                                ">>> _L['phi'] = ((2.65 - _L['rhob_g_cc']) / (2.65 - 1.0)).clip(0, "
                                '0.40)\n'
                                ">>> _L['pay'] = (_L['vsh'] < 0.35) & (_L['phi'] >= 0.12) & "
                                "(_L['rt_ohmm'] >= 15)\n"
                                '>>> def _zones(d, p, min_m=1.0):\n'
                                '...     out, top, last = [], None, None\n'
                                '...     for x, q in list(zip(d, p)) + [(None, False)]:\n'
                                '...         if q and top is None:\n'
                                '...             top = x\n'
                                '...         if not q and top is not None:\n'
                                '...             if last + 0.5 - top >= min_m:\n'
                                '...                 out.append((top, last + 0.5))\n'
                                '...             top = None\n'
                                '...         last = x\n'
                                '...     return out\n'
                                ">>> _Z = _zones(list(_L['depth_m']), list(_L['pay']))\n"
                                '>>> _net = sum(b - t for t, b in _Z)\n'
                                ">>> _phi_pay = _L.loc[_L['pay'], 'phi'].mean()\n"
                                ">>> _want = f'KW-3: {len(zones)} pay zones, net pay "
                                '{net_pay_m:.1f} m, mean porosity {phi_pay:.3f}, STOIIP P90 '
                                "{p90:.1f} / P50 {p50:.1f} / P10 {p10:.1f} MMbbl'\n"
                                ">>> bool(open('kw3_summary.txt', encoding='utf-8').read().strip() "
                                '== _want)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'kw3_summary.txt: one line, exactly in the format '
                                           'shown, built from your own variables.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
