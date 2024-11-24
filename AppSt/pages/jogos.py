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
        "https://github.com/CMatheus7/Jogos_do_Dia_FlashScore/blob/main/Jogos_Do_Dia_FlashScore_"
        + str(dia)
        + ".csv?raw=true"
    )
    return data_jogos


df_jogos = load_data_jogos()

st.dataframe(df_jogos)
