import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

from metrics import fleet_summary

engine = create_engine("sqlite:///fleet.db")

df = pd.read_sql(
    "SELECT * FROM trips",
    engine
)

summary = fleet_summary(df)

st.title(
    "Autonomous Fleet Analytics"
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Autonomous KM",
        summary["total_distance"]
    )

    st.metric(
        "Trips",
        summary["total_trips"]
    )

with col2:
    st.metric(
        "Disengagements",
        summary["disengagements"]
    )

    st.metric(
        "Rate/1000km",
        summary["disengagement_rate"]
    )

st.subheader(
    "Distance by Vehicle"
)

vehicle_distance = (
    df.groupby("vehicle_id")
      ["distance_km"]
      .sum()
)

st.bar_chart(vehicle_distance)

st.subheader(
    "Distance by Software Version"
)

release_stats = (
    df.groupby("software_version")
      ["distance_km"]
      .sum()
)

st.bar_chart(release_stats)