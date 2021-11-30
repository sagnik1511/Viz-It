import streamlit as st
from templates import ST_PAGE

class Home(ST_PAGE):

    def render_details(self):
        st.markdown(
            f"<h2 style='text-align: center; color:#9ffff;'>Simple Data Visualization tool developed using streamlit</h2>",
            unsafe_allow_html=True)

        st.markdown(
            f"<h2 style='text-align: center; color:#9ffff;'>Currently supported for csv files</h2>",
            unsafe_allow_html=True)



def app():
    app = Home('Viz-It', 'assets/home_bg.png', '#9ffff')
    app.render_details()




