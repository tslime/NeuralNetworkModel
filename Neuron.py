import os
import sys
import math
import random
import numpy as np

class Neuron:
    
    def __init__(self,w:[],b:float):
        self.weights = w
        self.bias = b


    def linear_transform(self,inputs:[],n):
        if len(inputs) < len(n.weights):
            print("Error: missing inputs")
        else:
            if len(inputs) > len(n.weights):
                print("Error: Too many inputs \n")
            else:
                t = np.dot(inputs,n.weights) + b

        return t
    
    def sigmoid(self,v):
        return (1/(1+np.exp(-v)))
 
    

"""Testing"""

"""
weight = 3*[None]
inp = 3*[None]

for a in range(len(weight)):
    weight[a] = a+2

for b in range(len(inp)):
    inp[b] = b+1

nr = Neuron(weight,2)

print("The linear transform of this neuron is: ",nr.linear_transform(inp,nr))
print()
print("And its output is: ",nr.sigmoid(nr.linear_transform(inp,nr)))


print()
"""