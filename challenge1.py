import pandas as pd
import numpy as np


students = ["Ali", "Hamza", "Zara", "Omar"]
scores   = [85, 92, 78, 88]

print(students)
print(scores)



#Turn these into a dictionary called results with keys "Name" and "Score".

results = { 
    "name" : ["Ali", "Hamza", "Zara", "Omar"], "score" : [85, 92, 78, 88] 
    }

#Convert results into a pandas DataFrame called df

df = pd.DataFrame(results, )
print(df)

#From df, write the code to:
#a) Find the average score.

print(df["score"].mean())


#b) Return the name of the student with the highest score.
top_index = df["score"].idxmax()
top_name = df.loc[top_index, "name"]

print(top_name)
