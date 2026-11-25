OK_FORMAT = True

test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) "
                                "* float(r['density_t_m3']) for r in _b]\n"
                                ">>> _g = [float(r['au_gpt']) for r in _b]\n"
                                '>>> import statistics as _st\n'
                                '>>> bool(abs(median_grade - _st.median(_g)) < 1e-12 and '
                                'abs(stdev_grade - _st.stdev(_g)) < 1e-12)\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Use the standard-library module statistics: '
                                           'statistics.median and statistics.stdev on the grades.'},
                       {'code': '>>> import csv as _csv\n'
                                ">>> _b = list(_csv.DictReader(open('block_model_pit1.csv', "
                                "encoding='utf-8')))\n"
                                ">>> _t = [float(r['dx_m']) * float(r['dy_m']) * float(r['dz_m']) "
                                "* float(r['density_t_m3']) for r in _b]\n"
                                ">>> _g = [float(r['au_gpt']) for r in _b]\n"
                                '>>> from collections import Counter as _C\n'
                                ">>> bool(rock_counts == _C(r['rock'] for r in _b))\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'rock_counts = Counter(...) of the rock column: from '
                                           'collections import Counter.'}],
             'scored': True,
             'setup': '',
             'teardown': '',
             'type': 'doctest'}]}
