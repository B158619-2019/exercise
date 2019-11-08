import os, sys
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1,5,6,8,4,6,7,30,1,2,6,4,9,8,1])
plt.savefig("Lecture16_01.png",transparent=True)
plt.show()

numbers =[1,5,6,8,4,6,7,3,1,2,6,4,9,8,1]
plt.plot(numbers, color="green")
plt.savefig("Lecture16_02.png",transparent=True)
plt.show()

numbers =[1,5,6,8,4,6,7,3,1,2,6,4,9,8,1]
plt.plot(numbers, color="red", label="My numbers")
plt.legend(loc='upper left')
plt.savefig("Lecture16_03.png",transparent=True)
plt.show()
