# IUGB · CSC 2301 · Principles of Computer Programming

Bachelor of Science in Mining Engineering and Petroleum Engineering · taught in English · Instructor: Laurent Kouadio

Course page (slides after sign-in with your `@iugb.edu.ci` email): **https://www.lkouadio.com/en/lab/iugb/csc2301**

| Week | Topic | Notebook | Data |
|---|---|---|---|
| 1 | Python basics with drill-hole data | [`CSC2301_W1_python_basics.ipynb`](notebooks/CSC2301_W1_python_basics.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/csc2301/notebooks/CSC2301_W1_python_basics.ipynb) | `drillholes_assays.csv` (synthetic, 99 intervals, 6 holes) |
| 2 | Control flow on a well log | [`CSC2301_W2_control_flow_well_log.ipynb`](notebooks/CSC2301_W2_control_flow_well_log.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/csc2301/notebooks/CSC2301_W2_control_flow_well_log.ipynb) | `well_log_kw1.csv` (synthetic gamma ray and porosity, 301 samples) |

Later weeks are added as the course progresses.

Each notebook ends with exercises checked by Otter-Grader: run `grader.check("q1")` under your answer.
The checks recompute the expected result from the data, so the answers are not written in `tests/`.

For the instructor: `python tools/make_csc2301.py` rebuilds every week's data, notebook and tests (week 1 in that file, later weeks in `tools/csc2301_w*.py`).
