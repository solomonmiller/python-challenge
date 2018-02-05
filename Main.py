
import csv
import pandas as pd
import os
import numpy as np

election = "HW/election_data_1.csv"
election_df = pd.read_csv(election)
count_var = 1
election_df['Count'] = count_var

count_vote = election_df["Voter ID"].count()

count_cand = election_df["Candidate"].value_counts()

count_df = pd.DataFrame(count_cand)

count_df["pct"] = count_df['Candidate'] / count_df['Candidate'].sum()

print("Election Results")
print("- - - - - - - - -")

print("Total Votes = " + str(count_vote))
print("- - - - - - - - -")

print(count_df)
print("- - - - - - - - -")

print("The Winner is" + str(count_df.head(n=1)))
print("- - - - - - - - -")

filename = 'test.txt'
with open(filename,'w') as file_object:
    file_object.write("Election Results")
    file_object.write("- - - - - - - - -")
    file_object.write("Total Votes = " + str(count_vote))
    file_object.write("- - - - - - - - -")
    file_object.write(str(count_df))
    file_object.write("- - - - - - - - -")
    file_object.write("The Winner is" + str(count_df.head(n=1)))
    file_object.write("- - - - - - - - -")
