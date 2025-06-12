import os
import sys
import random
import numpy as np

from Neuron import Neuron

class Neuralnetwork:

    def __init__(self,in_number,mlayers_size:[],outlayer_size:int):
        self.inputs_number = in_number
        self.layers_number = len(mlayers_size) + 1
        self.layers = self.layers_number*[None]
        
        
        """First middle layer"""
        self.layers[0] = mlayers_size[0]*[None]
        a = 0
        for a in range(mlayers_size[0]):
            self.layers[0][a] = Neuron(self.inputs_number)

        """Remaining middle layers"""
        k = 1
        b = 1
        while b < len(mlayers_size):
            self.layers[k] = mlayers_size[b]*[None]
            c = 0
            while c < mlayers_size[b]:
                self.layers[k][c] = Neuron(mlayers_size[b-1])
                c = c + 1
            
            b = b + 1
            k = k + 1
            
         
        """Output layer"""
        self.layers[k] = outlayer_size*[None]
        for x in range(outlayer_size):
            self.layers[k][x] = Neuron(mlayers_size[b-1])



    def feedforward_sigmoid(self,inputs:[]):
        if self.layers_number == 0:
            print("There are no neurons \n")
        else:
            if len(inputs) > self.inputs_number or len(inputs) < self.inputs_number:
                print("Wrong numbers of inputs \n")
            else:
                i = 0
                while i < self.layers_number:
                    f_outputs = (len(self.layers[i]))*[None]
                    j = 0
                    while j < len(self.layers[i]):
                        lt = self.layers[i][j].linear_transform(inputs,self.layers[i][j])
                        f_outputs[j] = self.layers[i][j].sigmoid(lt)
                        j = j + 1
                
                    inputs = f_outputs
                    i = i + 1
        

        return f_outputs

                

""" Testing """

print("test \n")

nn = Neuralnetwork(2,[2,2],1)

for x in range(nn.layers_number):
    print("Layer ",x," ",nn.layers[x],end=" \n")

print()

o_result = nn.feedforward_sigmoid([1,-1])

print("The feedforward output results are: \n",o_result)

