import streamlit as st
import backend
import pandas as pd 

st.title("Dangerous Building Data Page")

data2021_zipcode_file = "assets/data/danger_building_data_2021_pivot.csv"
data2022_zipcode_file = "assets/data/danger_building_data_2022_pivot.csv"
data2023_zipcode_file = "assets/data/danger_building_data_2023_pivot.csv"
data2024_zipcode_file = "assets/data/danger_building_data_2024_pivot.csv"
data2025_zipcode_file = "assets/data/danger_building_data_2025_pivot.csv"


data2021_zipcode = backend.create_df(data2021_zipcode_file)
data2022_zipcode = backend.create_df(data2022_zipcode_file)
data2023_zipcode = backend.create_df(data2023_zipcode_file)
data2024_zipcode = backend.create_df(data2024_zipcode_file)
data2025_zipcode = backend.create_df(data2025_zipcode_file)

data2021_file = "assets/data/danger_building_data_2021.csv"
data2022_file = "assets/data/danger_building_data_2022.csv"
data2023_file = "assets/data/danger_building_data_2023.csv"
data2024_file = "assets/data/danger_building_data_2024.csv"
data2025_file = "assets/data/danger_building_data_2025.csv"


data2021 = backend.create_df(data2021_file)
data2022 = backend.create_df(data2022_file)
data2023 = backend.create_df(data2023_file)
data2024 = backend.create_df(data2024_file)
data2025 = backend.create_df(data2025_file)
action = st.menu_button("Year", options=["2021", "2022", "2023", "2024", "2025"])
if action == "2021":
    mean = round(data2021_zipcode["COUNT of zipcode"].mean())
    median = round(data2021_zipcode["COUNT of zipcode"].median())
    range = data2021_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2021")
    st.bar_chart(data2021_zipcode, x = "zipcode", y="COUNT of zipcode")
elif action == "2022":
    mean = round(data2022_zipcode["COUNT of zipcode"].mean())
    median = round(data2022_zipcode["COUNT of zipcode"].median())
    range = data2022_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2022")
    st.bar_chart(data2022_zipcode, x = "zipcode", y="COUNT of zipcode")
elif action == "2023":
    mean = round(data2023_zipcode["COUNT of zipcode"].mean())
    median = round(data2023_zipcode["COUNT of zipcode"].median())
    range = data2023_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2023")
    st.bar_chart(data2023_zipcode, x = "zipcode", y="COUNT of zipcode")
elif action == "2024":
    mean = round(data2024_zipcode["COUNT of zipcode"].mean())
    median = round(data2024_zipcode["COUNT of zipcode"].median())
    range = data2024_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2024")
    st.bar_chart(data2024_zipcode, x = "zipcode", y="COUNT of zipcode")
elif action == "2025":
    mean = round(data2025_zipcode["COUNT of zipcode"].mean())
    median = round(data2025_zipcode["COUNT of zipcode"].median())
    range = data2025_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2025")
    st.bar_chart(data2025_zipcode, x = "zipcode", y="COUNT of zipcode")
else:
    mean = round(data2021_zipcode["COUNT of zipcode"].mean())
    median = round(data2021_zipcode["COUNT of zipcode"].median())
    range = data2021_zipcode["COUNT of zipcode"].max() - data2021_zipcode["COUNT of zipcode"].min()

    st.subheader("Case Number in 2021")
    st.bar_chart(data2021_zipcode, x = "zipcode", y="COUNT of zipcode")

col1, col2, col3 = st.columns(3)
col1.metric("Mean", str(mean))
col2.metric("Median", str(median))
col3.metric("Range", str(range))

if action =="2021":
    st.map(data2021, alt="Sample points", latitude="lat", longitude="lon")
elif action == "2022":
    map_data = data2022.dropna(subset=["lat", "lon"])
    st.map(map_data, alt="Sample points", latitude="lat", longitude="lon")

elif action == "2023":
    map_data = data2023.dropna(subset=["lat", "lon"])
    st.map(map_data, alt="Sample points", latitude="lat", longitude="lon")
elif action == "2024":
    map_data = data2024.dropna(subset=["lat", "lon"])
    st.map(map_data, alt="Sample points", latitude="lat", longitude="lon")
elif action == "2025":
    st.text("No map data for 2025")
else:
    st.map(data2021, alt="Sample points", latitude="lat", longitude="lon")