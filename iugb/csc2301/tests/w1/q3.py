OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(mean_dh03, float))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'mean_dh03 must be a number with decimals (a float).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _rows = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _s = [r for r in _rows if r['hole_id'] == 'DH-03']\n"
                                ">>> _l = [float(r['to_m']) - float(r['from_m']) for r in _s]\n"
                                ">>> _m = sum(int(r['au_ppb']) / 1000 * l for r, l in zip(_s, _l)) "
                                '/ sum(_l)\n'
                                '>>> bool(abs(mean_dh03 - _m) < 1e-3)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use only DH-03, convert ppb to g/t, and weight each '
                                           'grade by its interval length (to_m - from_m).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
