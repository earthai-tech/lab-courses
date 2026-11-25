OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                ">>> _a = _np.loadtxt('well_log_kw2.csv', delimiter=',', "
                                'skiprows=1)\n'
                                '>>> _d, _g, _r, _t = _a[:, 0], _a[:, 1], _a[:, 2], _a[:, 3]\n'
                                '>>> _phi = (2.65 - _r) / (2.65 - 1.0)\n'
                                '>>> bool(_np.allclose(vsh, _np.clip((_g - 25) / (130 - 25), 0, '
                                '1)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'V_sh = (GR - 25) / (130 - 25), clipped to 0–1 with '
                                           'np.clip, no loop.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
