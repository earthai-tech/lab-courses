OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv, numpy as _np\n'
                                ">>> _g = [int(r['au_ppb']) / 1000 for r in "
                                "_csv.DictReader(open('drillholes_assays.csv', "
                                "encoding='utf-8'))]\n"
                                '>>> _c, _e = _np.histogram(_g, bins=_np.arange(0, 10.5, 0.5))\n'
                                '>>> bool(_np.array_equal(_np.asarray(counts), _c))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'counts comes from ax_hist.hist(grades, '
                                           'bins=np.arange(0, 10.5, 0.5)): it returns (counts, '
                                           'edges, patches).'},
                       {'code': ">>> bool('g/t' in ax_hist.get_xlabel() and ax_hist.get_ylabel() "
                                "!= '')\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Label the x axis with the unit (g/t) and the y axis '
                                           '(number of intervals).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
