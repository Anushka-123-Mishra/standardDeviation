
import math



# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]



# finding mean
def calculateMean(dataInput):
    n= len(dataInput)
    total =0
    for x in dataInput:
        total += int(x)

    calculatedMean = total / n
    return calculatedMean

#getting the mean
# data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100] #list of x or y
# data=[60,61,65,63,98,99,90,95,91,96]

# squaring and getting the values
squared_list= []
for number in data:
    a = int(number) - calculateMean(data)
    a= a*a
    squared_list.append(a)

#getting sum of all the squares of the numbers calculated by getting the difference between the mean and exach individual number
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values i.e. 
# calculating mean of the sum of all the squares of the numbers calculated by getting the difference between the mean and exach individual number
result = sum/ (len(data)-1)

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print("STANDARDDEVIATION= ",std_deviation)
print("mean= ",calculateMean(data))
# print("derived using predefined function ",statistics.stdev(data))