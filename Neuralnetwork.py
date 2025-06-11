import os
import sys
import random
import numpy as np

from Neuron import Neuron

class Neuralnetwork:
    WEIGHTS1 = [1,2]
    WEIGHTS2 = [3,4]
    WEIGHTS3 = [5,6]

    def __init__(self,mlayers:[],outlayers:int):
        self.layers = (len(mlayers) + 1)*[None]
        self.layers_number = len(mlayers) + 1
            
        """Middle layers"""
        k = 0
        a = 0
        while a < len(mlayers):
            self.layers[k] = mlayers[a]*[None]
            b = 0
            while b < mlayers[a]:
                self.layers[k][b] = Neuron(self.WEIGHTS2,4)
                b = b + 1
            
            a = a + 1
            k = k + 1
            
         
        """Output layer"""
        self.layers[k] = outlayers*[None]
        for x in range(outlayers):
            self.layers[k][x] = Neuron(self.WEIGHTS3,4)



    def feedforward(self,inputs:[]):
        if self.NN.layers_number == 0:
            print("There are no neurons \n")
        else:
            i = 0
            output = (self.NN.layers_number - 1)*[None]
            while i < self.NN.layers_number:
                

""" Testing """

print("test \n")

nn = Neuralnetwork([2,2],1)

for x in range(nn.layers_number):
    print("Layer ",x," ",nn.layers[x],end=" \n")

print()