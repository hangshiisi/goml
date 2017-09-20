import matplotlib.pyplot as plt

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
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.ylabel('some numbers')
plt.show() 



