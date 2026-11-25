OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> _v = [2.31, 2.05, 2.62, 2.05, 1.98]\n'
                                '>>> (selection_sort(_v), _v)\n'
                                '([1.98, 2.05, 2.05, 2.31, 2.62], [2.31, 2.05, 2.62, 2.05, 1.98])',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Return a NEW sorted list (smallest first) and leave '
                                           'the input list unchanged: work on a copy, values[:].'},
                       {'code': '>>> [selection_sort([]), selection_sort([7])]\n[[], [7]]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'An empty list and a one-element list are already '
                                           'sorted.'},
                       {'code': '>>> import inspect as _in\n'
                                '>>> _s = _in.getsource(selection_sort)\n'
                                ">>> bool('sorted(' not in _s and '.sort(' not in _s and 'min(' "
                                'not in _s)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Write the algorithm yourself: no sorted(), .sort() or '
                                           'min() inside selection_sort.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
