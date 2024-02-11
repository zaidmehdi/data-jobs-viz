from dash import dash, dcc, html
import pandas as pd
import plotly.express as px



def boxplot_salary_gender_job_title(df_salaries:pd.DataFrame):
    fig = px.box(df_salaries, x='job_title_grouped', y='salary_in_usd', 
                 color='gender', title='Boxplot of Salary by Gender and Job Type')
    fig.update_layout(
        xaxis=dict(title='Job Type'),
        yaxis=dict(title='Salary (USD)'),
        legend_title='Gender',
        xaxis_tickangle=-45,
        showlegend=True)

    return fig

def main():
    df_salaries = pd.read_csv("data/df_salaries.csv")

    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Which Job should I choose?'),
        html.Div(children='''
            Boxplot of Salary by Gender and Job Type
        '''),
        dcc.Graph(
            id='boxplot',
            figure=boxplot_salary_gender_job_title(df_salaries)
        )
    ])

    app.run_server(debug=True)



if __name__ == '__main__':
    main()