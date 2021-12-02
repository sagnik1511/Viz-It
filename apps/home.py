import base64
import streamlit as st

class Home():

    def __init__(self, background, font):
        bg_ext = background.split('.')[-1]
        self.font = font
        _, image_col, _ = st.columns(3)
        with image_col:
            st.image("assets/logo_text.png", width=300)
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
            unsafe_allow_html=True
        )
    def render_details(self):
        st.markdown(
            f"<h2 style='text-align: center; color:#9ffff;'>Simple Data Visualization tool developed using streamlit</h2>",
            unsafe_allow_html=True)
        st.markdown(
            f"<h2 style='text-align: center; color:#9ffff;'>Currently supported for csv files</h2>",
            unsafe_allow_html=True)


def app():
    app = Home('assets/cyan_bg.jpg', '#9ffff')
    app.render_details()