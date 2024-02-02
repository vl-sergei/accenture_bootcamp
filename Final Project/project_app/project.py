from dash import dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df_pandas = pd.read_csv('modified_data.csv')



# Create Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df_pandas['COUNTRY_REGION'].unique()],
        value='Austria',
        multi=False
    ),
    dcc.Graph(id='ratio-vac-chart'),
])

print('Please open http://127.0.0.1:8050 in browser to see the plots')   

@app.callback(
    Output('ratio-vac-chart', 'figure'),
    Input('country-dropdown', 'value')
)



def update_scatter_plot(selected_country):
    # Filter data based on user selection or other criteria
    filtered_df = df_pandas[df_pandas[('COUNTRY_REGION')] == selected_country]

    # Sort the DataFrame by 'DEATHS_PER_1000CASES_RATIO' column
    # filtered_df['DEATHS_PER_1000CASES_RATIO'] = filtered_df['DEATHS_PER_1000CASES_RATIO'].round()
    filtered_df = filtered_df.sort_values(by='DEATHS_PER_1000CASES_RATIO')
    # Create scatter plot
    fig = px.scatter(
        filtered_df, x=('DATE'), y=['DEATHS_PER_1000CASES_RATIO', 'WEEKLY_VAC_X1000', 'CASES_WEEKLY_X1000'],
        title='Vaccination and Death cases', labels=({'value': 'Cases per thousand people', 'DATE': 'Time'})
    )

    # Update x-axis range for weekly ticks
    fig.update_xaxes(
    #     range=[df_pandas['DATE'].min(), df_pandas['DATE'].max()],
    #     tickvals=pd.date_range(start=df_pandas['DATE'].min(), end=df_pandas['DATE'].max(), freq='W-MON'),
    #     tickformat='%Y-%m-%d'
        #   {'yaxis': {'title': 'Cases per thousand people'}},
          range=('2020-12-01', '2022-12-01')
    )
    
    return fig

    # print(filtered_df.info()) 

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)



