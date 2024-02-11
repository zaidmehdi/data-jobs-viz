from dash import dash, dcc, html
import pandas as pd
import plotly.express as px

from plots import boxplot_salary_gender_job_title



def main():
    df_salaries = pd.read_csv("data/df_salaries.csv")

    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Which Job should I choose?'),
        dcc.Graph(
            id='boxplot',
            figure=boxplot_salary_gender_job_title(df_salaries)
        )
    ])

    app.run_server(debug=True)



if __name__ == '__main__':
    main()