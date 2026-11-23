OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> bool(abs(ecart_rf - (scores['rf'][0] - scores['rf'][1])) < "
                                '1e-3)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'ecart_rf = exactitude k-fold aléatoire − exactitude '
                                           "GroupKFold, pour la forêt ('rf')."},
                       {'code': '>>> bool(ecart_rf > 0)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "L'écart devrait être positif : le k-fold aléatoire est "
                                           'optimiste.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
