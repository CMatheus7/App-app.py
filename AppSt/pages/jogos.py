import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

# Título do aplicativo Streamlit
st.title("Jogos do dia")


dia = st.date_input("Data de analise", date.today())


def load_data_jogos():
    data_jogos = pd.read_csv(
        "https://raw.githubusercontent.com/CMatheus7/Jogos_do_Dia_FlashScore/refs/heads/main/Jogos_Do_Dia_FlashScore/"+str(dia)+.csv"
    )
    return data_jogos


df_jogos = load_data_jogos()

st.dataframe(df_jogos)
