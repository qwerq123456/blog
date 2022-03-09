#2.5.2 XOR 게이트 까지 구현

import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    temp = np.sum(w*x) + b
    if temp <=0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    temp = np.sum(w*x) + b
    if temp <=0:
        return 0
    else :
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.3
    temp = np.sum(w*x) + b
    if temp <=0 :
        return 0
    else :
         return 1

def XOR(x1,x2):
    return AND(NAND(x1,x2),OR(x1,x2))

# print(XOR(0,0))
# print(XOR(1,0))
# print(XOR(0,1))
# print(XOR(1,1))