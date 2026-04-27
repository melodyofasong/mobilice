import streamlit as st
from utils.paywithchai import paywithchai_sidebar, paywithchai_footer

st.subheader("Access to 1000 Free Phone Numbers")

with st.sidebar:
	paywithchai_sidebar()

st.write("City-wise differentiation")
# use urllib.request for webscraping method .urlopen.read()
st.space()
st.write("This project is still in progress and not open to the public eye yet.")

paywithchai_footer()
