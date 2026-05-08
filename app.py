import streamlit as st
import urllib.request 
from utils.extracter import phonenums
from utils.sample_text import generate_sample_text
from utils.paywithchai import paywithchai_sidebar, paywithchai_footer

st.set_page_config(page_title="Extract Phone Numbers from text", page_icon='📄')

st.title("Extract Phone Numbers from Text")
st.caption("Paste text or upload a file — get a clean CSV of every Indian phone number found.")

with st.sidebar:
	paywithchai_sidebar()

col5, col6 = st.columns(2)
with col5:
	st.write("Input")

input_container = st.container(border=True)

with input_container:
	sample_data, rawtext, upload, webscraping = st.tabs(["Try Sample Data", "Paste Text", 
														"Upload File", "Web-Scraping"])
	
	with sample_data:
		sample_text = generate_sample_text()
		with st.expander("View sample input document", expanded=True):
			st.text(sample_text)
		sample_extract = st.button("Load this sample", icon=":material/arrow_forward:",shortcut="Enter")
		if sample_extract:
			st.session_state.input_text = sample_text

	with rawtext:
		placeholder_text = "Please contact our Delhi office at 98201 23456 or reach Priya on +91 84739 20011 for further assistance. You can also call our Mumbai helpline at 022-49871234 or WhatsApp Rajan at 7865043210 for quick responses."
		st.session_state.input_text = st.text_area(label="Copy Paste below:", placeholder=placeholder_text, height=150)

	with upload:
		file = st.file_uploader("Upload File", type=['txt'], 
			help="Upload any document containing phone numbers.")
		if file is not None:
			st.session_state.input_text = file.read().decode('utf-8', errors='ignore')
		else:
			st.session_state.input_text = None

	with webscraping:
		url = st.text_area(label="Paste the URL below:", placeholder="https://...")
		st.caption("Enter only one URL at a time.")
		try:
			if url is not None:
				opening = urllib.request.urlopen(str(url))
				st.session_state.input_text = opening.read().decode('utf-8')
			else:
				st.session_state.input_text = None
		except Exception as e:
			print(f"Kuch toh galat hai: {e}")

	col1, col2 = st.columns([2, 1])

	with col2:
		extract = st.button("Extract Numbers" , icon=":material/arrow_forward:",shortcut="Enter")

with st.container(border=True) as output_container:
    col3, col4 = st.columns([2.5, 1])
    with col3:
        st.subheader("Results")
    with st.status("Extracting phone numbers...", expanded=True) as status:
    	if extract:
        	if not st.session_state.input_text or st.session_state.input_text.strip() == "":
        		st.warning("Input is empty.")
        	else:
        		try:
        			df = phonenums(st.session_state.input_text)
        			csv = df.to_csv().encode("utf-8")
        			status.update(label=f"Extracted {len(df)} numbers", state="complete", expanded=False)
        		except Exception as e:
        			status.update(label=f"Something went wrong: {e}", state="error")

        		with col4:
        			download = st.download_button(label="Download as CSV", data=csv,
                                   file_name="phonenumbers.csv", icon=":material/download:")
        		if download:
        			st.toast("Your csv file has been saved.")
        		st.dataframe(df)

paywithchai_footer()