import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly.subplots import make_subplots
import plotly.graph_objects as go


data_raw = (
    pd.read_csv("raw_dataset.csv")#Combination.csv
    #.query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

data_norm = (
    pd.read_csv("normalization.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data_norm: pd.to_datetime(data_norm["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

data_eval_7_1 = (
    pd.read_csv("evaluation_original_7_1.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)
data_eval_7_2 = (
    pd.read_csv("evaluation_original_7_2.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_14_1 = (
    pd.read_csv("evaluation_original_14_1.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_14_2 = (
    pd.read_csv("evaluation_original_14_2.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_14_7 = (
    pd.read_csv("evaluation_original_14_7.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_30_1 = (
    pd.read_csv("evaluation_original_30_1.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_30_2 = (
    pd.read_csv("evaluation_original_30_2.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

data_eval_30_7 = (
    pd.read_csv("evaluation_original_30_7.csv")
    #.query("type == 'conventional' and region == 'Albany'")
    # .sort_values(by="Date")
)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"
app.config['suppress_callback_exceptions'] = True
app.config.suppress_callback_exceptions = True


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.H2(
                    children="Raw data", className="part-title"
                ),
                html.Div([
                    html.Div(
                    children=
                    dcc.Tabs(id="tabs-raw-data-graph", value='Y-raw-graph', children=[
                        dcc.Tab(label='Y', value='Y-raw-graph'),
                        dcc.Tab(label='Oil_Close', value='Oil_Close-raw-graph'),
                        dcc.Tab(label='Gold_Close', value='Gold_Close-raw-graph'),
                        dcc.Tab(label='Volume_Top5', value='Volume_Top5-raw-graph'),
                        dcc.Tab(label='Volume_Top4', value='Volume_Top4-raw-graph'),
                        dcc.Tab(label='Volume_Top3', value='Volume_Top3-raw-graph'),
                        dcc.Tab(label='Volume_Top2', value='Volume_Top2-raw-graph'),
                        dcc.Tab(label='X9', value='X9-raw-graph'),
                        dcc.Tab(label='X8', value='X8-raw-graph'),
                        dcc.Tab(label='X7', value='X7-raw-graph'),
                        dcc.Tab(label='X6', value='X6-raw-graph'),
                        dcc.Tab(label='X5', value='X5-raw-graph'),
                        dcc.Tab(label='X4', value='X4-raw-graph'),
                        dcc.Tab(label='X3', value='X3-raw-graph'),
                        dcc.Tab(label='X2', value='X2-raw-graph'),
                        dcc.Tab(label='X1', value='X1-raw-graph'),
                    ]),
                ),
                    html.Div(id='tabs-content-raw-graph')
                ]),
                html.H2(
                    children="Normalized data", className="part-title"
                ),
                html.Div([
                    html.Div(
                    children=
                    dcc.Tabs(id="tabs-norm-data-graph", value='Y-norm-graph', children=[
                        dcc.Tab(label='Y', value='Y-norm-graph'),
                        dcc.Tab(label='Oil_Close', value='Oil_Close-norm-graph'),
                        dcc.Tab(label='Gold_Close', value='Gold_Close-norm-graph'),
                        dcc.Tab(label='Volume_Top5', value='Volume_Top5-norm-graph'),
                        dcc.Tab(label='Volume_Top4', value='Volume_Top4-norm-graph'),
                        dcc.Tab(label='Volume_Top3', value='Volume_Top3-norm-graph'),
                        dcc.Tab(label='Volume_Top2', value='Volume_Top2-norm-graph'),
                        dcc.Tab(label='X9', value='X9-norm-graph'),
                        dcc.Tab(label='X8', value='X8-norm-graph'),
                        dcc.Tab(label='X7', value='X7-norm-graph'),
                        dcc.Tab(label='X6', value='X6-norm-graph'),
                        dcc.Tab(label='X5', value='X5-norm-graph'),
                        dcc.Tab(label='X4', value='X4-norm-graph'),
                        dcc.Tab(label='X3', value='X3-norm-graph'),
                        dcc.Tab(label='X2', value='X2-norm-graph'),
                        dcc.Tab(label='X1', value='X1-norm-graph'),
                    ]),
                ),
                    html.Div(id='tabs-content-norm-graph')
                ]),
                html.H2(
                    children="Evaluation", className="part-title"
                ),
                html.Div([
                    html.Div(
                    children=
                    dcc.Tabs(id="tabs-evaluating-graph", value='mse-graph', children=[
                        dcc.Tab(label='mse', value='mse-graph'),
                        dcc.Tab(label='mae', value='mae-graph'),
                        dcc.Tab(label='rmse', value='rmse-graph'),
                        dcc.Tab(label='Deviation', value='Deviation-graph'),
                    ]),
                ),
                    html.Div([
                        dcc.Graph(id="tabs-content-evaluating-grap")
                    ])
                ],
                    className="wrapper",
                )
            ],
        )
    ]
)

#Evaluation data
@app.callback(
    Output("tabs-content-evaluating-grap", "figure"), 
    Input('tabs-evaluating-graph', 'value')
    )
def customize_width(tab):
    if tab == 'mse-graph':
        print('mse-graph')
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["mse"],
                name='Use 7 days to predict 1 day'
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["mse"],
                name='Use 7 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["mse"],
                name='Use 14 days to predict 1 day'
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["mse"],
                name='Use 14 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["mse"],
                name='Use 14 days to predict 7 day'
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["mse"],
                name='Use 30 days to predict 1 day'
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["mse"],
                name='Use 30 days to predict 2 day'
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["mse"],
                name='Use 30 days to predict 7 day'
            )
        )
        fig.update_layout(height=1200, width=1000, title_text="Side By Side Subplots")

        return fig
    elif tab == 'mae-graph':
        print('mae-graph')
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["mae"],
                name='Use 7 days to predict 1 day'
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["mae"],
                name='Use 7 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["mae"],
                name='Use 14 days to predict 1 day'
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["mae"],
                name='Use 14 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["mae"],
                name='Use 14 days to predict 7 day'
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["mae"],
                name='Use 30 days to predict 1 day'
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["mae"],
                name='Use 30 days to predict 2 day'
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["mae"],
                name='Use 30 days to predict 7 day'
            )
        )
        fig.update_layout(height=1200, width=1000, title_text="Side By Side Subplots")
    elif tab == 'rmse-graph':
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["rmse"],
                name='Use 7 days to predict 1 day'
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["rmse"],
                name='Use 7 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["rmse"],
                name='Use 14 days to predict 1 day'
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["rmse"],
                name='Use 14 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["rmse"],
                name='Use 14 days to predict 7 day'
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["rmse"],
                name='Use 30 days to predict 1 day'
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["rmse"],
                name='Use 30 days to predict 2 day'
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["rmse"],
                name='Use 30 days to predict 7 day'
            )
        )
        fig.update_layout(height=1200, width=1000, title_text="Side By Side Subplots")
    elif tab == 'Deviation-graph':
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["deviation"],
                name='Use 7 days to predict 1 day'
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["deviation"],
                name='Use 7 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["deviation"],
                name='Use 14 days to predict 1 day'
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["deviation"],
                name='Use 14 days to predict 2 day'
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["deviation"],
                name='Use 14 days to predict 7 day'
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["deviation"],
                name='Use 30 days to predict 1 day'
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["deviation"],
                name='Use 30 days to predict 2 day'
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["deviation"],
                name='Use 30 days to predict 7 day'
            )
        )
        fig.update_layout(height=1200, width=1000, title_text="Side By Side Subplots")


