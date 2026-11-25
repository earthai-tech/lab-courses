OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> round(weighted_mean([{'from_m': 0.0, 'to_m': 2.0, 'au_gpt': "
                                "1.0}, {'from_m': 2.0, 'to_m': 3.0, 'au_gpt': 4.0}]), 6)\n"
                                '2.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Length-weighted: (2 × 1 + 1 × 4) / 3 = 2.'},
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
                                '>>> bool(all(abs(hole_grades[h] - _wm([x for x in _ok if x[0] == '
                                'h])) < 1e-6 for h in _holes))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'hole_grades: hole_id -> weighted mean grade of that '
                                           "hole's valid intervals."}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
