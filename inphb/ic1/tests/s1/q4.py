OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> bool(isinstance(mae_rf_zero, (float, np.floating)) and '
                                'mae_rf_zero > 0)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'mae_rf_zero doit être une MAE positive.'},
                       {'code': ">>> _m0 = make_pipeline(SimpleImputer(strategy='constant', "
                                'fill_value=0), RandomForestRegressor(400, min_samples_leaf=2, '
                                'random_state=0)).fit(X_tr, y_tr)\n'
                                '>>> bool(abs(mae_rf_zero - mean_absolute_error(y_te, '
                                '_m0.predict(X_te))) < 0.05)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Refaites la forêt avec '
                                           "SimpleImputer(strategy='constant', fill_value=0), "
                                           'mêmes paramètres, et calculez la MAE sur le test.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
