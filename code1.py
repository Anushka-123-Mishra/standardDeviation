#1. import csv
#2. read the contents of the csv and remove the headers fromthe data>
#3.calculate the total marks of all the students in the classroomand find the total number of students>
#4. the formula (Sum of Marks of all the students/Total Students)>

import csv

with open('class1.csv', newline='') as fileObject:
    reader = csv.reader(fileObject)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))
#Note that when printing, we areconverting the mean from float type tostring type with the str() method.Float types are 
#numbers having adecimal value. In Python, we have tomake sure to convert integers or floats as string.


#X Coordinate should be thenumber of students, and theY Coordinate should be thenumber of marks obtained.
#1. import the plotly and pandaslibrary>
#2. read the csv file using Pandas
#3. create a scatter plot with Xcoordinate as the StudentNumber and Y Coordinateas the Marks>
#4. display the graph>
#5. One thing, that is different in this codefrom the previous one is that we are also displaying the line of average inour graph with the following code

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                       y="Marks"
           )
fig.update_layout(shapes=[
   dict(
     type= 'line',
     y0= mean, y1= mean,
     x0= 0, x1= total_entries
   )
])

#To make both the graphs consistentbwith each other, we will add thebfollowing line 
fig.update_yaxes(rangemode="tozero")


fig.show()