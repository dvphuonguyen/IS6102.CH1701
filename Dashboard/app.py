import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly.subplots import make_subplots
import plotly.graph_objects as go


data_raw = (
    pd.read_csv("raw_dataset.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

data_predict_7_1 = (
    pd.read_csv("predict_1_day/7_days_1_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_14_1 = (
    pd.read_csv("predict_1_day/14_days_1_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_30_1 = (
    pd.read_csv("predict_1_day/30_days_1_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

data_predict_7_2 = (
    pd.read_csv("predict_2_days/7_days_2_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_14_2 = (
    pd.read_csv("predict_2_days/14_days_2_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_30_2 = (
    pd.read_csv("predict_2_days/30_days_2_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_14_7 = (
    pd.read_csv("predict_7_days/14_days_7_day_ALL.csv")#Combination.csv
    .assign(Date=lambda data_raw: pd.to_datetime(data_raw["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
data_predict_30_7 = (
    pd.read_csv("predict_7_days/30_days_7_day_ALL.csv")#Combination.csv
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
app.title = "Công nghệ thương mại điện tử - IS6102.CH1701"
app.config['suppress_callback_exceptions'] = True
app.config.suppress_callback_exceptions = True


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Img(src=r'assets/Logo_UIT_Web_Transparent.png', alt='UIT logo', style={'width':'80%'}),
                        ], 
                        className="center",
                    ),
                html.H1(
                    children="Công nghệ thương mại điện tử", className="header-title"
                ),
                html.H1(
                    children="IS6102.CH1701", className="header-title"
                ),
                html.Div(children=[
                    html.P(
                        children=(
                            "SV: Đặng Vũ Phương Uyên - 19520345"
                        ),
                    ),
                    html.P(
                        children=(
                            "SV: Trịnh Thị Thanh Trúc - 19521059"
                        ),
                    ),
                ],className="header-description")
                
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
                        dcc.Tab(label='Oil_Close', value='Oil_Close-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Gold_Close', value='Gold_Close-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top5', value='Volume_Top5-raw-graph'),
                        dcc.Tab(label='Volume_Top4', value='Volume_Top4-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top3', value='Volume_Top3-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top2', value='Volume_Top2-raw-graph'),
                        dcc.Tab(label='Cost per Transaction', value='X9-raw-graph'),
                        dcc.Tab(label='Number of transactions', value='X8-raw-graph'),
                        dcc.Tab(label='Number of transactions per block', value='X7-raw-graph'),
                        dcc.Tab(label='Number of unique addresses', value='X6-raw-graph'),
                        dcc.Tab(label='Average block size', value='X5-raw-graph'),
                        dcc.Tab(label='Median confirmation time', value='X4-raw-graph'),
                        dcc.Tab(label='Hash rate', value='X3-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Block mining difficulty', value='X2-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Miners’ revenue', value='X1-raw-graph',className='custom-tab',selected_className='custom-tab--selected'),
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
                        dcc.Tab(label='Oil_Close', value='Oil_Close-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Gold_Close', value='Gold_Close-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top5', value='Volume_Top5-norm-graph'),
                        dcc.Tab(label='Volume_Top4', value='Volume_Top4-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top3', value='Volume_Top3-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Volume_Top2', value='Volume_Top2-norm-graph'),
                        dcc.Tab(label='Cost per Transaction', value='X9-norm-graph'),
                        dcc.Tab(label='Number of transactions', value='X8-norm-graph'),
                        dcc.Tab(label='Number of transactions per block', value='X7-norm-graph'),
                        dcc.Tab(label='Number of unique addresses', value='X6-norm-graph'),
                        dcc.Tab(label='Average block size', value='X5-norm-graph'),
                        dcc.Tab(label='Median confirmation time', value='X4-norm-graph'),
                        dcc.Tab(label='Hash rate', value='X3-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Block mining difficulty', value='X2-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
                        dcc.Tab(label='Miners’ revenue', value='X1-norm-graph',className='custom-tab',selected_className='custom-tab--selected'),
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
                ]),
                html.H2(
                    children="BTC Price Forecasting", className="part-title"
                ),
                html.Div([
                    html.Div(
                    children=
                    dcc.Tabs(id="tabs-forecast-data-graph", value='Forecast_7_1-graph', children=[
                        dcc.Tab(label='Use 7d predict 1d', value='Forecast_7_1-graph'),
                        dcc.Tab(label='Use 7d predict 2d', value='Forecast_7_2-graph'),
                        dcc.Tab(label='Use 14d predict 1d', value='Forecast_14_1-graph'),
                        dcc.Tab(label='Use 14d predict 2d', value='Forecast_14_2-graph'),
                        dcc.Tab(label='Use 14d predict 7d', value='Forecast_14_7-graph'),
                        dcc.Tab(label='Use 30d predict 1d', value='Forecast_30_1-graph'),
                        dcc.Tab(label='Use 30d predict 2d', value='Forecast_30_2-graph'),
                        dcc.Tab(label='Use 30d predict 7d', value='Forecast_30_7-graph'),
                    ]),
                ),
                    html.Div(id='tabs-content-forecast-graph')
                ]),
            ],
            className="content"
        )
    ],
    className = "back-ground"
)
############################################################
#Raw focast
@app.callback(Output('tabs-content-forecast-graph', 'children'),
              Input('tabs-forecast-data-graph', 'value'))
def render_content(value):
    if value == 'Forecast_7_1-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_7_1["Date"].min().date(),
                                    max_date_allowed=data_predict_7_1["Date"].max().date(),
                                    start_date=data_predict_7_1["Date"].min().date(),
                                    end_date=data_predict_7_1["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_7_1["Date"],
                                    "y": data_predict_7_1["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_7_2-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_7_2["Date"].min().date(),
                                    max_date_allowed=data_predict_7_2["Date"].max().date(),
                                    start_date=data_predict_7_2["Date"].min().date(),
                                    end_date=data_predict_7_2["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_7_2["Date"],
                                    "y": data_predict_7_2["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_14_1-graph':

        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_14_1["Date"].min().date(),
                                    max_date_allowed=data_predict_14_1["Date"].max().date(),
                                    start_date=data_predict_14_1["Date"].min().date(),
                                    end_date=data_predict_14_1["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_14_1["Date"],
                                    "y": data_predict_14_1["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_14_2-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_14_2["Date"].min().date(),
                                    max_date_allowed=data_predict_14_2["Date"].max().date(),
                                    start_date=data_predict_14_2["Date"].min().date(),
                                    end_date=data_predict_14_2["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_14_2["Date"],
                                    "y": data_predict_14_2["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_14_7-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_14_7["Date"].min().date(),
                                    max_date_allowed=data_predict_14_7["Date"].max().date(),
                                    start_date=data_predict_14_7["Date"].min().date(),
                                    end_date=data_predict_14_7["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_14_7["Date"],
                                    "y": data_predict_14_7["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_30_1-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_30_1["Date"].min().date(),
                                    max_date_allowed=data_predict_30_1["Date"].max().date(),
                                    start_date=data_predict_30_1["Date"].min().date(),
                                    end_date=data_predict_30_1["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_30_1["Date"],
                                    "y": data_predict_30_1["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_30_2-graph':
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_30_2["Date"].min().date(),
                                    max_date_allowed=data_predict_30_2["Date"].max().date(),
                                    start_date=data_predict_30_2["Date"].min().date(),
                                    end_date=data_predict_30_2["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_30_2["Date"],
                                    "y": data_predict_30_2["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")
    elif value == 'Forecast_30_7-graph':  
        return html.Div([
            html.Div(
                        children=[
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data_predict_30_7["Date"].min().date(),
                                    max_date_allowed=data_predict_30_7["Date"].max().date(),
                                    start_date=data_predict_30_7["Date"].min().date(),
                                    end_date=data_predict_30_7["Date"].max().date(),
                                ),
                            ]
            ),
            dcc.Graph(
                        id="forecast-data-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_test"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'Y_test'
                                },
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_SARIMAX"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'SARIMAX Predicts'
                                },
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_LR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LR Predicts'
                                },
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_XGBR"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'XGBR Predicts'
                                },
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_LSTM"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'LSTM Predicts'
                                },
                                {
                                    "x": data_predict_30_7["Date"],
                                    "y": data_predict_30_7["Y_GRU"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                    'name': 'GRU Predicts'
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": True,
                                },
                                "colorway":  ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
                            },
                        },
                    ),
        ],
        className="card")  
    

@app.callback(
    Output("forecast-data-chart", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
    Input('tabs-forecast-data-graph', 'value')
)
def update_charts(start_date, end_date, value):
    filtered_forecast_data_7_1 = data_predict_7_1.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_7_2 = data_predict_7_2.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_14_1 = data_predict_14_1.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_14_2 = data_predict_14_2.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_14_7 = data_predict_14_7.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_30_1 = data_predict_30_1.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_30_2 = data_predict_30_2.query(
        " Date >= @start_date and Date <= @end_date"
    )
    filtered_forecast_data_30_7 = data_predict_30_7.query(
        " Date >= @start_date and Date <= @end_date"
    )
    price_chart_figure = {}
    
    if value == 'Forecast_7_1-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_7_1["Date"],
                    "y": filtered_forecast_data_7_1["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_7_2-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_7_2["Date"],
                    "y": filtered_forecast_data_7_2["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_14_1-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_14_1["Date"],
                    "y": filtered_forecast_data_14_1["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_14_2-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_14_2["Date"],
                    "y": filtered_forecast_data_14_2["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_14_7-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_14_7["Date"],
                    "y": filtered_forecast_data_14_7["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_30_1-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_30_1["Date"],
                    "y": filtered_forecast_data_30_1["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_30_2-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_30_2["Date"],
                    "y": filtered_forecast_data_30_2["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }
    elif value == 'Forecast_30_7-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_test"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                    'name': 'Y_test'
                },
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_SARIMAX"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'SARIMAX Predicts'
                },
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_LR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_XGBR"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'XGBR Predicts'
                },
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_LSTM"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'LSTM Predicts'
                },
                {
                    "x": filtered_forecast_data_30_7["Date"],
                    "y": filtered_forecast_data_30_7["Y_GRU"],
                    "type": "lines",
                    "hovertemplate": (
                        "%{y:.2f}<extra></extra>"
                    ),
                    'name': 'GRU Predicts'
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#de614b","#5ccb5f","#9988DD","#2527FF","#1099BB","#f3aacb"],
            },
        }   
    
    return price_chart_figure



############################################################

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
                name='Use 7 days to predict 1 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["mse"],
                name='Use 7 days to predict 2 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["mse"],
                name='Use 14 days to predict 1 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["mse"],
                name='Use 14 days to predict 2 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["mse"],
                name='Use 14 days to predict 7 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["mse"],
                name='Use 30 days to predict 1 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["mse"],
                name='Use 30 days to predict 2 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["mse"],
                name='Use 30 days to predict 7 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.update_layout(height=1200, title_text="Compare MSE when use x day to predict y day")

        return fig
    elif tab == 'mae-graph':
        print('mae-graph')
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["mae"],
                name='Use 7 days to predict 1 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["mae"],
                name='Use 7 days to predict 2 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["mae"],
                name='Use 14 days to predict 1 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["mae"],
                name='Use 14 days to predict 2 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["mae"],
                name='Use 14 days to predict 7 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["mae"],
                name='Use 30 days to predict 1 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["mae"],
                name='Use 30 days to predict 2 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["mae"],
                name='Use 30 days to predict 7 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.update_layout(height=1200, title_text="Compare MAE when use x day to predict y day")
        return fig
    elif tab == 'rmse-graph':
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["rmse"],
                name='Use 7 days to predict 1 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["rmse"],
                name='Use 7 days to predict 2 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["rmse"],
                name='Use 14 days to predict 1 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["rmse"],
                name='Use 14 days to predict 2 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["rmse"],
                name='Use 14 days to predict 7 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["rmse"],
                name='Use 30 days to predict 1 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["rmse"],
                name='Use 30 days to predict 2 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["rmse"],
                name='Use 30 days to predict 7 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.update_layout(height=1200, title_text="Compare RMSE when use x day to predict y day")

        return fig
    elif tab == 'Deviation-graph':
        fig = make_subplots(rows=3, cols=3)
        fig.add_trace(row=1, col=1,
            trace=go.Bar(
                x= data_eval_7_1["algo"],
                y= data_eval_7_1["deviation"],
                name='Use 7 days to predict 1 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=1, col=2,
            trace=go.Bar(
                x= data_eval_7_2["algo"],
                y= data_eval_7_2["deviation"],
                name='Use 7 days to predict 2 day',
                marker_color='#98defb', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )
        fig.add_trace(row=2, col=1,
            trace=go.Bar(
                x= data_eval_14_1["algo"],
                y= data_eval_14_1["deviation"],
                name='Use 14 days to predict 1 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=2,
            trace=go.Bar(
                x= data_eval_14_2["algo"],
                y= data_eval_14_2["deviation"],
                name='Use 14 days to predict 2 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=2, col=3,
            trace=go.Bar(
                x= data_eval_14_7["algo"],
                y= data_eval_14_7["deviation"],
                name='Use 14 days to predict 7 day',
                marker_color='#1b83dd', 
                marker_line_color='rgb(8,48,107)',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=1,
            trace=go.Bar(
                x= data_eval_30_1["algo"],
                y= data_eval_30_1["deviation"],
                name='Use 30 days to predict 1 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=2,
            trace=go.Bar(
                x= data_eval_30_2["algo"],
                y= data_eval_30_2["deviation"],
                name='Use 30 days to predict 2 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.add_trace(row=3, col=3,
            trace=go.Bar(
                x= data_eval_30_7["algo"],
                y= data_eval_30_7["deviation"],
                name='Use 30 days to predict 7 day',
                marker_color='#003380', 
                marker_line_color='#00060f',
                marker_line_width=1.5, opacity=0.6
            )
        )

        fig.update_layout(height=1200, title_text="Compare Deviation when use x day to predict y day")

        return fig
        
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Cost per Transaction attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of transactions attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of transactions per block attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of unique addresses attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Average block size attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Median confirmation time attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Hash rate attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Block mining difficulty attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Miners’ revenue attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Oil_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Gold_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
    if value == 'Y-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Y"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X9-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X9"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Cost per Transaction attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X8-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X8"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of transactions attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X7-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X7"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of transactions per block attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X6-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X6"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of unique addresses attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X5-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X5"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Average block size attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X4-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X4"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Median confirmation time attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X3-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X3"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Hash rate attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X2-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X2"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Block mining difficulty attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X1-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X1"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Miners’ revenue attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top5-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top5"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top4-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top4"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top3-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top3"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top2-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top2"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Oil_Close-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Oil_Close"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Oil_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Gold_Close-raw-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Gold_Close"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Gold_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The BTC price",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Cost per Transaction attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of transactions attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of transactions per block attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Number of unique addresses attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Average block size attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Median confirmation time attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Hash rate attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Block mining difficulty attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Miners’ revenue attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top5 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top4 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top3 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Volume_Top2 attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Oil_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
                                        "%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "The Gold_Close attribute",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "",
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
    if value == 'Y-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Y"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The BTC price",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X9-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X9"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Cost per Transaction attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X8-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X8"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of transactions attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X7-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X7"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of transactions per block attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X6-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X6"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Number of unique addresses attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X5-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X5"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Average block size attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X4-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X4"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Median confirmation time attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X3-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X3"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Hash rate attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X2-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X2"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Block mining difficulty attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'X1-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["X1"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Miners’ revenue attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top5-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top5"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top5 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top4-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top4"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top4 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top3-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top3"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top3 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Volume_Top2-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Volume_Top2"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Volume_Top2 attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Oil_Close-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Oil_Close"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Oil_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    elif value == 'Gold_Close-norm-graph':
        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["Gold_Close"],
                    "type": "lines",
                    "hovertemplate": "%{y:.2f}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "x": 0.05,
                    "xanchor": "left",
                    "text": "The Gold_Close attribute",

                },
                "xaxis": {"fixedrange": True},
                "yaxis": {"tickprefix": "", "fixedrange": True},
                "colorway": ["#2196f3"],
            },
        }
    return price_chart_figure








app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
if __name__ == "__main__":
    app.run_server(debug=True)



