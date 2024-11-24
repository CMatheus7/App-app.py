import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date


st.title("Jogos do dia")


dia = st.date_input("Data de análise", date.today())


def load_data_jogos():
    # Formatar a data para o formato ddmmyyyy
    dia_formatado = dia.strftime('%d%m%Y')
    
  
    url = f"https://raw.githubusercontent.com/CMatheus7/Jogos_do_Dia_FlashScore/main/base_excel/jogos_{dia_formatado}.csv"
    
  
    data_jogos = pd.read_csv(url)
    
    return data_jogos


df_jogos = load_data_jogos()

st.dataframe(df_jogos)
