from apps import overview, home, eda
from PIL import Image
import streamlit as st

pages = {
    'Home' : home.app,
    'Overview': overview.app,
    'EDA': eda.app,
}

if __name__ == "__main__":
    logo = Image.open("assets/logo.png")
    st.sidebar.image(logo, width = 150)
    app = st.sidebar.selectbox('PAGES',pages.keys())
    if app != "":
        pages[app]()