import numpy as np

def init():
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5], [0.2,0.4,0.6]])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['W3'] = np.array([[0.1,0.3], [0.2,0.4]])
    network['b1'] = np.array([[0.1,0.2,0.3]])
    network['b2'] = np.array([[0.1,0.2]])
    network['b3'] = np.array([[0.1,0.2]])

    return network

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def identity_function(x):
    return x

def forward(network,x,problem):
    W1, W2, W3 = network['W1'],network['W2'],network['W3']
    b1, b2, b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    if(problem == 'classification'):
        y = softmax(a3)
    else:
        y = identity_function(a3)
    return y

network = init()
x = np.array([1.0,0.5])
# if problem is classification
y1 = forward(network,x,'classification')
print(y1)
# if problem is regression
y2 = forward(network,x,'regression')
print(y2)