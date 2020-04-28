import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylsheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylsheets)

colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

app.layout = html.Div(style={'backgroundColor':colors['background']}, children=[
        html.H1(
            children='Hello Dash',
            style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

        html.Div(children='Dash: A web application framework for python.',
                 style={
                    'textAlgin': 'center',
                    'color': colors['text']
                }),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                {'x': [1, 2, 3], 'y': [4, 2, 2], 'type': 'plot', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'plot', 'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font':{
                            'color': colors['text']
                        }
                    }
                }
            )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
