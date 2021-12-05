import numpy as np
import os
import pandas as pd
import plotly.express as px
import streamlit as st
from templates import ST_PAGE
from wordcloud import WordCloud


class EDA(ST_PAGE):

    def load_data(self):
        self.data = pd.DataFrame({})
        if os.path.isfile('data.csv'):
            self.data = pd.read_csv('data.csv')

    def choose_feature(self):
        if len(self.data.columns) > 0:
            feature = st.selectbox("FEATURE", self.data.columns)
            st.markdown(
                f"<h3 style='text-align: center; color:{self.font};'>Feature : {feature} &nbsp;&nbsp;&nbsp; || &nbsp;&nbsp;&nbsp; Data Type : {str(self.data[feature].dtype).upper()}</h3>",
                unsafe_allow_html = True)
            self.count_null_values(feature)
            if self.data[feature].dtype == 'object':
                self.check_unique_value_distribution_for_object_data_type_features(feature)
                self.generate_word_cloud(feature)
            else:
                self.add_imp_stat_values(feature)
                self.create_line_charts(feature)
                self.create_scatter_plot(feature)
                self.create_hist_plot(feature)
                self.create_box_plot(feature)


    def validate_data_presence(self):
        if len(self.data) == 0:
            st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Upload data to visualize!</h3>",
                        unsafe_allow_html = True)

    def check_unique_value_distribution_for_object_data_type_features(self, feature):
        st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Unique value distribution</h3>",
                    unsafe_allow_html = True)
        feature_array = self.data[feature]
        if feature_array.nunique() <= 20:
            label_dist_fig = px.bar(x = feature_array.value_counts().index, y = feature_array.value_counts().values,
                                    title = f"Unique Value Distribution ({feature})")
            st.plotly_chart(label_dist_fig)
        else:
            _, mid_col, _ = st.columns(3)
            with mid_col:
                st.write(feature_array.value_counts())

    def add_imp_stat_values(self, feature):
        feature_array = np.array(self.data[feature].tolist())
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>Important Statistical Values</h3>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h5 style='text-align: center;'>Mean : {'%.3f'%np.mean(feature_array)}</h5>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h5 style='text-align: center;'>Median : {'%.3f'%np.median(feature_array)}</h5>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h5 style='text-align: center;'>Standard Deviation : {'%.3f'%np.std(feature_array)}</h5>",
            unsafe_allow_html = True)
        st.markdown(
            f"<h5 style='text-align: center;'>Variance : {'%.3f'%np.var(feature_array)}</h5>",
            unsafe_allow_html = True)

    def count_null_values(self, feature):
        if len(self.data) > 0:
            st.markdown(f"<h3 style='text-align: center; color:{self.font};'>Null values : {self.data[feature].isnull().sum()}</h3>",
                        unsafe_allow_html = True)

    def generate_word_cloud(self, feature):
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>WordCloud</h3>",
            unsafe_allow_html=True)
        feature_array = self.data[feature].tolist()
        feature_string = " ".join(feature_array)
        wordcloud_plot = WordCloud(max_font_size = 40).generate(feature_string)
        _, wc_col, _ = st.columns([0.2, 1, 1])
        with wc_col:
            st.image(wordcloud_plot.to_array(), width = 600)

    def create_line_charts(self, feature):
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>LineChart</h3>",
            unsafe_allow_html = True)
        feature_array = self.data[feature]
        line_chart_fig = px.line(x = feature_array.index, y = feature_array.values,
                                 title = f"Line-Chart ({feature})")
        st.plotly_chart(line_chart_fig, use_container_width = True)

    def create_hist_plot(self, feature):
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>Histogram : Visualize Density Distribution</h3>",
            unsafe_allow_html = True)
        feature_array = self.data[feature].tolist()
        box_plot_fig = px.histogram(feature_array,
                              title = f"Histogram ({feature})")
        st.plotly_chart(box_plot_fig, use_container_width = True)

    def create_scatter_plot(self, feature):
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>Scatter-Plot</h3>",
            unsafe_allow_html = True)
        feature_array = self.data[feature].tolist()
        scatter_plot_fig = px.scatter(x = range(len(feature_array)),
                                  y = feature_array,
                                  title=f"Spatial Data Distribution ({feature})")
        st.plotly_chart(scatter_plot_fig, use_container_width = True)

    def create_box_plot(self, feature):
        st.markdown(
            f"<h3 style='text-align: center; color:{self.font};'>Box-Plot : Visualize the outliers</h3>",
            unsafe_allow_html = True)
        feature_array = self.data[feature].tolist()
        box_plot_fig = px.box(feature_array,
                              title = f"Outlier Detection ({feature})")
        st.plotly_chart(box_plot_fig, use_container_width = True)


    def fire(self):
        self.load_data()
        self.validate_data_presence()
        self.choose_feature()

def app():
    app = EDA("Exploratory Data Analysis", "assets/green_bg.jpg","#057a24")
    app.fire()