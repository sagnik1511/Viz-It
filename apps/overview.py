import os
import pandas as pd
import plotly.express as px
import streamlit as st
from templates import ST_PAGE

class Overview(ST_PAGE):

    def data_handler(self):
        self.file = st.file_uploader("Upload data", type = ['csv'])
        _,_,_,col,_,_,_ = st.columns(7)
        with col:
            self.delete = st.button('DELETE DATA')
        if self.file is not None:
            try:
                with open('data.csv', "wb") as f:
                    f.write(self.file.getbuffer())
            except:
                st.write('Invalid format...')
        if self.delete and os.path.isfile('data.csv'):
            os.remove('data.csv')
            st.file = None

    def fetch_data(self):
        self.data = pd.DataFrame({})
        if os.path.isfile('data.csv'):
            self.data = pd.read_csv('data.csv')

    def null_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Missing Value Analysis</h3>",
                        unsafe_allow_html = True)
            null_overview_figure = px.bar(x = self.data.isnull().sum().index,
                                          y = self.data.isnull().sum().values,
                                          title = f"Null value Overview")
            st.plotly_chart(null_overview_figure, use_container_width = True)

    def duplicates_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Duplicate Value Analysis</h3>",
                        unsafe_allow_html = True)
            row_duplicate_count = len(self.data) - len(self.data.drop_duplicates())
            st.markdown(f"<h5 style='text-align: center;'>Duplicate rows : {row_duplicate_count}</h5>",
                        unsafe_allow_html = True)
            col_duplicate_count = self.data.shape[1] - self.data.T.drop_duplicates().shape[0]
            st.markdown(
                f"<h5 style='text-align: center;'>Duplicate columns : {col_duplicate_count}</h5>",
                unsafe_allow_html = True)
    def column_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Column Overview</h3>",
                        unsafe_allow_html = True)
            cols_data = pd.DataFrame(
                {
                    'name': self.data.dtypes.value_counts().index.astype('str').tolist(),
                    'value': self.data.dtypes.value_counts().values.astype('int64').tolist()
                }
            )

            bar_fig = px.bar(x = cols_data['name'], y = cols_data['value'],
                             title = f"Column Data Type Distribution ")
            st.plotly_chart(bar_fig)

    def fire(self):
        self.data_handler()
        self.fetch_data()
        self.column_overview()
        self.null_overview()
        self.duplicates_overview()

def app():
    app = Overview('Overview', 'assets/fadered_bg.png', "#00008B")
    app.fire()