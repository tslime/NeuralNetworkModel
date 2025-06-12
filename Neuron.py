import os
import sys
import math
import random
import numpy as np

class Neuron:
    
    def __init__(self,num_weights):
        self.weights = num_weights*[None]
        for i in range(num_weights):
            self.weights[i] = random.uniform(-1,1)
        
        self.bias = random.uniform(-1,1)


    def linear_transform(self,inputs:[],n):
        if len(inputs) < len(n.weights):
            print("Error: missing inputs")
        else:
            if len(inputs) > len(n.weights):
                print("Error: Too many inputs \n")
            else:
                t = np.dot(inputs,n.weights) + n.bias

        return t
    
    def sigmoid(self,v):
        return (1/(1+np.exp(-v)))

    def tanh(self,v):
        return (np.exp(v) - np.exp(-v))/(np.exp(v) + np.exp(-v))
    
    def relu(self,v):
        return max(0,v)

    def leakyRelu(self,v,alpha):
        if v > 0:
            return v
        else:
            return alpha*v  

    

"""Testing"""


inp = 3*[None]

for a in range(len(inp)):
    inp[a] = a+1


nr = Neuron(len(inp))

print("The linear transform of this neuron is: ",nr.linear_transform(inp,nr))
print()
print("And its output is: ",nr.leakyRelu(nr.linear_transform(inp,nr),0.01))


print()
