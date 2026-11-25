OK_FORMAT = True

test = {'name': 'q5',
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
                                '>>> def _line(h):\n'
                                '...     b = _best([x for x in _ok if x[0] == h])\n'
                                "...     tail = 'best none' if b is None else f'best "
                                "{b[0]:.1f}-{b[1]:.1f} m at {b[2]:.2f} g/t'\n"
                                "...     return f'{h}: {_m[h]:.1f} m drilled, mean {_wm([x for x "
                                "in _ok if x[0] == h]):.2f} g/t, ' + tail\n"
                                ">>> _got = open('campaign_report.txt', "
                                "encoding='utf-8').read().splitlines()\n"
                                '>>> bool(_got == [_line(h) for h in _holes])\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'One line per hole, sorted by hole_id, exactly in the '
                                           'format shown in the question.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