@app.callback(Output('tabs-content-evaluating-graph', 'figure'),
              Input('tabs-evaluating-graph', 'value'))
def render_content(tab):
    if tab == 'mse-graph':
        print("Vo day la duoc "+'mse-graph')
        return html.Div([
           dcc.Graph(
                        id="mse-chart",
                        # config={"displayModeBar": False},
                        figure={customize_width(tab)},
                    ),
        ],
        className="card")

    elif tab == 'mae-graph':
        print("Vo day la duoc "+'mae-graph')
        return html.Div([
           dcc.Graph(
                        id="mae-chart",
                        # config={"displayModeBar": False},
                        figure={customize_width(tab)},
                    ),
        ],
        className="card")
    elif tab == 'rmse-graph':
        return html.Div([
            dcc.Graph(
                        id="rmse-chart",
                        # config={"displayModeBar": False},
                        figure={customize_width(tab)},
                    ),
        ],
        className="card")
    elif tab == 'Deviation-graph':
        return html.Div([
           dcc.Graph(
                        id="Deviation-chart",
                        # config={"displayModeBar": False},
                        figure={customize_width(tab)},
                    ),
        ],
        className="card")
    

#Raw data
@app.callback(Output('tabs-content-raw-graph', 'children'),
              Input('tabs-raw-data-graph', 'value'))
