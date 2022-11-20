from dash import Dash, dcc, html, Input, Output 
import plotly.express as px
import pandas as pd

#pip install dash

path = 'accidents_chocs.csv'
df = pd.read_csv(path)


app = Dash(__name__)

app.layout = html.Div([
    html.H4("Gravité de l'accident en fonction du point de choc initial"),
    dcc.Graph(id="graph"),
    html.P("Type de choc:"),
    dcc.Dropdown(id='values',
        options=[
            'Avant gauche',
            'Avant droit',
            'Arrière gauche',
            'Côté gauche',
            'Côté droit', 
            'Arrière','Avant',
            'Arrière droit',
            'Chocs mutliples'],
        value='Avant gauche', clearable=False
    ),
    
    dcc.Dropdown(id='names',
        options=['Gravité'],
        value='Gravité', clearable=False,
        style = {'display':'None'}
    ),
    
])

 
@app.callback(
    Output("graph", "figure"), 
    Input("names", "value"),
    Input("values", "value"))
def generate_chart(names,values):
    fig = px.pie(df, values=values, names=names, hole=.3)
    return fig

app.run_server(debug = True, port = 8053)