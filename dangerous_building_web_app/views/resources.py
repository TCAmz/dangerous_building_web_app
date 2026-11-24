import streamlit as st
import backend

st.title("Dangerous Building Resources Page", icon= "📈")

st.text("By Thanh Cao\nNov 24th, 2026")

st.subheader("Where all infomation came from:")
list_of_sources = '''
- [Philly Stat 360](https://philly-stat-360.phila.gov/pages/demolitions) 
- [NBC Philadelphia](https://www.nbcphiladelphia.com/investigators/more-than-two-year-after-li-split-properties-linger-in-unsafe-and-dangerous-status/4335677/)
- [NBC10 Philadelphia Youtube video](https://www.youtube.com/watch?v=zqLezlRS_Tg)
'''
st.markdown(list_of_sources)

st.subheader("Dataset and how it was used:")
st.markdown("All data came from [OpenDataPhilly](https://opendataphilly.org/datasets/)")

data_used_text = '''
- Clean the data:
1. The large data files were imported into Excel to filter for dangerous building cases only
2. remove blank, duplicate information and unused columns
- Google Sheet was used to create pivot tables and count the number of houses in each ZIP code area
'''
st.markdown(data_used_text)

st.subheader("Development tools:")
st.markdown('''- Coded with Python
- [Streamlit](https://streamlit.io/) and [Pandas](https://pandas.pydata.org/docs/reference/index.html) were used to display and run the web app.''')

st.subheader("Please report for your safety and the safety of other citizens!!")
st.markdown("If you notice any house is in a dangerous condition, you can call 311 or report it through the [Philly 311 online portal](https://www.phila.gov/services/property-lots-housing/submit-a-service-request-with-311/). They will send people to check on the house situation.")
st.image("assets/images/philly-311-bell.png", width = 100)

