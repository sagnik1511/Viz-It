import matplotlib.pyplot as plt
import os
import pandas as pd
import plotly.express as px
import streamlit as st
from templates import ST_PAGE


class EDA(ST_PAGE):

    def load_data(self):
        self.data = pd.DataFrame({})
        if os.path.isfile('data.csv'):
            self.data = pd.read_csv('data.csv')

    def choose_feature(self):
        if len(self.data.columns) > 0:
            feature = st.selectbox("FEATURE",self.data.columns)
            st.markdown(
                f"<h3 style='text-align: center; color:#{self.font};'>Feature : {feature}  ||  Data Type : {str(self.data[feature].dtype).upper()}</h3>",
                unsafe_allow_html=True)
            if self.data[feature].dtype == 'object':
                self.check_unique_value_distribution_for_object_data_type_features(self.data[feature])


    def validate_data_presence(self):
        if len(self.data) == 0:
            st.markdown(f"<h3 style='text-align: center; color:#{self.font};'>Upload data to visualize!</h3>",
                        unsafe_allow_html = True)

    def check_unique_value_distribution_for_object_data_type_features(self, feature_array):
        st.markdown(f"<h3 style='text-align: center; color:#{self.font};'>Unique value distribution</h3>",
                    unsafe_allow_html=True)
        if feature_array.nunique() <= 20:
            label_dist_fig = px.bar(x = feature_array.value_counts().index, y = feature_array.value_counts().values)
            st.plotly_chart(label_dist_fig)
        else:
            _,mid_col,_ = st.columns(3)
            with mid_col:
                st.write(feature_array.value_counts())

    def count_null_values(feature):
        pass



    def fire(self):
        self.load_data()
        self.validate_data_presence()
        self.choose_feature()

def app():
    app = EDA("Exploratory Data Analysis", "assets/eda_bg.jpg",'#9ffff')
    app.fire()