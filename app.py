import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Maharashtra Climate Tracker", layout="wide")

st.title("Maharashtra Live Climate & Air Quality Tracker")

csv_file = "maharashtra_climate_live_data.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    latest_timestamp = df["timestamp"].max()
    df_latest = df[df["timestamp"] == latest_timestamp]

    st.subheader(f"Latest Update: {latest_timestamp}")
    
    # KPI cards
    col1, col2, col3 = st.columns(3)
    highest_aqi = df_latest.sort_values(by="aqi_index", ascending=False).iloc[0]
    highest_temp = df_latest.sort_values(by="temperature_celsius", ascending=False).iloc[0]

    col1.metric("Highest AQI City", highest_aqi["city"], f"{highest_aqi['aqi_index']} AQI")
    col2.metric("Highest Temp City", highest_temp["city"], f"{highest_temp['temperature_celsius']} °C")
    col3.metric("Total Cities Monitored", f"{len(df_latest)}")

    st.divider()

    # Visual Charts
    c1, c2 = st.columns(2)
    with c1:
        fig_bar = px.bar(df_latest, x="city", y="aqi_index", color="aqi_index", title="Air Quality Index (AQI) by City")
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        fig_scatter = px.scatter(df_latest, x="temperature_celsius", y="humidity_percent", color="city", size="pm2_5", title="Temperature vs Humidity")
        st.plotly_chart(fig_scatter, use_container_width=True)

    # Table
    st.subheader("Stored Data Records")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("Data file nahi mili! Pehle fetch_data.py run karein.")