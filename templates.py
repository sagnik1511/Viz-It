import base64
import streamlit as st

class ST_PAGE():
    def __init__(self, title, background, font):
        bg_ext = background.split('.')[-1]
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
        st.markdown(f"<h1 style='text-align: center; color:#{self.font};'>{title}</h1>",
                    unsafe_allow_html = True)