import streamlit as st

def header():

    st.title(f"⛵ SailsPitch v{st.session_state['app_version']}")
    st.markdown("<h5>Give your ideas a voice</h5>", unsafe_allow_html=True)