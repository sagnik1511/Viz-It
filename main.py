import json
import os
import streamlit as st
from apps import overview
def app():
    st.markdown(f"<h1 style='text-align: center; color:#9ffff;'>Viz-It</h1>",
                unsafe_allow_html=True)

    st.markdown(f"<h2 style='text-align: center; color:#9ffff;'>Simple Data Visualization tool developed using streamlit</h2>",
                unsafe_allow_html=True)

    st.markdown(
        f"<h2 style='text-align: center; color:#9ffff;'>Currently supported for csv files</h2>",
        unsafe_allow_html=True)
pages = {
    'Home' : app,
    'Overview': overview.app,
}

if __name__ == "__main__":
    app = st.sidebar.selectbox('page',pages.keys())
    if app != "":
        pages[app]()