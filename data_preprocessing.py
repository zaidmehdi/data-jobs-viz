import random

import pandas as pd
import numpy as np



def generate_age(experience_level):
    if experience_level == "SE":
        return int(np.random.normal(loc=40, scale=5))
    elif experience_level == "EX":
        return int(np.random.normal(loc=52.5, scale=5))
    elif experience_level == "MI":
        return int(np.random.normal(loc=30, scale=5))
    elif experience_level == "EN":
        return int(np.random.normal(loc=21.5, scale=2.5))
    else:
        return None


def generate_gender(salary):
    male_mean, male_std = 80000, 15000
    female_mean, female_std = 60000, 15000

    if np.random.rand() < 0.5:
        return "Male" if salary > np.random.normal(male_mean, male_std) else "Female"
    else:
        return "Female" if salary < np.random.normal(female_mean, female_std) else "Male"


def generate_working_hour_means(df):
    country_codes_list = df.company_location.unique()
    distribution_mean = {}
    for country in country_codes_list:
        distribution_mean[country] = np.random.uniform(35, 50)

    return distribution_mean


def generate_working_hours(df, distribution_mean: dict):
    for country_code, mean in distribution_mean.items():
        mask = df['company_location'] == country_code
        num_records = mask.sum()

        standard_dev = random.randint(1, 5)
        working_hours = np.random.normal(
            loc=mean, scale=standard_dev, size=num_records)
        df.loc[mask, "weekly_hours"] = working_hours

    return df


def generate_data(df_salaries:pd.DataFrame) -> pd.DataFrame:
    distribution_mean = generate_working_hour_means(df_salaries)
    df_salaries = generate_working_hours(df_salaries, distribution_mean)
    df_salaries['age'] = df_salaries['experience_level'].apply(generate_age)
    df_salaries['gender'] = df_salaries['salary_in_usd'].apply(generate_gender)

    return df_salaries


def group_job_titles(df_salaries:pd.DataFrame):
    top_job_titles = df_salaries['job_title'].value_counts().nlargest(4).index
    df_salaries['job_title_grouped'] = df_salaries['job_title'].apply(
        lambda x: x if x in top_job_titles else 'Other')
    
    return df_salaries


def preprocess_data(df_salaries:pd.DataFrame):
    df_salaries = group_job_titles(df_salaries)

    return df_salaries


def main():
    df_salaries = pd.read_csv("data/ds_salaries.csv")
    df_salaries = generate_data(df_salaries)
    df_salaries = preprocess_data(df_salaries)

    df_salaries.to_csv("data/df_salaries.csv", index=False)


if __name__ == "__main__":
    main()