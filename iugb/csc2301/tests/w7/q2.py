OK_FORMAT = True

test = {'name': 'q2',
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
                                '>>> _m = {}\n'
                                '>>> for h, f, t, g in _iv:\n'
                                '...     _m[h] = _m.get(h, 0) + t - f\n'
                                '>>> bool(all(abs(metres_by_hole[h] - _m[h]) < 1e-9 for h in _m) '
                                'and len(metres_by_hole) == len(_m))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Drilled metres count every interval of the file, '
                                           'sampled or not.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
