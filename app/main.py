import pandas as pd
import numpy as np

'''
    Requirements to perform calculation on the given data.
    1. Find employee count whose age is greated than 30.
    2. Calculate appraisals for employees:
        a. for employees with sal more than 1lakh - 10% hike.
        b. for employees with less than 1lakh - 20% hike.
    3. Find employees distributed amoung regions.
'''

def calculate_employee_appraisals(df):
    if not 'new_hike' in df.columns:
        print('Calculating new hike')
        df['new_hike'] = np.where(df['Salary']>100000, '10%', '20%')
        df['new_salary'] = np.where(df['Salary']>100000, df['Salary']*1.1, df['Salary']*1.2)
    return df

def calculate_employee_count_age_gt_30(df):
    age_list = list(df['Age in Yrs.'])
    new_age_list = [age for age in age_list if age>30]
    return len(new_age_list)

def get_employee_distribution(df):
    region_list = list(df['Region'])
    distribution_dict = {}
    for region in region_list:
        if region in distribution_dict:
            distribution_dict[region] += 1
        else:
            distribution_dict[region] = 1
    return distribution_dict


if __name__=='__main__':
    file_path = '/home/venugopal/Downloads/ins/projects/SamplePythonProject/app/employee_data.csv'
    df = pd.read_csv(file_path)
    #requirement 1
    employee_count = calculate_employee_count_age_gt_30(df)
    print('There are %s employees whose age is greater than 30' % employee_count)
    #requirement 2
    new_df = calculate_employee_appraisals(df)
    new_df.to_csv(file_path, index=False)
    #requirement 3
    employee_distribution_dict = get_employee_distribution(df)
    print(employee_distribution_dict)