OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(gx.shape == (50, 60) and gy.shape == (50, 60) and gx[0, '
                                '0] == 15 and gx[0, -1] == 1195 and gy[-1, 0] == 995)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'gx, gy = np.meshgrid(np.arange(15, 1200, 20), '
                                           'np.arange(15, 1000, 20)): 50 rows (north) by 60 '
                                           'columns (east).'},
                       {'code': '>>> bool(n_nodes == 3000)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'n_nodes = gx.size.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
