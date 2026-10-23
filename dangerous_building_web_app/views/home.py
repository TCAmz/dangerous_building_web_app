import streamlit as st
import backend

st.title("Dangerous Building Home Page", text_alignment= "center")
st.image("assets/images/home_page_main_img.png", use_container_width=True)

st.subheader("What is this website about?")
st.markdown("This website shows the data of the number of dangerous buildings reported and recorded since 2021. All data is recorded by 311 and stored on [OpenDataPhilly](https://opendataphilly.org/)")

st.subheader("What is a dangerous building?")
st.text('''A dangerous building is a threat for public safety, health and property. A poorly maintained building can collapse at any time, the rate based on how bad the building is. And once it collapses, it is a death threat for people inside, people on the street and nearby houses.
A building can be considered as dangerous if:

-Has structural issues
-Has poor maintained
-Has high fire risk
-Falling Bricks
-Unrepaired racks
''')
st.markdown("More information can be found at: [Philly Stat 360](https://philly-stat-360.phila.gov/pages/demolitions)")

st.subheader("Why are there many dangerous buildings in Philadelphia?")
st.markdown("According to [NBC10Philadelphia](https://www.nbcphiladelphia.com/investigators/more-than-two-year-after-li-split-properties-linger-in-unsafe-and-dangerous-status/4335677/) there are over 3,300 unsafe buildings are accorded in early 2026. There are many reasons for that number but abandoned buildings and old structures, materials because many houses in Philadelphia were built for decades are two main reasons.")
st.subheader("Where to report if you think a building is dangerous?")
st.markdown("You can report a building by calling 311 or through [Philly 311 online portal](https://www.phila.gov/services/property-lots-housing/submit-a-service-request-with-311/)")
st.image("assets/images/philly-311-bell.png", width = 100)

st.text("Thanh Cao-10/23/2026")