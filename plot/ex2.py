import matplotlib.pyplot as plt
import numpy as np 



plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.show()



# create some data to use for the plot
# dt = 0.001
# t = np.arange(0.0, 10.0, dt)
# r = np.exp(-t[:1000]/0.05)               # impulse response
# x = np.random.randn(len(t))
# s = np.convolve(x, r)[:len(x)]*dt  # colored noise

# # the main axes is subplot(111) by default
# plt.plot(t, s)
# plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
# plt.xlabel('time (s)')
# plt.ylabel('current (nA)')
# plt.title('Gaussian colored noise')

# # this is an inset axes over the main axes
# a = plt.axes([.65, .6, .2, .2], facecolor='y')
# n, bins, patches = plt.hist(s, 400, normed=1)
# plt.title('Probability')
# plt.xticks([])
# plt.yticks([])

# # this is another inset axes over the main axes
# a = plt.axes([0.2, 0.6, .2, .2], facecolor='y')
# plt.plot(t[:len(r)], r)
# plt.title('Impulse response')
# plt.xlim(0, 0.2)
# plt.xticks([])
# plt.yticks([])

# plt.show()