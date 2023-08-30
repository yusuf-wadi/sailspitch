import streamlit as st
st.set_page_config(page_icon="⛵", page_title='SailsPitch')

from components.main import main
from components.sidebar import sidebar
from components.app_auth import login_register
from components.header_ import header
import subprocess

st.session_state['app_version'] = "1"
# session state

if "authentication_status" not in st.session_state:
    st.session_state['authentication_status'] = None
if "name" not in st.session_state:
    st.session_state['name'] = None
if "username" not in st.session_state:
    st.session_state['username'] = None
if "credits" not in st.session_state:
    st.session_state['credits'] = None

# start backend for stripe
# subprocess.Popen(["ruby" ,"src/server.rb"])

if __name__ == '__main__':
    
    if not st.session_state['authentication_status']:
        header()
        login_register()
    else:
        main()
        sidebar()
        