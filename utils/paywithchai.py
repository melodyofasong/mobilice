import streamlit as st

def paywithchai_sidebar():
	st.write("")

	with st.container(border=True):
		st.write("☕ Buy me a chai")
		st.caption("If this tool was useful, a small tip keeps it running.")
		st.markdown("""
    	<a href="https://www.paywithchai.in/melodyofasong" target="_blank"
       	style="
           display: inline-block;
           padding: 8px 18px;
           background-color: #FAEEDA;
           color: #633806;
           border: 1px solid #EF9F27;
           border-radius: 8px;
           font-size: 14px;
           font-weight: 500;
           text-decoration: none;
       ">
       PayWithChai
    	</a>
		""", unsafe_allow_html=True)
	st.write("")
	st.caption("mobilice")
	st.caption("Version 2.2.4")

def paywithchai_footer():
	st.divider()
	col9, col10 = st.columns([4,1])
	with col9:
		st.write("☕ Found this useful? A small tip helps keep this free.")
	with col10:
		st.markdown("""
    	<a href="https://www.paywithchai.in/melodyofasong" target="_blank"
       	style="
        	display: inline-block;
        	padding: 8px 18px;
        	background-color: #FAEEDA;
        	color: #633806;
        	border: 1px solid #EF9F27;
        	border-radius: 8px;
        	font-size: 14px;
        	font-weight: 500;
        	text-decoration: none;
       	">
       	Buy me a chai
    	</a>
		""", unsafe_allow_html=True)
	st.divider()
	col7, col8 = st.columns([4,1])
	with col7:
		st.caption("mobilice")

	with col8:
		st.caption("Version 2.2.4")
