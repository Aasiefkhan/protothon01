import random
import os
import csv
j=1
row= [['#', 'NUM1','NUM2','NUM3','NUM4','NUM5']]
for i in range(1,3):
    k=open(f"myfile{i}.csv", "x")
    while os.stat(f"myfilekk{i}.csv").st_size< 2048:
        row.append([j,random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101)])
        j=j+1
        with open(f"myfile{i}.csv", 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(row)  