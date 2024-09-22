# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

DATA_CSV = "./task2.csv"

data = pd.read_csv(DATA_CSV)
data = data.sort_values(by="date")

app = Dash(__name__)

fig = px.line(data, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?'),

    dcc.Graph(
        id='pink-morsel-sale-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
