import matplotlib.pyplot as plt
import os
import pandas as pd
import plotly.express as px
import streamlit as st
from templates import ST_PAGE

class Overview(ST_PAGE):

    def data_handler(self):
        self.file = st.file_uploader("Upload data", type=['csv'])
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

    def column_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:#00008B;'>Column Overview</h3>",
                        unsafe_allow_html=True)
            column_overview_figure, column_overview_ax= plt.subplots(1,2,figsize = (15,5))
            column_overview_ax[0].pie(self.data.dtypes.value_counts().values,
                                      labels = self.data.dtypes.value_counts().index)
            column_overview_ax[0].set_title('Pie-Chart')
            column_overview_ax[1].bar(x = self.data.dtypes.value_counts(),
                                      height = self.data.dtypes.value_counts().values,
                                      tick_label = self.data.dtypes.value_counts().index)
            column_overview_ax[1].set_title('Bar diagram')
            column_overview_figure.suptitle('Column Overview')
            st.pyplot(fig = column_overview_figure)

    def null_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:#00008B;'>Missing Value Analysis</h3>",
                        unsafe_allow_html=True)
            null_overview_figure = px.bar(x = self.data.isnull().sum().index,
                                          y = self.data.isnull().sum().values)
            st.plotly_chart(null_overview_figure, use_container_width=True)

    def duplicates_overview(self):
        if len(self.data.columns) > 0:
            st.markdown(f"<h3 style='text-align: center; color:#00008B;'>Duplicate Value Analysis</h3>",
                        unsafe_allow_html=True)
            row_duplicate_count = len(self.data) - len(self.data.drop_duplicates())
            st.markdown(f"<h5 style='text-align: center; color:#{self.font};'>Duplicate rows : {row_duplicate_count}</h5>",
                        unsafe_allow_html=True)
            col_duplicate_count = self.data.shape[1] - self.data.T.drop_duplicates().shape[0]
            st.markdown(
                f"<h5 style='text-align: center; color:#{self.font};'>Duplicate columns : {col_duplicate_count}</h5>",
                unsafe_allow_html=True)

    def fire(self):
        self.data_handler()
        self.fetch_data()
        self.column_overview()
        self.null_overview()
        self.duplicates_overview()

def app():
    app = Overview('Overview', 'assets/overview_bg.jpg', '#9ffff')
    app.fire()