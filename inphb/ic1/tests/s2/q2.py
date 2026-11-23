OK_FORMAT = True

test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> from sklearn.metrics import recall_score\n'
                                '>>> _cl = sorted(y.unique()); _r = recall_score(y, pred, '
                                'labels=_cl, average=None)\n'
                                '>>> bool(facies_plus_confondu == _cl[int(np.argmin(_r))])\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Cherchez le faciès dont la valeur diagonale (rappel) '
                                           'est la plus faible dans la matrice normalisée.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
