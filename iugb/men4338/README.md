# IUGB · MEN 4338 · Geostatistics (Lecture & Lab)

Bachelor of Science in Mining Engineering · taught in English · Instructor: Laurent Kouadio

Course page (slides after sign-in with your `@iugb.edu.ci` email): **https://www.lkouadio.com/en/lab/iugb/men4338**

From drill-hole data to a classified mineral resource: exploratory statistics, compositing and declustering, variograms and anisotropy, kriging (point, block, simple, universal, indicator), change of support, grade–tonnage curves and Gaussian simulation. Every method is programmed from scratch with NumPy, so nothing is a black box.

All datasets are **synthetic**: drawn from random fields with a known variogram. For the Bassam gold prospect the true grade of every 10 m cell is given (`bassam_truth_grid.csv`), so students can measure how good each estimate really is.

| Week | Topic | Notebook | Data |
|---|---|---|---|
| 1 | Regionalised variables and exploratory data analysis | [`MEN4338_W1_eda_bassam_gold.ipynb`](notebooks/MEN4338_W1_eda_bassam_gold.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W1_eda_bassam_gold.ipynb) | `bassam_samples.csv` (Bassam gold: 580 RC holes) |
| 2 | Compositing and declustering | [`MEN4338_W2_compositing_declustering.ipynb`](notebooks/MEN4338_W2_compositing_declustering.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W2_compositing_declustering.ipynb) | `bassam_intervals.csv`, `bassam_samples.csv` (Bassam: 3 777 assay intervals) |
| 3 | Spatial continuity: h-scatterplots and the variogram | [`MEN4338_W3_experimental_variogram.ipynb`](notebooks/MEN4338_W3_experimental_variogram.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W3_experimental_variogram.ipynb) | `bassam_samples.csv` (Bassam samples) |
| 4 | Directional variograms and anisotropy | [`MEN4338_W4_anisotropy_directional_variograms.ipynb`](notebooks/MEN4338_W4_anisotropy_directional_variograms.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W4_anisotropy_directional_variograms.ipynb) | `bassam_samples.csv` (Bassam samples) |
| 5 | Variogram models and fitting | [`MEN4338_W5_variogram_models_fitting.ipynb`](notebooks/MEN4338_W5_variogram_models_fitting.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W5_variogram_models_fitting.ipynb) | `bassam_samples.csv` (Bassam samples) |
| 6 | Classical estimators and cross-validation | [`MEN4338_W6_idw_cross_validation.ipynb`](notebooks/MEN4338_W6_idw_cross_validation.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W6_idw_cross_validation.ipynb) | `bassam_samples.csv`, `bassam_truth_grid.csv` (Bassam samples + true grades (12 000 cells)) |
| 7 | Review mini-project: Copper South | [`MEN4338_W7_review_copper_south.ipynb`](notebooks/MEN4338_W7_review_copper_south.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W7_review_copper_south.ipynb) | `copper_south_intervals.csv`, `copper_south_collars.csv` (Copper South: 156 holes, raw intervals) |
| 8 | Ordinary kriging at a point | [`MEN4338_W8_ordinary_kriging_point.ipynb`](notebooks/MEN4338_W8_ordinary_kriging_point.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W8_ordinary_kriging_point.ipynb) | `bassam_samples.csv` (Bassam samples) |
| 9 | Kriging maps and validation | [`MEN4338_W9_kriging_maps_validation.ipynb`](notebooks/MEN4338_W9_kriging_maps_validation.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W9_kriging_maps_validation.ipynb) | `bassam_samples.csv`, `bassam_truth_grid.csv` (Bassam samples + true grades) |
| 10 | Change of support, block kriging and grade–tonnage | [`MEN4338_W10_block_kriging_grade_tonnage.ipynb`](notebooks/MEN4338_W10_block_kriging_grade_tonnage.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W10_block_kriging_grade_tonnage.ipynb) | `bassam_samples.csv`, `bassam_truth_grid.csv` (Bassam samples + true grades) |
| 11 | Trends: simple and universal kriging of porosity | [`MEN4338_W11_trend_simple_universal_kriging.ipynb`](notebooks/MEN4338_W11_trend_simple_universal_kriging.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W11_trend_simple_universal_kriging.ipynb) | `porosity_wells.csv` (Porosity at 48 wells) |
| 12 | Indicator kriging: the probability of ore | [`MEN4338_W12_indicator_kriging.ipynb`](notebooks/MEN4338_W12_indicator_kriging.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W12_indicator_kriging.ipynb) | `bassam_samples.csv`, `bassam_truth_grid.csv` (Bassam samples + true grades) |
| 13 | Sequential Gaussian simulation | [`MEN4338_W13_sequential_gaussian_simulation.ipynb`](notebooks/MEN4338_W13_sequential_gaussian_simulation.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W13_sequential_gaussian_simulation.ipynb) | `bassam_samples.csv` (Bassam samples) |
| 14 | Final project: resource estimate for Kossou | [`MEN4338_W14_final_project_kossou.ipynb`](notebooks/MEN4338_W14_final_project_kossou.ipynb) · [Open in Colab](https://colab.research.google.com/github/earthai-tech/lab-courses/blob/main/iugb/men4338/notebooks/MEN4338_W14_final_project_kossou.ipynb) | `kossou_intervals.csv`, `kossou_collars.csv` (Kossou: 384 holes, raw intervals) |

Each notebook ends with five exercises checked by Otter-Grader: run `grader.check("q1")` under your answer.
The checks recompute the expected result from the data and from your own variables, so the answers are not written in `tests/`.
Week 14 (final project) checks consistency only: the variogram model and the classification are the student's choices, assessed in the report.

Python packages: numpy, pandas, matplotlib, scipy (all available on Google Colab).

For the instructor: `python tools/make_men4338.py` rebuilds every dataset, notebook and test (data generators in that file, one `tools/men4338_wN.py` per week).
