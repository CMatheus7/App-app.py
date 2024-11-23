import streamlit as st
import pandas as pd
import numpy as np


st.title("FOOTBALL DATA")

st.sidebar.header("league")
selected_league = st.sidebar.selectbox(
    "league", ["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"]
)

st.sidebar.header("season")
selected_season = st.sidebar.selectbox(
    "Season",
    [
        "2013/2014",
        "2014/2015",
        "2015/2016",
        "2016/2017",
        "2017/2018",
        "2018/2019",
        "2019/2020",
        "2020/2021",
        "2021/2022",
        "2022/2023",
        "2023/2024",
        "2024/2025",
    ],
)

# Web scraping Footbal Data


def load_data(league, season):

    if selected_league == "England":
        liga = "E0"
    if selected_league == "Germany":
        liga = "D1"
    if selected_league == "Italy":
        liga = "I1"
    if selected_league == "Spain":
        liga = "SP1"
    if selected_league == "France":
        liga = "F1"


    if selected_season == "2012/2013":
        season = "1213"
    if selected_season == "2013/2014":
        season = "1314"
    if selected_season == "2014/2015":
        season = "1415"
    if selected_season == "2015/2016":
        season = "1516"
    if selected_season == "2016/2017":
        season = "1617"
    if selected_season == "2017/2018":
        season = "1718"
    if selected_season == "2018/2019":
        season = "1819"
    if selected_season == "2019/2020":
        season = "1920"
    if selected_season == "2020/2021":
        season = "2021"
    if selected_season == "2021/2022":
        season = "2122"
    if selected_season == "2022/2023":
        season = "2223"
    if selected_season == "2023/2024":
        season = "2324"
    if selected_season == "2024/2025":
        season = "2425"

    url = "https://www.football-data.co.uk/mmz4281/" + season + "/" + league + ".csv"

    data = pd.read_csv(url)
    return data


df = load_data(selected_league, selected_season)


st.subheader("Dataframe: " + selected_league)
st.dataframe(df)
