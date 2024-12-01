import streamlit as st
import pandas as pd


def lehibe():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_lehibe.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Lehibe.")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#1eff1e"],
        stack=False
    )

def tanora_zokiny():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_tanorazokiny.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
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

def zatovo():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_zatovo.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Zatovo")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

def mantoanto():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_mantoanto.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Mantoanto")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

def tanora_zandriny():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_tanorazandriny.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Tanora Zandiny")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

def ankizy():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_ankizy.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Ankizy")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

def zaza_minono():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_zazaminono.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Zaza Minono")
    st.bar_chart(
        df,
        y=["mambra_tonga", "nianatra_im-pito"],
        y_label="isa",
        x="sabata",
        x_label="Sabata",
        color=["#808080", "#ff1e1e"],
        stack=False
    )

def zaza_bodo():
    url = "https://github.com/UrimThummim0/python-project/blob/main/ivandry_ss_db_zazabodo.csv?raw=true"
    df = pd.read_csv(url, sep=",")

    st.header("Tahan'ny fianarana im-pito.")
    st.subheader("Kilasy Zaza Bodo")
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
    st.logo("sda.png")
    st.button(label="Lehibe", on_click=lehibe)
    st.button(label="Tanora Zokiny", on_click=tanora_zokiny)
    st.button(label="Zatovo", on_click=zatovo)
    st.button(label="Mantoanto", on_click=mantoanto)
    st.button(label="Tanora Zandriny", on_click=tanora_zandriny)
    st.button(label="Ankizy", on_click=ankizy)
    st.button(label="Zaza bodo", on_click=zaza_bodo)
    st.button(label="Zaza Minono", on_click=zaza_minono)
