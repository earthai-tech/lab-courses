OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(n_intervals, int))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_intervals must be a whole number (an int).'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _rows = list(_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8')))\n"
                                '>>> bool(n_intervals == len(_rows))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Count every assay interval in the file, not the header '
                                           'line.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
