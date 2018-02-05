import csv
import pandas as pd
import os
import numpy as np

employee = "HW/employee_data1.csv"
employee_df = pd.read_csv(employee)

employee_df['Last_Name'] = employee_df['Name'].str.split(' ').str.get(1)
employee_df['First_Name'] = employee_df['Name'].str.split(' ').str.get(0)
employee_df['Year'] = employee_df['DOB'].str.split('-').str.get(0)
employee_df['Month'] = employee_df['DOB'].str.split('-').str.get(1)
employee_df['Day'] = employee_df['DOB'].str.split('-').str.get(2)
employee_df['DOB_new'] = employee_df[['Month', 'Day','Year']].apply(lambda x: '/'.join(x), axis=1)
employee_df['SSN_v2'] = employee_df['SSN'].str.split('-').str.get(2)
employee_df['SSN_V3'] = '***'
employee_df['SSN_V4'] = '**'
employee_df['SSN_New'] = employee_df[['SSN_V3', 'SSN_V4','SSN_v2']].apply(lambda x: '-'.join(x), axis=1)


