import streamlit as st


st.markdown("""   
    <style>
    .stApp {background-color:rgb(101, 166, 250);}
    </style>
    """, unsafe_allow_html=True)
# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 4, Web Development - Section B")
st.subheader("Anthony Edgecombe, Patrick Vettickatt")
st.subheader("Page Descriptions")
st.markdown("Patrick Portfolio")
st.markdown("Ty Portfolio")
st.markdown("Weather")

with st .container():
    container = st.container(border=True)
    container.write("""
    Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

    1. Anthony Edgecombe's Portfolio Page: View Education, Proffessional Experience, Projects, Skills, and Activities
    2. Patrick Vettickatt's Portfolio: View Education, Proffessional Experience, Projects, Skills, and Activities
    3. Weather App: Input latitude and longditude to caluculate the weather forcast for the next 7 Days.
    4. Dream Destination: Compare vacation spots with our ai integrated model. Get weather reports and an analysis of which destination is more ideal! 

    """)

