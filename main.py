import csv
import pandas as pd

rows=[]
with open('stars.csv', 'r') as f:
    df=csv.reader(f)
    for i in df:
        rows.append(i)

headings=rows[0]
data=rows[1:]

final_data=[]

for i in data:
    if float(i[2]) < 100:
        if float(i[5]) > 150 and float(i[5]) < 350:
            final_data.append(i)

print(len(final_data))
        
names=[]
distance=[]
mass=[]
radius=[]
gravity=[]

for i in final_data:
    names.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])

dataframe=pd.DataFrame(
    list(zip(names, distance, mass, radius, gravity)),
    columns=['star_name','distance','mass','radius','gravity']
)

dataframe.to_csv('output.csv')