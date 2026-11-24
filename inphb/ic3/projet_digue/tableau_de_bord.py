"""Tableau de bord : pip install streamlit  puis  streamlit run tableau_de_bord.py"""
import pandas as pd
import streamlit as st

from digue import SystemeSurveillance, verifier_contrat

st.set_page_config(page_title="Surveillance digue", layout="wide")
st.title("Surveillance de la digue à résidus")

systeme = SystemeSurveillance.charger("systeme_digue.joblib")
fichier = st.file_uploader("Fichier capteurs (CSV)", type="csv")
df = pd.read_csv(fichier) if fichier else pd.read_csv("../data/digue_residus_capteurs.csv")

problemes = verifier_contrat(df)
if problemes:
    st.error("Contrat de données non respecté : " + "; ".join(problemes))
    st.stop()

alertes = systeme.alertes(df)
capteur = st.selectbox("Capteur", list(systeme.modeles))
dernier = alertes.iloc[-1]
c1, c2, c3 = st.columns(3)
c1.metric("Mesure", f"{df[capteur].iloc[-1]:.2f} m")
c2.metric("Attendu", f"{dernier[capteur + '_attendu']:.2f} m", f"{dernier[capteur + '_residu']:+.2f} m")
c3.metric("Statut", "ALERTE" if dernier[capteur + "_alerte"] else "normal")

st.subheader("Mesuré et attendu")
st.line_chart(alertes.set_index("date")[[capteur + "_attendu"]].join(df.set_index("date")[[capteur]]))
st.subheader("Résidu et seuil conforme")
r = alertes.set_index("date")[[capteur + "_residu"]]
r["seuil"] = systeme.seuils[capteur]
r["-seuil"] = -systeme.seuils[capteur]
st.line_chart(r)
st.subheader("Dérive des capteurs (biais mensuel)")
d = systeme.derive(df)
st.dataframe(d[d["capteur"] == capteur].tail(12))
st.caption("Une alerte n’est pas un diagnostic : elle déclenche une inspection par l’ingénieur géotechnicien.")
