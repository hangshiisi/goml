import matplotlib.pyplot as plt
import numpy as np 

#example 1, straight line 
# x will be automatically generated 
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show() 


#example 2, x, y both are provided 
#
#plt.plot([1,2,3,4], [1,4,9,16])
#plt.ylabel('some numbers')
#plt.show() 


#example 3, add some format string (red circle)
#  the default string is 'b-', solid blue string
# 
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
##[xmin, xmax, ymin, ymax ]
#plt.axis([0, 6, 0, 20])
#plt.ylabel('some numbers')
#plt.show() 


#example 5, work with numpy arrays 
# plotting several lines 
# 
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show() 





