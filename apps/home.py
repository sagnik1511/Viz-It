import base64
import streamlit as st
import utils

class Home():

    def __init__(self, background, font):
        bg_ext = background.split('.')[-1]
        _, image_col, _ = st.columns([1, 1, 1])
        with image_col:
            st.image("assets/logo_text.png", width = 300)
        self.font = font
        st.markdown(
            f"""<style>
                        .reportview-container {{
                            background: url(data:image/{bg_ext};base64,{base64.b64encode(open(background, "rb").read()).decode()})
                            }}
                            background-position: center;
                            background-repeat: no-repeat;
                            background-size: cover;
                            }}
                        </style>""",
            unsafe_allow_html = True
        )
    def render_details(self):
        st.markdown(
            f"<h2 style='text-align: center; color:{self.font};'>Simple Data Visualization tool developed using streamlit</h2>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h4 style='text-align: center; color:#2b1df0;'>{utils.description_text}</h4>",
            unsafe_allow_html = True)
        st.text("")
        _, video_cont, _ = st.columns([0.25, 1, 1])
        video_cont.markdown("""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/t1y0888mF-M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, unsafe_allow_html = True)
        st.markdown(
            f"<h2 style='text-align: center; color:{self.font};'>Currently supported for csv files only. Will update for other data formats too.</h2>",
            unsafe_allow_html = True)
        st.markdown(
            f"<div align = 'center'><h2 style = 'color:{self.font}'>If you like it star this on  <a href = 'http://happyai.epizy.com'>Github</a></h2>",
            unsafe_allow_html = True)
        st.markdown(
            f"<div align = 'center'><h1 style='text-align: center;'>Developed with ❤ by &nbsp;&nbsp;<a href = 'http://happyai.epizy.com'><i>Sagnik Roy</i></a></h1></div>",
            unsafe_allow_html = True)


    def fire(self):
        self.render_details()

def app():
    app = Home('assets/cyan_bg.jpg', "#49056e")
    app.fire()