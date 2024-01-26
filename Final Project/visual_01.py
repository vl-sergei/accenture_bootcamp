import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import snowflake.connector


# connector to Snowflake
conn = snowflake.connector.connect(
    user = 'SERGEI',
    password = 'changemeP1s',
    account = 'tgdbsvg-lh06896',
    warehouse = 'COMPUTE_WH',
    database = 'KAGGLE_DATASET',
    schema = 'PUBLIC',
    role = 'ACCOUNTADMIN'
)

cur = conn.cursor()
cur.execute('SELECT * FROM MERGED_RESULT')

# Storing the data into variable
data = cur.fetchall()
vac_death = pd.DataFrame(data, columns = [x[0] for x in cur.description])
vac_death.to_csv('vac_death_data.csv', index=False)
# print(vac_death)

cur.close()
conn.close()


vac_death['DATE'] = pd.to_datetime(vac_death['DATE'])

# Create Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in vac_death['COUNTRY_REGION'].unique()],
        value='Austria',
        multi=False
    ),
    dcc.Graph(id='ratio-vac-chart'),
])

# Define callback to update the line plot based on selected country
@app.callback(
    Output('ratio-vac-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)

def update_scatter_plot(selected_country):
    # Filter data based on user selection or other criteria
    filtered_df = vac_death[vac_death['COUNTRY_REGION'] == selected_country]

    # Create scatter plot
    fig = px.scatter(
        filtered_df, x='DATE', y=['DEATHS_PER_1000CASES_RATIO', 'WEEKLY_VAC_PER1000'],
        title='Vaccination and Death cases', labels={'value': 'Cases per thousand people', 'DATE': 'Time'}
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
