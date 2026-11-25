OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.array_equal(reliable, n_grid >= 30))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'reliable = n_grid >= 30 (a boolean array).'},
                       {'code': ">>> bool(len(ax_vg.lines) >= 2 and 'm' in ax_vg.get_xlabel())\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Plot g_grid against h_grid with markers, a dashed '
                                           'horizontal line at var_grid (ax_vg.axhline) and an x '
                                           'label with the unit.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(nugget_guess - g_grid[0]) < 1e-12 and abs(sill_guess '
                                '- var_grid) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'nugget_guess = g_grid[0] (first lag), sill_guess = '
                                           'var_grid.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
