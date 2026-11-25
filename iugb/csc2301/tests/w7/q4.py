OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> _b = best_intercept([{'from_m': 0.0, 'to_m': 1.0, 'au_gpt': "
                                "0.2}, {'from_m': 1.0, 'to_m': 3.0, 'au_gpt': 2.0}, {'from_m': "
                                "3.0, 'to_m': 4.0, 'au_gpt': 1.0}, {'from_m': 4.0, 'to_m': 5.0, "
                                "'au_gpt': 0.1}])\n"
                                '>>> (_b[0], _b[1], round(_b[2], 6))\n'
                                '(1.0, 4.0, 1.666667)',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Join consecutive intervals with grade ≥ 1.0 into a '
                                           'run; return (from_m of the first, to_m of the last, '
                                           'weighted mean).'},
                       {'code': '>>> import csv as _csv\n'
                                '>>> def _g(s):\n'
                                '...     try:\n'
                                '...         v = float(s)\n'
                                '...     except ValueError:\n'
                                '...         return None\n'
                                '...     return v if v >= 0 else None\n'
                                ">>> _all = list(_csv.DictReader(open('campaign_rc_assays.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _iv = [(r['hole_id'], float(r['from_m']), float(r['to_m']), "
                                "_g(r['au_gpt'])) for r in _all]\n"
                                '>>> _ok = [x for x in _iv if x[3] is not None]\n'
                                '>>> _holes = sorted({x[0] for x in _iv})\n'
                                '>>> def _wm(xs):\n'
                                '...     return sum((t - f) * g for h, f, t, g in xs) / sum(t - f '
                                'for h, f, t, g in xs)\n'
                                '>>> def _best(xs, c=1.0):\n'
                                '...     best, run = None, []\n'
                                '...     for x in xs + [None]:\n'
                                '...         if x is not None and x[3] >= c:\n'
                                '...             run.append(x)\n'
                                '...             continue\n'
                                '...         if run:\n'
                                '...             m = sum((t - f) * g for h, f, t, g in run)\n'
                                '...             if best is None or m > best[0]:\n'
                                '...                 best = (m, run[0][1], run[-1][2], _wm(run))\n'
                                '...         run = []\n'
                                '...     return None if best is None else best[1:]\n'
                                '>>> _r = {h: _best([x for x in _ok if x[0] == h]) for h in '
                                '_holes}\n'
                                ">>> _s = {h: best_intercept([x for x in intervals if x['hole_id'] "
                                '== h]) for h in _holes}\n'
                                '>>> bool(all((_r[h] is None and _s[h] is None) or (_s[h] is not '
                                'None and all(abs(a - b) < 1e-6 for a, b in zip(_r[h], _s[h]))) '
                                'for h in _holes))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'When a hole has several runs, keep the one with the '
                                           'most metal: the largest sum of grade × length. No run: '
                                           'return None.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
