OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv\n'
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
                                '>>> bool(n_valid == len(_ok))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Keep the intervals whose grade is a number ≥ 0: 'NS' "
                                           'and the error code -9.99 are not grades.'},
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
                                ">>> bool([(x['hole_id'], x['from_m'], x['to_m'], x['au_gpt']) for "
                                'x in intervals] == _ok)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'intervals: list of dicts (hole_id, from_m, to_m, '
                                           'au_gpt) with floats, valid grades only, in file '
                                           'order.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
