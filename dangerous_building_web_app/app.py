import streamlit as st
import backend


st.set_page_config(page_title="Dangerous Building Philadelphia", layout="wide")

home = st.Page("views/home.py", title="Overview", default=True)
data = st.Page("views/data.py", title="Data Analytics")
resources = st.Page("views/resources.py", title="Resources")
map = st.Page("views/map.py", title="Map")

pg = st.navigation([home, data, resources, map])

pg.run()