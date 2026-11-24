# CURAT · Data Sciences, visualisation et Big Data

M2 Télédétection et SIG (semestre 9, ECUE GAD2432092) · 20 h · 10 séances de 2 h · Enseignant : Laurent Kouadio

Page du cours (diapositives après saisie du code de classe) : **https://www.lkouadio.com/fr/lab/curat/data-science**

| Séance | Thème | TP |
|---|---|---|
| S1 | Data Science et Big Data géospatial | [`TP1_premier_notebook_geospatial`](notebooks/TP1_premier_notebook_geospatial.ipynb) |
| S2 | Formats cloud-native et catalogues STAC | [`TP2_Abidjan_STAC_COG`](notebooks/TP2_Abidjan_STAC_COG.ipynb) |
| S3 | Raster et vecteur : GeoPandas, rioxarray | [`TP3_Tonkpi_pente_zonale`](notebooks/TP3_Tonkpi_pente_zonale.ipynb) |
| S4 | Dask et séries temporelles d'images | [`TP4_Dask_NDVI_Tai`](notebooks/TP4_Dask_NDVI_Tai.ipynb) |
| S5 | Apprentissage automatique et validation spatiale | [`TP5_Yamoussoukro_RF_validation_spatiale`](notebooks/TP5_Yamoussoukro_RF_validation_spatiale.ipynb) |
| S6 | Principes de visualisation | [`TP6_Reparer_trois_graphiques`](notebooks/TP6_Reparer_trois_graphiques.ipynb) |
| S7 | Cartographie interactive et tableaux de bord | [`TP7_Carte_interactive_Abidjan`](notebooks/TP7_Carte_interactive_Abidjan.ipynb) |
| S8 | Produits de télédétection et incertitude | [`TP8_Incertitude_calibration`](notebooks/TP8_Incertitude_calibration.ipynb) |
| S9 | Calcul distribué : Dask, Spark, HPC | [`TP9_Soumettre_mesurer_expliquer`](notebooks/TP9_Soumettre_mesurer_expliquer.ipynb) |
| S10 | Études de cas et mini-projets | [`MiniProjet_modele`](notebooks/MiniProjet_modele.ipynb) |

**Connexion Internet nécessaire** : les TP lisent les images Sentinel-2 (Earth Search, STAC), ESA WorldCover et geoBoundaries directement en ligne, sans tout télécharger.

**Colab** : chaque notebook a un badge *Ouvrir dans Colab* ; une cellule en tête installe les paquets manquants (pystac-client, odc-stac, rioxarray…).
**Sur votre ordinateur** : `conda env create -f environment.yml` (dans ce dossier), puis `conda activate geodatasciences` et `jupyter lab`.

Pour l'enseignant : `python tools/prepare_curat_ds.py <04_Cours>` recopie les notebooks étudiants (pas les versions corrigées de `_build/`).
Les corrigés et notebooks exécutés de l'enseignant ne vont pas dans ce dépôt public.
