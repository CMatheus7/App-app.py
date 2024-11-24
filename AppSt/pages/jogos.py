import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

# Título do aplicativo Streamlit
st.title("Jogos do dia")

# Data de análise selecionada pelo usuário
dia = st.date_input("Data de análise", date.today())

# Função para carregar os dados do arquivo CSV
def load_data_jogos():
    # Formatar a data para o formato ddmmyyyy
    dia_formatado = dia.strftime('%d%m%Y')
    
    # Construir o link do arquivo CSV no GitHub
    url = f"https://raw.githubusercontent.com/CMatheus7/Jogos_do_Dia_FlashScore/main/base_excel/jogos_{dia_formatado}.csv"
    
    # Carregar os dados do CSV
    data_jogos = pd.read_csv(url)
    
    return data_jogos

# Tentar carregar os dados e exibir o DataFrame
try:
    df_jogos = load_data_jogos()  # Tenta carregar o CSV
    st.dataframe(df_jogos)  # Exibe os dados na interface do Streamlit
