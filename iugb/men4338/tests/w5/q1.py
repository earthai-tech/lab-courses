OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n'
                                '...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** '
                                '3), 0.0)\n'
                                '>>> _h = _np.array([0, 10, 50, 99.9, 100, 250])\n'
                                '>>> bool(_np.allclose(spherical(_h, 0.1, 0.5, 100), _sph(_h, 0.1, '
                                '0.5, 100)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'spherical: c0 + c (1.5 h/a - 0.5 (h/a)^3) for h < a, '
                                           'c0 + c beyond, and exactly 0 at h = 0.'},
                       {'code': '>>> bool(float(spherical(0.0, 0.1, 0.5, 100)) == 0.0 and '
                                'abs(float(spherical(1e-9, 0.1, 0.5, 100)) - 0.1) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'γ(0) = 0 but γ jumps to the nugget c0 as soon as h > '
                                           '0: use np.where(h > 0, ..., 0.0).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
