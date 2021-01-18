import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np

# Assign spreadsheet filename to `file`
file = '122.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')
print(datetime.date.today())
a = datetime.date.today().day
b = datetime.date(2021,1,1).day
print(a, b)
#print(df1['том/книга'])
tasks =[]
for i in df1['том/книга']:
    tasks.append(i)
print(tasks)
series1 = np.array([7])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(len(tasks))
# [xmin, xmax, ymin, ymax]
plt.axis([0,15,-0.5,3.5])
plt.title('график производства работ')
plt.barh(2,series1,color='r')
#plt.barh(index,series2,color='b',left=5)
#plt.barh(index,series3,color='g',left=(series2+series1))
plt.yticks(index,tasks)
plt.show()