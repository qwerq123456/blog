import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def step_function(x) :
    return np.array(x>0, dtype = np.int)

def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)
sig = sigmoid(x)
step = step_function(x)
relu = relu(x)
plt.plot(x,sig,label = "sigmoid")
plt.plot(x,step,label = "step")
plt.plot(x,relu, label = "relu")
plt.ylim(-0.1,1.1)
plt.legend()
plt.show()