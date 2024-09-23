# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

DATA_CSV = "./task2.csv"

data = pd.read_csv(DATA_CSV)
data = data.sort_values(by="date")
colors = {
    "background-color": "#E0E0E0",
    "content-color": "#584A6F"
}

dash_app = Dash(__name__)

# header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "color": colors["content-color"],
        "display": "flex",
        "justify-content": "center",
    }
)

# visualized graph
def generate_figure(filtered_data):
    line_chart = px.line(filtered_data, x="date", y="sales")
    line_chart.update_layout(
        plot_bgcolor=colors["content-color"],
        paper_bgcolor=colors["background-color"],
        font_color=colors["content-color"]
    )    
    return line_chart

visualization = dcc.Graph(
    id="visualization",
    
    figure=generate_figure(data)
)

# region_picker button
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "all",
    id="region_picker",
    inline=True
)

region_picker_wrapper = html.Div([
    region_picker
], style={
    'display': 'flex',
    'justify-content': 'center',
    "background-color": colors["background-color"],
    "font-size": "150%",
    "color": colors["content-color"],
})

@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    figure = generate_figure(trimmed_data)
    return figure

dash_app.layout = html.Div(children=[
    header,
    visualization,
    region_picker_wrapper
], style={"background-color": colors["background-color"]})

if __name__ == '__main__':
    dash_app.run(debug=True)
