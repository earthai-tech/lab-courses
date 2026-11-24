# UAO · IA appliquée aux géosciences (I)

Master 1 Géosciences · Université Alassane Ouattara (Bouaké) · 20 h · Enseignant : Laurent Kouadio

Page du cours (support de cours en PDF après saisie du code de classe) : **https://www.lkouadio.com/fr/lab/uao/m1**

Un seul notebook accompagne tout le cours : [`M1_TD_TP_enonces.ipynb`](notebooks/M1_TD_TP_enonces.ipynb). Fil rouge : estimer le débit des forages d'eau en socle cristallin à partir de mesures géoélectriques.

| Partie | Thème |
|---|---|
| TD de cours | Tâche, performance, expérience ; types de problèmes ; métriques ; quiz |
| Séance 1 | Prise en main de Python et des données géoscientifiques |
| Séance 2 | Nettoyage (QA/QC) et visualisation exploratoire |
| Séance 3 | Régression supervisée : estimer le débit d'un forage |
| Séance 4 | Classification : forage productif ou improductif |
| Séance 5 | Clustering (K-Means) et usage raisonné de l'IA générative |
| Bonus | La validation spatiale en pratique |

## Données

| Fichier | Contenu |
|---|---|
| [`forages_socle_synthetique.csv`](data/forages_socle_synthetique.csv) | 320 forages synthétiques : position, zone, lithologie, profondeur, altération, résistivité, paramètres géoélectriques (sfi, magnitude, power, ohmic_area) et débit (m³/h). Contient volontairement des erreurs à nettoyer (séance 2). |
| [`forages_socle_propre.csv`](data/forages_socle_propre.csv) | Le même jeu après nettoyage, pour reprendre à la séance 3. |

## Examen final 2025-2026

Épreuve écrite de 1 h 30, sans ordinateur : une partie commune (QCM, 10 points) et un problème selon le parcours (Pédologie, Géomatériaux ou Géomarines, 10 points). La première promotion de Master 2 l'a passée sur le programme de ce cours ; c'est l'examen de référence du Master 1.

- Sujet : [`Examen_final_2025-2026_sujet.pdf`](examen/Examen_final_2025-2026_sujet.pdf)
- Données des trois problèmes, pour s'entraîner sur ordinateur : [`examen/donnees`](examen/donnees) (classification et régression pour chaque parcours, 1 200 échantillons chacun)
- Le corrigé est sur la page du cours, après saisie du code de classe.

## Travailler

- **Google Colab** (recommandé) : cliquez sur le badge *Ouvrir dans Colab* en haut du notebook. La première cellule télécharge les données toute seule. Pour garder votre travail : *Fichier → Enregistrer une copie dans Drive*.
- **Avec Google Drive** : copiez le notebook et le CSV dans un dossier `IA_Geosciences_M1` de votre Drive, puis mettez `UTILISER_DRIVE = True` dans la première cellule.
- **Sans Internet** : téléchargez le kit [`KIT_HORS_LIGNE_M1.zip`](kit/KIT_HORS_LIGNE_M1.zip) (notebook, données, `VERIFIER.bat`, `LANCER_JUPYTER.bat`) et suivez `LISEZMOI.txt` (WinPython sur clé USB ou Anaconda).

Exécutez les cellules dans l'ordre. Après une pause : *Exécution → Exécuter avant*. Pour rendre le travail : *Fichier → Télécharger → .ipynb*, nommé `NOM_Prenom_S1.ipynb` (S2, S3… selon la séance).

Pour l'enseignant : `python tools/prepare_uao_ia.py <M1_TD_TP_enonces.ipynb>` recopie le notebook étudiant. Le notebook corrigé et l'examen corrigé ne vont pas dans ce dépôt public.
