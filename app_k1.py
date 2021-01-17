import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import dash_table
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#df = px.data.medals_wide(indexed=True)
#df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
df = pd.read_csv('./input.csv', index_col=['user'])
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
df1 = pd.read_csv(data_url)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        html.Div([
            html.P("Heatmap in DST:"),
            dcc.Checklist(
                id='secures',
                options=[{'label': x, 'value': x}
                         for x in df.index()],
                value=df.columns.tolist(),
            )
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in df1.State.unique()],
                value='State'
            ),
            #dcc.RadioItems(
            #    id='crossfilter-yaxis-type',
            #    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            #    value='Linear',
            #    labelStyle={'display': 'inline-block'}
            #)
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),


    html.Div([
        dcc.Graph(id="graph"),
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i}
                     for i in df1.columns],
            data=df1.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        )], style={'display': 'inline-block', 'width': '49%'})
    #])
])

@app.callback(
    Output("graph", "figure"),
    [Input("secures", "value")])
def filter_heatmap(cols):
    #fig = ff.create_annotated_heatmap(df[cols], colorscale='rainbow')
    fig = px.imshow(df[cols])
    return fig

app.run_server(debug=True)


#html.Div([
'''
html.Div([
    dcc.Dropdown(
        id='crossfilter-yaxis-column',
        options=[{'label': i, 'value': i} for i in df1.state.unique()],
        value='State'
    ),
    #dcc.RadioItems(
    #    id='crossfilter-yaxis-type',
    #    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
    #    value='Linear',
    #    labelStyle={'display': 'inline-block'}
    #)
], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
'''
