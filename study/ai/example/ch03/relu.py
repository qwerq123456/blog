import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)


x = np.arange(-5.0, 5.0, 0.1)
relu = relu(x)
plt.plot(x,relu, label = "relu")
plt.ylim(-0.1,1.1)
plt.legend()
plt.show()