def render_content(tab):
    if tab == 'Y-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Y"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X9-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X9"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X9 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X8-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X8"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X8 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X7-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X7"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X7 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X6-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X6"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X6 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X5-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X5"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X4-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X4"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X3-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X3"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X2-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X2"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X1-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["X1"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X1 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top5-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Volume_Top5"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top4-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Volume_Top4"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top3-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Volume_Top3"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top2-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Volume_Top2"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Oil_Close-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Oil_Close"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Oil_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Gold_Close-raw-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_raw["Date"].min().date(),
                                    max_date_allowed=data_raw["Date"].max().date(),
                                    start_date=data_raw["Date"].min().date(),
                                    end_date=data_raw["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="raw-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_raw["Date"],
                                    "y": data_raw["Gold_Close"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Gold_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")

@app.callback(
    Output("raw-data-chart", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
    Input('tabs-raw-data-graph', 'value')
)
def update_charts(start_date, end_date, value):
    filtered_data = data_norm.query(
        " Date >= @start_date and Date <= @end_date"
    )
    price_chart_figure = {}
    print(value)
    if value == 'Y-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Y"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X9-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X9"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X9 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X8-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X8"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X8 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X7-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X7"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X7 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X6-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X6"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X6 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X5-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X5"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X4-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X4"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X3-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X3"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X2-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X2"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X1-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X1"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X1 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top5-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top5"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top4-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top4"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top3-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top3"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top2-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top2"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Oil_Close-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Oil_Close"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Oil_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Gold_Close-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Gold_Close"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Gold_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    return price_chart_figure

#Norm data
@app.callback(Output('tabs-content-norm-graph', 'children'),
              Input('tabs-norm-data-graph', 'value'))
def render_content(tab):
    if tab == 'Y-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Y"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X9-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X9"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X9 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X8-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X8"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X8 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X7-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X7"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X7 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X6-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X6"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X6 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X5-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X5"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X4-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X4"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X3-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X3"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X2-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X2"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'X1-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["X1"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the X1 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top5-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Volume_Top5"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top4-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Volume_Top4"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top3-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Volume_Top3"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Volume_Top2-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Volume_Top2"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Volume_Top2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Oil_Close-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Oil_Close"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Oil_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
    elif tab == 'Gold_Close-norm-graph':
        return html.Div([
            html.Div(
                        children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_norm["Date"].min().date(),
                                    max_date_allowed=data_norm["Date"].max().date(),
                                    start_date=data_norm["Date"].min().date(),
                                    end_date=data_norm["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="norm-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_norm["Date"],
                                    "y": data_norm["Gold_Close"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Title name of the Gold_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
        ],
        className="card")
@app.callback(
    Output("norm-data-chart", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
    Input('tabs-norm-data-graph', 'value')
)
def update_charts(start_date, end_date, value):
    filtered_data = data_norm.query(
        " Date >= @start_date and Date <= @end_date"
    )
    price_chart_figure = {}
    print(value)
    if value == 'Y-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Y"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X9-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X9"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X9 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X8-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X8"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X8 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X7-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X7"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X7 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X6-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X6"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X6 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X5-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X5"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X4-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X4"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X3-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X3"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X2-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X2"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'X1-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X1"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the X1 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top5-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top5"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top4-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top4"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top3-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top3"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Volume_Top2-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top2"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Volume_Top2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Oil_Close-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Oil_Close"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Oil_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    elif value == 'Gold_Close-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Gold_Close"],
                    "type": "lines",
                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "Title name of the Gold_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "$", "fixedrange": True},
                "colorway": ["#17B897"],
            },
        }
    return price_chart_figure








app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
if __name__ == "__main__":
    app.run_server(debug=True)



