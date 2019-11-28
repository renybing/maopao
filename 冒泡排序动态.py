
'''
冒泡排序PYTHON'''
import random as rda
from matplotlib import pyplot as plt
a = list(range(1,30))
x =list(range(1,30))
rd.shuffle(a)
print(a)
my_list = list('34513453')

def minindex(object):
	mini = 0
	minc = 1
	while minc < len(object):
		if object[minc]<object[mini]:
			mini = minc
		minc+=1

	print(mini,object[mini])

def paixu(object):
	
	n = 1



	while n<len(object):
		m = 0 
		while m<len(object)-1:
			if object[n]<object[m]:
				object[m],object[n] = object[n],object[m]
				print(object)
				plt.bar(x,a,color = 'blue')
				plt.bar(m,object[m],color = 'orange')
				plt.pause(0.2)
				plt.cla()

				

			m+=1
		n+=1
		
		# plt.bar(x,a,color = 'orange')
		# plt.pause(0.1)
		# plt.cla()






paixu(a)
plt.bar(x,a,color = 'orange')
plt.show()
# minindex(a)
