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

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_df['State_new'] = employee_df["State"].map(us_state_abbrev )

df = employee_df[["Emp ID","First_Name","Last_Name","DOB_new","SSN_New","State_new"]]

df.rename(columns = {'DOB_new':'DOB','SSN_New': 'SSN','State_new':'State'})

print(df)

filename = 'test_PyBoss.txt'
with open(filename,'w') as file_object:
    file_object.write(str(df))
df