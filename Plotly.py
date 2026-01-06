import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class Plotlypx:

    def __int__(self, df, x, y, c):
        self.df = df,
        self.x = x,
        self.y = y,
        self.c = c
        # color_var = color_var

    def px_scatter(self, df, x, y, c):
        return px.scatter(df, x=x, y=y, color=c)  # Creating title dynamically.

    def px_line(self, df, x, y, c):
        return px.line(df, x=x, y=y, color=c)

    def px_bar(self, df, x, y, c):
        return px.bar(df, x=x, y=y, color=c)

    def px_pie(self, df, x, y, c):
        return px.pie(df, values=x, names=y, color=c)