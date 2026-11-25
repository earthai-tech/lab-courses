OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> [round(_gt.vshale(g), 3) for g in (10, 30, 75, 120, 150)]\n'
                                '[0.0, 0.0, 0.5, 1.0, 1.0]',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'vshale(gr, gr_clean=30.0, gr_shale=120.0): (gr - '
                                           'gr_clean) / (gr_shale - gr_clean), clipped to 0–1.'},
                       {'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> round(_gt.vshale(77.5, gr_clean=25, gr_shale=130), 3)\n'
                                '0.5',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The clean and shale lines are parameters with default '
                                           'values.'},
                       {'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> bool(_gt.vshale.__doc__)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Give vshale a docstring too.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
