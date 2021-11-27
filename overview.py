import base64
import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt

class Overview():
    def __init__(self, title, background, font):
        bg_ext = background.split('.')[-1]
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
        st.markdown(f"<h1 style='text-align: center; color:#{font};'>{title}</h1>",
                    unsafe_allow_html=True)
        super(Overview, self).__init__()

    def data_handler(self):
        self.file = st.file_uploader("Upload data", type=['csv'])
        self.delete = st.sidebar.button('DELETE DATA')
        if self.file is not None:
            try:
                with open('data.csv', "wb") as f:
                    f.write(self.file.getbuffer())
            except:
                st.write('Invalid format...')
        if self.delete and os.path.isfile('data.csv'):
            os.remove('data.csv')
            st.file = None

    def plot_column_overview(self):
        if os.path.isfile('data.csv'):
            data = pd.read_csv('data.csv')
            fig, ax = plt.subplots(1,2,figsize = (15,5))
            ax[0].pie(data.dtypes.value_counts().values, labels = data.dtypes.value_counts().index)
            ax[0].set_title('Pie-Chart')
            ax[1].bar(x = data.dtypes.value_counts(), height = data.dtypes.value_counts().values, tick_label = data.dtypes.value_counts().index)
            ax[1].set_title('Bar diagram')
            fig.suptitle('Column Overview')
            st.pyplot(fig = fig)

    def fire(self):
        self.data_handler()
        self.plot_column_overview()



app = Overview('Viz-it','src/bg.png','#9ffff')
app.fire()






