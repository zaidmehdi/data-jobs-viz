import pandas as pd
import plotly.express as px


def boxplot_salary_gender_job_title(df_salaries:pd.DataFrame):
    fig = px.box(df_salaries, x='job_title_grouped', y='salary_in_usd', 
                 color='gender', title='Boxplot of Salary by Gender and Job Type')
    fig.update_layout(
        xaxis=dict(title='Job Type', tickfont=dict(size=10)),
        yaxis=dict(title='Salary (USD)', tickfont=dict(size=10)),
        legend_title='Gender',
        showlegend=True,
        margin=dict(t=50, b=50, l=50, r=50))
    fig.update_xaxes(title_standoff=10)
    fig.update_yaxes(title_standoff=10)

    return fig


def histogram_salary_company_size(df_salaries:pd.DataFrame):
    fig = px.histogram(df_salaries, x='salary_in_usd', color='company_size', 
                   histnorm='percent', barmode='overlay', title='Histogram of Salaries by Company Size')
    fig.update_layout(
        xaxis=dict(title='Salary (USD)', tickfont=dict(size=10)),
        yaxis=dict(title='Percentage', tickfont=dict(size=10)),
        legend_title='Company Size',
        showlegend=True,
        margin=dict(t=50, b=50, l=50, r=50))
    fig.update_xaxes(title_standoff=10)
    fig.update_yaxes(title_standoff=10)

    return fig


def histogram_weekly_hours_seniority_level(df_salaries:pd.DataFrame):
    fig = px.histogram(df_salaries, x='weekly_hours', color='company_location',
                       title='Weekly Working Hours Distribution by Company Location',
                       barmode='overlay', histnorm='percent', facet_row="remote_ratio")
    
    fig.update_layout(
        xaxis=dict(title='Weekly Working Hours', tickfont=dict(size=10)),
        yaxis=dict(title='Percentage', tickfont=dict(size=10)),
        legend_title='Country',
        showlegend=True,
        margin=dict(t=50, b=50, l=50, r=50))
    fig.update_xaxes(title_standoff=10)
    fig.update_yaxes(title_text='Percentage', title_standoff=10)
    fig.update_layout(height=800)
    
    return fig


def heatmap_median_salary(df_salaries:pd.DataFrame):
    median_salaries = df_salaries.groupby('company_location')['salary_in_usd'].median().reset_index()

    fig = px.choropleth(median_salaries, 
                    locations='company_location', 
                    color='salary_in_usd', 
                    color_continuous_scale=px.colors.sequential.Blues,
                    range_color=(0, median_salaries['salary_in_usd'].max()),
                    labels={'salary_in_usd': 'Median Salary (USD)'}
                   )
    fig.update_layout(
        title_text="Median Salary by Country",
        margin=dict(t=50, b=50, l=50, r=50),
        geo=dict(
            showcoastlines=True)
            )

    return fig


def main():
    df_salaries = pd.read_csv("data/df_salaries.csv")
    fig = heatmap_median_salary(df_salaries)
    fig.show()


if __name__ == "__main__":
    main()