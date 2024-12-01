import streamlit as st
import pandas as pd
import altair as alt

#CSV into DataFrame
def tanora_zokiny():
    df = pd.read_csv(
        "/home/ihasina/python-project/ivandry_ss_db.csv",
        sep=",",
    )

    st.header("Tahan'ny fianarana im-pito")
    st.subheader("Kilasy Tanora Zokiny")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

with st.sidebar:
    st.button(label="Lehibe",)
    st.button(label="Tanora Zokiny", on_click=tanora_zokiny)
    st.button(label="Zatovo")
    st.button(label="Mantoanto")
    st.button(label="Tanora Zandriny")
    st.button(label="Ankizy")
    st.button(label="Zaza bodo")
    st.button(label="Zaza Minono")