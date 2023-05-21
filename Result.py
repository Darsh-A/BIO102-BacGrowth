import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt',delimiter=',')

diameters = data[:, 0]
number_of_colonies = data[:,3]

plt.plot(diameters, number_of_colonies, 'o')
plt.xlabel("Number of Colonies")
plt.ylabel("Diameter of Colonies")
plt.title("Number of Colonies vs Diameter of Colonies")
plt.minorticks_on()
plt.grid()
plt.savefig('media\images\Result\Result.png')
plt.show()