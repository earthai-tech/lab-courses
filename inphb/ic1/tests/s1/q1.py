OK_FORMAT = True

test = {'name': 'q1',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(meilleur_modele, str) and meilleur_modele in '
                                'modeles)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "meilleur_modele doit être une chaîne : 'lin', 'ridge' "
                                           "ou 'rf'."},
                       {'code': '>>> _mae = {k: mean_absolute_error(y_te, m.predict(X_te)) for k, '
                                'm in modeles.items()}\n'
                                '>>> bool(meilleur_modele == min(_mae, key=_mae.get))\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "Ce n'est pas le modèle qui a la plus petite MAE sur le "
                                           'test.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
