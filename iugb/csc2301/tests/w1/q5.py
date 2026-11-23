OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(hole_means, dict) and len(hole_means) == 6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'hole_means must be a dictionary with one entry per '
                                           'hole (6 holes).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _rows = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                '>>> _w = {}; _t = {}\n'
                                '>>> for r in _rows:\n'
                                "...     l = float(r['to_m']) - float(r['from_m'])\n"
                                "...     _w[r['hole_id']] = _w.get(r['hole_id'], 0) + "
                                "int(r['au_ppb']) / 1000 * l\n"
                                "...     _t[r['hole_id']] = _t.get(r['hole_id'], 0) + l\n"
                                '>>> bool(all(abs(hole_means[h] - _w[h] / _t[h]) < 1e-3 for h in '
                                '_w))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each value should be the length-weighted mean grade in '
                                           'g/t of that hole (same method as Q3).'},
                       {'code': '>>> bool(richest_hole == max(hole_means, key=hole_means.get))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'richest_hole should be the hole_id with the highest '
                                           'mean in hole_means.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
