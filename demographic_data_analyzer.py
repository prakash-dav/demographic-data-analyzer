import pandas as pd
import numpy as np

def load_data():
    # CSV फाइल का पाथ दें
    df = pd.read_csv('adult.data.csv')
    return df

def race_count(df):
    return df['race'].value_counts()

def average_age_of_men(df):
    return df[df['sex'] == 'Male']['age'].mean().round(1)

def percentage_with_bachelors(df):
    total_people = len(df)
    bachelors_count = len(df[df['education'] == "Bachelors"])
    percentage = (bachelors_count / total_people) * 100
    return round(percentage, 1)

def higher_lower_education_rich(df):
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)
    return higher_education_rich, lower_education_rich


def min_work_hours(df):
    return df['hours-per-week'].min()

def rich_percentage_min_workers(df):
    min_hours = min_work_hours(df)
    num_min_workers = df[df['hours-per-week'] == min_hours].shape[0]
    rich_min_workers = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')].shape[0]
    return round((rich_min_workers / num_min_workers) * 100, 1)

def country_with_highest_earning(df):
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max() * 100, 1)
    return highest_earning_country, highest_earning_country_percentage

def most_popular_occupation_in_india(df):
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation = india_high_earners['occupation'].value_counts().idxmax()
    return most_popular_occupation

def main():
    df = load_data()
    
    print("Ans 1. People of each race are represented:\n", race_count(df))
    print("Ans 2. Average Age of Men:", average_age_of_men(df))
    print("Ans 3. Percentage of people who have a Bachelor's degree:", percentage_with_bachelors(df))
    
    higher_edu_rich, lower_edu_rich = higher_lower_education_rich(df)
    print(f"Ans 4. Percentage of people with advanced education: {higher_edu_rich}%")
    print(f"Ans 5. Percentage of people without advanced education: {lower_edu_rich}%")
    
    print("Ans 6. Minimum number of hours a person works per week:", min_work_hours(df))
    print("Ans 7. Percentage of Rich among Minimum Workers:", rich_percentage_min_workers(df))
    
    highest_country, highest_percentage = country_with_highest_earning(df)
    print(f"Ans 8. Country with Highest Earning >50K: {highest_country} ({highest_percentage}%)")

    popular_occupation = most_popular_occupation_in_india(df)
    print("Ans 9. The most popular occupation for those earning >50K in India is:", popular_occupation)



if __name__ == "__main__":
    main()




