from apps import overview, home
import streamlit as st

pages = {
    'Home' : home.app,
    'Overview': overview.app,
}

if __name__ == "__main__":
    st.sidebar.header("VIZ-IT")
    app = st.sidebar.selectbox('PAGES',pages.keys())
    if app != "":
        pages[app]()