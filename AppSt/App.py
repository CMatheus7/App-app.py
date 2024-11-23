import streamlit as st
import pandas as pd
import numpy as np


st.title("FOOTBALL DATA")

st.sidebar.header("league")
selected_league = st.sidebar.selectbox("league", ["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"])

st.sidebar.header("season")
selected_season = st.sidebar.selectbox("Season", ["2013/2014", "2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023", "2023/2024", "2024/2025"])

# Web scraping Footbal Data

def load_data(Liga, season):
  url = https://www.football-data.co.uk/mmz4281/"+season+"/"+liga+"/E0.csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)
