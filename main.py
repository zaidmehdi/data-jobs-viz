from dash import dash, dcc, html, Input, Output
import pandas as pd

from plots import boxplot_salary_gender_job_title, \
                histogram_salary_company_size, \
                histogram_weekly_hours_seniority_level
from utils import get_frequent_company_locations


app = dash.Dash(__name__)

df_salaries = pd.read_csv("data/df_salaries.csv")

app.layout = html.Div(children=[
    html.H1(children='Which Job should I choose?'),
    dcc.Graph(
        id='1',
        figure=boxplot_salary_gender_job_title(df_salaries)
    ),
    dcc.Graph(
        id='2',
        figure=histogram_salary_company_size(df_salaries)
    ),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} 
                    for country in get_frequent_company_locations(df_salaries)],
        value=['US', 'GB'],
        multi=True
    ),
    dcc.Graph(id='3')
])


@app.callback(
    Output('3', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_histogram(selected_countries):
    filtered_df = df_salaries[df_salaries['company_location'].isin(selected_countries)]
    fig = histogram_weekly_hours_seniority_level(filtered_df)

    return fig


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    main()