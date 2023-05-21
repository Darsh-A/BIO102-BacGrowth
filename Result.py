import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt',delimiter=',')

diameters = data[:, 0]
number_of_colonies = data[:,3]

plt.plot(diameters, number_of_colonies, 'o')
plt.savefig('media\images\Result\Result.png')
plt.show()