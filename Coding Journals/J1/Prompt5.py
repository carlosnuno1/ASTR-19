import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1000, 2 * np.pi)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()