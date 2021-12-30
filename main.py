import csv
from collections import Counter
import pandas as pd

with open('D:\Documents\school\jr\PRIVATE\Python\Project 104\SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    weight = file_data[i][1]
    new_data.append(float(weight))


#sorting out the data
n=len(new_data)
new_data.sort()
data = Counter(new_data)


def median() :
    if n % 2 == 0:
        #getting the first median
        median1 = float(new_data[n//2])
        #getting the second median
        median2= float(new_data[n//2-1])
        median = (median1+median2)/2
    else:
        median = new_data[n//2]

    print('Median is -> ',median)


def mean():
    n= len(new_data)
    total = 0

    for x in new_data:
       total+=x

    mean= total/n

    print('Mean (Average) is -> ',mean)


def mode() :
    #creating variables for the modes
    mode_data_for_range = {
        "50-60" : 0,
        "60-70" : 0,
        "70-80" : 0
    }

    #identifying the modes
    for weight, occurence in data.items():
        if 50 < float(weight) <60:
            mode_data_for_range["50-60"]+=occurence
        elif 60 < float(weight) <70:
            mode_data_for_range["60-70"]+=occurence
        elif 70 < float(weight) <80:
            mode_data_for_range["70-80"]+=occurence

    #finding the highest number of occurences
    mode_range, mode_occurrence= 0,0

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")

def main():
    mean()
    median()
    mode()

main()