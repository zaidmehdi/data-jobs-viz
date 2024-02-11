import pandas as pd
import plotly.express as px



def boxplot_salary_gender_job_title(df_salaries:pd.DataFrame):
    fig = px.box(df_salaries, x='job_title_grouped', y='salary_in_usd', 
                 color='gender', title='Boxplot of Salary by Gender and Job Type')
    fig.update_layout(
        xaxis=dict(title='Job Type'),
        yaxis=dict(title='Salary (USD)'),
        legend_title='Gender',
        showlegend=True)

    return fig


def main():
    df_salaries = pd.read_csv("data/df_salaries.csv")
    fig = boxplot_salary_gender_job_title(df_salaries)
    fig.show()

if __name__ == "__main__":
    main()