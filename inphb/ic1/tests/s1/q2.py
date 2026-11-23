OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(r2_rf, (float, np.floating)))\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'r2_rf doit être un nombre (utilisez r2_score).'},
                       {'code': ">>> bool(abs(r2_rf - r2_score(y_te, modeles['rf'].predict(X_te))) "
                                '< 1e-3)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'r2_rf ne correspond pas au R² de la forêt sur le jeu '
                                           'de test.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
