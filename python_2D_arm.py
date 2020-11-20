import numpy as np
from matplotlib import pyplot as plt

plt.figure(1)
plt.ion()

l1 = 1
l2 = 1
l3 = 1

theta1 = 10
theta2 = -5
theta3 = -5

i=0
while i<60:

    p1 = [l1*np.cos(np.radians(theta1)), l1*np.sin(np.radians(theta1))]
    p2 = [p1[0] + l1*np.cos(np.radians(theta2 + theta1)), p1[1] + l1*np.sin(np.radians(theta2 + theta1))]
    p3 = [p2[0] + l1*np.cos(np.radians(theta3 + theta2 + theta1)), p2[1] + l1*np.sin(np.radians(theta3 + theta2 + theta1))]

    plt.clf()
    plt.plot([0, p1[0], p2[0], p3[0]], [0, p1[1], p2[1], p3[1]], '-*')

    theta1 = theta1 + 5
    theta2 = theta2 - 1
    theta3 = theta3 + 3
    plt.grid()
    plt.ylim([-5,5])
    plt.xlim([-5,5])
    plt.draw()
    plt.pause(0.001)
    i = i + 1

   

  

plt.ioff()
plt.show()