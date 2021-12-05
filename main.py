from apps import overview, home, eda, correlation
import streamlit as st
from utils import dev_details

pages = {
    'Home' : home.app,
    'Overview': overview.app,
    'EDA': eda.app,
    "Correlation" : correlation.app,
}

if __name__ == "__main__":
    _, logo_col, _ = st.sidebar.columns([0.3, 1, 1])
    logo_col.image("assets/logo.png", width = 200)
    app = st.sidebar.selectbox('PAGES', pages.keys())
    dev_details()
    if app != "":
        pages[app]()