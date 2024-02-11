import pandas as pd

def get_frequent_company_locations(df_salaries:pd.DataFrame, min_frequency:int=10):
    mask = df_salaries['company_location'].value_counts()>=min_frequency
    company_locations = mask[mask].index.tolist()

    return company_locations

def main():
    df_salaries = pd.read_csv("data/df_salaries.csv")
    company_locations = get_frequent_company_locations(df_salaries)
    print(company_locations)

if __name__ == "__main__":
    main()