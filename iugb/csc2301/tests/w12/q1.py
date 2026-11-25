OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> [find_first([45, 60, 120, 98, 130], 100), find_first([45, '
                                '60], 100), find_first([], 5)]\n'
                                '[2, -1, -1]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Return the position of the FIRST value greater than '
                                           'the threshold, or -1 when there is none.'},
                       {'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> bool(first_shale == int(_np.argmax(_a[:, 1] > 100)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'first_shale = find_first(gr, 100) with gr the GR '
                                           'column of well_log_kw2.csv, as a list.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
