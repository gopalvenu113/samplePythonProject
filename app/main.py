import pandas as pd

'''
    Requirements to perform calculation on the given data.
    1. Find employee count whose age is greated than 30.
    2. Calculate appraisals for employees:
        a. for employees with sal more than 1lakh - 10% hike.
        b. for employees with less than 1lakh - 20% hike.
    3. Find employees distributed amoung regions.
'''


def calculate_employee_count_age_gt_30(df):
    age_list = list(df['Age in Yrs.'])
    new_age_list = [age for age in age_list if age>30]
    return len(new_age_list)


if __name__=='__main__':
    file_path = '/home/venugopal/Downloads/ins/projects/SamplePythonProject/app/employee_data.csv'
    df = pd.read_csv(file_path)
    employee_count = calculate_employee_count_age_gt_30(df)
    print('There are %s employees whose age is greater than 30' % employee_count)