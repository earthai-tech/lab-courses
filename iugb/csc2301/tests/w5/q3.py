OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv\n'
                                ">>> _a = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                '>>> _n = {}\n'
                                '>>> for r in _a:\n'
                                "...     _n[r['lithology']] = _n.get(r['lithology'], 0) + 1\n"
                                '>>> bool(lith_counts == _n)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Count the intervals of each lithology: dictionary '
                                           'lithology -> count. dict.get(key, 0) helps.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
