import matplotlib.pyplot as plt 
from matplotlib.pyplot import plot, draw, show
import csv #for loading data
import numpy as np


draw()
#########  1   ############
#plt.plot([1,2,3],[4,5,6])

#plt.show()
#show graph






############# 2 #############

# draw()
# #draw() alows us to shut down 

# x = [1,2,3]

# y = [5,2,7]

# x2 = [43,32,45]
# y2 = [313,6,32]

# plt.plot(x,y, label='First') #label gives name
# plt.plot(x2,y2,label='second') 
# plt.xlabel('Px')
# plt.ylabel('Py')
# plt.title('this is 2\nthis is subtitle')
# plt.legend()
# plt.show()



########### 3 ###################

# population_ages = [42,24,45,64,22,53,3,43,45,23,24,66,32,13]

# ids = [x for x in range(len(population_ages))]
# #this is the way to put label on each, so that we can get value for x


# #plt.bar(ids, population_ages,label='pop')

# # x = [1,2,3,6,8]

# # y = [5,2,7,4,2]

# # x2 = [12,13,15,17,19]
# # y2 = [3,45,56,7,8]

# #  plt.bar(x,y, label='Bars1',color='blue') #bar for bar chart
# # plt.bar(x2,y2, label='Bar2',color='r')


# bins = [0,10,20,30,40,50,60,70,80,90,100,120,130]
# #bins for x measure
# plt.hist(population_ages,bins, histtype='bar', rwidth=0.8)



# plt.xlabel('Px')
# plt.ylabel('Py')
# plt.title('this is 2\nthis is subtitle')
# plt.legend()
# plt.show()










###########   4    #####################
#scatter plot
# x = [1,2,3,4,5,6,7]
# y =[5,4,2,5,6,7,4]





# plt.scatter(x,y, label ='skitscat', color='k', marker='*',s=150)
# #determine marker and size



# plt.xlabel('Px')
# plt.ylabel('Py')
# plt.title('this is 2\nthis is subtitle')
# plt.legend()
# plt.show()

######### 5 ###############

# days = [1,2,3,4,5]


# sleeping = [7,8,6,11,7]
# eating = [2,3,4,5,1]
# working = [7,8,5,2,2]
# playing = [8,6,4,2,13]

# plt.plot([],[],color='m', label='sleeing',linewidth=5)
# plt.plot([],[],color='c', label='eating',linewidth=5)
# plt.plot([],[],color='r', label='working',linewidth=5)
# plt.plot([],[],color='k', label='playing',linewidth=5)


# plt.stackplot(days, sleeping,eating,working,playing, colors = ['m','c','r','k'])


# plt.xlabel('Px')
# plt.ylabel('Py')
# plt.title('this is 2\nthis is subtitle')
# plt.legend()
# plt.show()





#skipped 6
########### 7 ##################
 

# x = []
# y = []


#this is without numpy

# with open('sample.txt','r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter=',')
# 	for row in plots:
# 		x.append(int(row[0]))
# 		y.append(int(row[1]))


# plt.plot(x,y,label='Load')
#




x, y = np.loadtxt('sample.txt',delimiter=',',unpack=True)
#before demiliter x after y
#unpack checks for variables wether it matches with file or not
plt.plot(x,y,label='Loaded from fi')






plt.xlabel('x')
plt.ylabel('y')
plt.title('this is 2\nthis is subtitle')
plt.legend()
plt.show()



















