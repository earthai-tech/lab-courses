OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import numpy as _np\n'
                                '>>> bool(_np.allclose(aniso_h(_np.array([0., 100, '
                                '70.71067811865476]), _np.array([100., 0, 70.71067811865476]), 0, '
                                '300, 100), [100, 300, 223.60679774997897]))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Rotate (dx, dy) into the major (u) and minor (w) axes, '
                                           'then h = sqrt(u² + (w · a_major / a_minor)²).'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> bool(abs(float(aniso_h(70.71067811865476, 70.71067811865476, '
                                '45, 300, 150)) - 100) < 1e-6 and '
                                'abs(float(aniso_h(-70.71067811865476, 70.71067811865476, 45, 300, '
                                '150)) - 200) < 1e-6)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'For azimuth 45: u = dx sin(45°) + dy cos(45°) runs '
                                           'along N045, w = dx cos(45°) - dy sin(45°) along N135.'},
                       {'code': '>>> import numpy as _np\n'
                                '>>> def _sph(h, c0, c, a):\n'
                                '...     h = _np.asarray(h, float); r = _np.minimum(h / a, 1)\n'
                                '...     return _np.where(h > 0, c0 + c * (1.5 * r - 0.5 * r ** '
                                '3), 0.0)\n'
                                '>>> _t = _np.radians(45)\n'
                                '>>> def _ah(dx, dy):\n'
                                '...     u = dx * _np.sin(_t) + dy * _np.cos(_t); w = dx * '
                                '_np.cos(_t) - dy * _np.sin(_t)\n'
                                '...     return _np.sqrt(u ** 2 + (w * 2) ** 2)\n'
                                '>>> _dx = _np.array([0., 50, -80, 120]); _dy = _np.array([0., 50, '
                                '80, -10])\n'
                                '>>> bool(_np.allclose(gamma_bassam(_dx, _dy), _sph(_ah(_dx, _dy), '
                                '0.06, 0.20, 300)))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'gamma_bassam(dx, dy) = spherical(aniso_h(dx, dy, 45, '
                                           '300, 150), 0.06, 0.20, 300).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
