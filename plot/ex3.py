import matplotlib.pyplot as plt
import numpy as np 

#example 1, control line properties  
#  line have many attributes that you ca set: linewidth, dash style, 
#      antializase, etc. a few different ways to do so: 
#       1) use keyword args, plt.plt(x, y, linewidth=2.0)
#       2) setter methods of a Line2D instance. 
#              line, = plt.plot(x, y, '=')
#              line.set_antialiased(False)
#       3) setp function 
#  


def f(t): 
	return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.2)

plt.figure(1)
#number of rows, columns, and figures 
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')


plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show() 





