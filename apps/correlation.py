import pandas as pd
import plotly.express as px
import os
import streamlit as st
from templates import ST_PAGE


class Correlation(ST_PAGE):

    def load_data(self):
        self.data = pd.DataFrame({})
        if os.path.isfile('data.csv'):
            self.data = pd.read_csv('data.csv')

    def general_correlation(self):
        if len(self.data.columns) > 0:
            st.markdown(
                f"<h3 style='text-align: center; color:{self.font};'>Correlation Plot</h3>",
                unsafe_allow_html=True)
            corr_data = self.data.corr()
            corr_plot_fig = px.imshow(corr_data, title = "Correlation Matrix")
            st.plotly_chart(corr_plot_fig)
        else:
            st.markdown(
                f"<h3 style='text-align: center; color:{self.font};'>Upload data to visualize!</h3>",
                unsafe_allow_html=True)

    def feature_to_feature_dependecy(self):
        if len(self.data.columns) > 0:
            st.markdown(
                f"<h3 style='text-align: center; color:{self.font};'>Intra-Feature Correlation</h3>",
                unsafe_allow_html=True)
            left_check_box, right_check_box = st.columns(2)
            with left_check_box:
                feature_1 = st.selectbox("Feature-1", self.data.columns)
            with right_check_box:
                feature_2 = st.selectbox("Feature-2", reversed(self.data.columns))
            if feature_1 == feature_2:
                st.markdown(
                    f"<h5 style='text-align: center; color:{self.font};'>Both feature can not be Same!</h5>",
                    unsafe_allow_html=True)
            else:
                self.scatter_correlation(feature_1, feature_2)

    def scatter_correlation(self, feature_1, feature_2):
        st.markdown(
            f"<h5 style='text-align: center; color:{self.font};'>Correlation</h5>",
            unsafe_allow_html=True)
        scatter_plot_fig = px.scatter(self.data[feature_1], self.data[feature_2],
                                      title = f"{feature_1} vs. {feature_2}")
        st.plotly_chart(scatter_plot_fig, use_container_width = True)

    def fire(self):
        self.load_data()
        self.general_correlation()
        self.feature_to_feature_dependecy()

def app():
    app = Correlation("Correlation","assets/yellow_bg.jpg","#db5f2a")
    app.fire()