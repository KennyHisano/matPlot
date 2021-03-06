import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show
from matplotlib import style

draw()

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
	xs = []
	ys = []

	for i in range(10):
		x = i
		y = random.randrange(10)

		xs.append(x)
		ys.append(y)
	return xs, ys

ax1 = fig.add_subplot(211)
#2 * 1 * select for each
ax2 = fig.add_subplot(212)


x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)


plt.show()
