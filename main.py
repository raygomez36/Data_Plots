import streamlit as st
import pandas as pd
from pandas import json_normalize
import plotly.express as px
import matplotlib.pyplot as mp

from Plotly import Plotlypx
from CSV import CSVFile

st.title("Data Plots")

# Upload File
df_file = st.file_uploader("Select your Local CSV file (default provided)")

cx = CSVFile

if df_file is not None:
    df_file.seek(0)
    df_file = cx.load_dataframe(df_file)
    #st.write(df_file.head())
    column_list = []
    for column_names in df_file.columns:
        column_list.append(column_names)



# if cx.is_csv(df_file):
#     df_file = pd.read_csv(df_file)
#     st.write(df_file.head())
# elif cx.is_json(df_file):
#     df_file = pd.read_json(df_file)
#     st.write(df_file.to_string())



    # column_list = []
    # for column_names in df_file.columns:
    #     column_list.append(column_names)

    plot = Plotlypx()

    selected_column = st.selectbox("What column would you like to visualize? ",
                                   df_file.columns.tolist())#column_list)

    selected_x_var = st.selectbox('What do you want the x variable to be?',
                                  df_file.columns.tolist())#column_list)

    selected_y_var = st.selectbox('What about the y?',
                                  df_file.columns.tolist())#column_list)

    selected_plot = st.selectbox("Select a Type of Plot:", ["Bar Plot", "Scatter Plot", "Line Plot", "Pie Plot"])

    #new_df = df_file.loc[selected_column]

    if selected_plot is "Scatter Plot":
        fig = plot.px_scatter(df_file, selected_x_var, selected_y_var, selected_column)
        st.plotly_chart(fig)
    elif selected_plot is "Line Plot":
        fig = plot.px_line(df_file, selected_x_var, selected_y_var, selected_column)
        st.plotly_chart(fig)
    elif selected_plot is "Bar Plot":
        fig = plot.px_bar(df_file, selected_x_var, selected_y_var, selected_column)
        st.plotly_chart(fig)
    elif selected_plot is "Pie Plot":
        fig = plot.px_pie(df_file, selected_x_var, selected_y_var, selected_column)
        st.plotly_chart(fig)



    # fig = px.scatter(df_file, x=selected_x_var, y=selected_y_var, title=f"Scatterplot of {selected_column}",
    #                  color=selected_column)  # Creating title dynamically.

    #fig = plot.px_scatter(df_file, selected_x_var, selected_y_var)
    #fig = selected_plot
    #st.plotly_chart(fig)

else:
#     # penguins_df = pd.read_csv('data/penguins.csv')
      st.popover(label='Please try to upload again!')

# species_set = set(df_file)
# column_list = []
# for column_names in df_file.columns:
#     column_list.append(column_names)
#
# selected_column = st.selectbox("What column would you like to visualize? ",
#                                column_list)
#
# selected_x_var = st.selectbox('What do you want the x variable to be?',
#                               column_list)
#
# selected_y_var = st.selectbox('What about the y?',
#                               column_list)
#
# fig = px.scatter(df_file, x=selected_x_var, y=selected_y_var, title=f"Scatterplot of {selected_column}",
#                  color=selected_column)  # Creating title dynamically.
#
# st.plotly_chart(fig)