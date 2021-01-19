import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import numpy as np
import random

# Assign spreadsheet filename to `file`
file = '122.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

labels = ['Контрольная\nгруппа № %i' % i for i in range(1, 6)]

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')
print(datetime.date.today())
a = datetime.date(2021,1,25)
b = datetime.date(2021,1,1)
c = datetime.timedelta(days=365)
xlen = (a - b).days

fig, ax = plt.subplots()

print(df1)
tasks =[]

for i in df1['том/книга']:
    tasks.append(i)
print(tasks)
series1 = np.array(7)
leftp = df1['начало']  #.split(',')[0]
rightp = df1['конец']   #.split(',')[0]

#series2 = np.array([1,2,2,5])
#series3 = np.array([2,3,3,4])
index = np.arange(len(tasks))
# [xmin, xmax, ymin, ymax]
plt.axis([b,a,int(min(tasks)-1),int(max(tasks)+1)])
plt.title('график производства работ')
plt.ylabel("Том/Книга", fontsize=11, fontweight="bold")
colors = ['b','r', 'g', 'm', 'y','c']
start = 0
end = 0

x = [b + datetime.timedelta(days=i) for i in range((a-b).days)]


x = [mdates.date2num(item) for item in x]
print(x)
y= range(int(max(tasks)+1))



for el in range(len(index)):
    #print(type(e1[el]))
    if type(rightp[el]) == str:
        tmp = rightp[el].split(',')
        end = datetime.date(int(tmp[2]),int(tmp[1]),int(tmp[0]))
        end = mdates.date2num(end)
        if end > max(x):
            end = max(x)
        elif end < min(x):
            end = min(x)
        print(end, ' 22222222222222')
    else:
        end = mdates.date2num(a)
        print(end, ' 3333333')
    tmp = leftp[el].split(',')
    start = datetime.date(int(tmp[2]),int(tmp[1]),int(tmp[0]))
    start = mdates.date2num(start)
    print(start, ' 111111111')
    rand = random.randint(0, len(colors)) -1

    ax.barh(el, end, color=colors[rand], left=start)
    #print(e1[el], l1[el])

ax.set_yticks(index)
#ax.plot(range(len(x)))

#  Устанавливаем подписи тиков
ax.set_yticklabels(tasks,
                   fontsize = 15)
#plt.barh(index,series2,color='b',left=5)
#plt.barh(index,series3,color='g',left=(series2+series1))
#plt.plot(x,y)
#plt.yticks(index,tasks)
ax.xaxis.set_major_locator(mdates.DayLocator())
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))



plt.show()
