OK_FORMAT = True

test = {'name': 'q5',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import pandas as _pd, numpy as _np\n'
                                ">>> _s = _pd.read_csv('bassam_samples.csv')\n"
                                ">>> _g = _s[_s['campaign'] == 'grid']\n"
                                ">>> _x, _y, _v = (_g[c].to_numpy() for c in ('x', 'y', "
                                "'au_gpt'))\n"
                                '>>> _i, _j = _np.triu_indices(len(_v), 1)\n'
                                '>>> _dx = _np.concatenate([_x[_j] - _x[_i], _x[_i] - _x[_j]]); '
                                '_dy = _np.concatenate([_y[_j] - _y[_i], _y[_i] - _y[_j]])\n'
                                '>>> _sq = _np.tile(0.5 * (_v[_j] - _v[_i]) ** 2, 2)\n'
                                '>>> _ix = _np.floor((_dx + 300) / 50).astype(int); _iy = '
                                '_np.floor((_dy + 300) / 50).astype(int)\n'
                                '>>> _k = (_ix >= 0) & (_ix < 12) & (_iy >= 0) & (_iy < 12)\n'
                                '>>> _s1 = _np.zeros((12, 12)); _n1 = _np.zeros((12, 12))\n'
                                '>>> _np.add.at(_s1, (_iy[_k], _ix[_k]), _sq[_k]); _np.add.at(_n1, '
                                '(_iy[_k], _ix[_k]), 1)\n'
                                '>>> _vm = _np.where(_n1 > 0, _s1 / _np.maximum(_n1, 1), _np.nan)\n'
                                '>>> bool(vmap.shape == (12, 12) and _np.allclose(vmap, _vm, '
                                'equal_nan=True))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'vmap[row, col]: mean of 0.5*(z_i - z_j)^2 for the '
                                           'separation vectors (both signs) falling in cell row = '
                                           'floor((dy+300)/50), col = floor((dx+300)/50); NaN '
                                           'where empty.'},
                       {'code': '>>> bool(len(ax_vm.images) >= 1)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Draw vmap with ax_vm.imshow(..., origin='lower', "
                                           'extent=[-300, 300, -300, 300]).'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
