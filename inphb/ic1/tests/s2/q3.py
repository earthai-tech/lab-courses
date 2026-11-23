OK_FORMAT = True

test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(acc_gr_norm, (float, np.floating)) and 0 < '
                                'acc_gr_norm <= 1)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'acc_gr_norm doit être une exactitude entre 0 et 1.'},
                       {'code': ">>> _X = X.copy(); _X['GR_api'] = "
                                "fa.groupby('puits')['GR_api'].transform(lambda s: (s - s.mean()) "
                                '/ s.std())\n'
                                ">>> _a = cross_val_score(modeles['rf'], _X, y, cv=GroupKFold(6), "
                                'groups=puits).mean()\n'
                                '>>> bool(abs(acc_gr_norm - _a) < 0.01)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Remplacez GR par sa version normalisée par puits, puis '
                                           'refaites la validation GroupKFold(6) avec la forêt.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
