OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> _gt.GOLD_OZ_G\n'
                                '31.1035',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'geotools.py must define the constant GOLD_OZ_G = '
                                           '31.1035 (grams in one troy ounce).'},
                       {'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> (round(_gt.block_tonnes(10, 10, 5, 2.7), 6), '
                                'round(_gt.gold_ounces(1350, 2.0), 3))\n'
                                '(1350.0, 86.807)',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Copy your week 3 block_tonnes and gold_ounces into '
                                           'geotools.py; gold_ounces must use GOLD_OZ_G.'},
                       {'code': '>>> import importlib as _il, geotools as _gt\n'
                                '>>> _gt = _il.reload(_gt)\n'
                                '>>> bool(_gt.block_tonnes.__doc__ and _gt.gold_ounces.__doc__)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Each function needs a docstring: a """text""" line '
                                           'right under the def.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
