# Neural Network Model

A simple, educational implementation of a feedforward neural network built from scratch in Python using NumPy.

neural test

## Overview

This project implements a customizable feedforward neural network without relying on deep learning frameworks like TensorFlow or PyTorch. It's designed to help understand the fundamental concepts of neural networks, including neuron structure, layer connections, and activation functions.

## Features

- **Custom Network Architecture**: Define networks with any number of hidden layers and neurons per layer
- **Multiple Activation Functions**: Supports sigmoid, tanh, ReLU, and Leaky ReLU
- **Softmax Output**: Includes softmax function for classification tasks
- **Pure Python Implementation**: Built using only NumPy for matrix operations

## Project Structure

- `Neuron.py` - Single neuron implementation with weights, bias, and activation functions
- `Neuralnetwork.py` - Complete neural network with multiple layers and feedforward capability

## Installation

Ensure you have Python and NumPy installed:

```bash
pip install numpy
```

## Usage

### Creating a Neural Network

```python
from Neuralnetwork import Neuralnetwork

# Create a network with:
# - 2 input features
# - 2 hidden layers (2 neurons each)
# - 1 output neuron
nn = Neuralnetwork(2, [2, 2], 1)
```

### Forward Pass

```python
# Feed inputs through the network
inputs = [1, -1]
output = nn.feedforward_sigmoid(inputs)
print("Output:", output)
```

### Using Softmax

```python
# Apply softmax to outputs for classification
probabilities = nn.softmax([2, 1, 1])
print("Probabilities:", probabilities)
```

## Neuron Class

The `Neuron` class represents a single artificial neuron with:
- Randomly initialized weights (uniform distribution between -1 and 1)
- Randomly initialized bias
- Linear transformation: `z = w·x + b`
- Multiple activation functions:
  - **Sigmoid**: `σ(z) = 1 / (1 + e^(-z))`
  - **Tanh**: `tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))`
  - **ReLU**: `max(0, z)`
  - **Leaky ReLU**: `max(αz, z)` where α is typically 0.01

## Neural Network Architecture

The `Neuralnetwork` class manages multiple layers:
1. **Input Layer**: Accepts input features
2. **Hidden Layers**: Configurable number and size
3. **Output Layer**: Produces final predictions

### Parameters

- `in_number`: Number of input features
- `mlayers_size`: List specifying the number of neurons in each hidden layer
- `outlayer_size`: Number of neurons in the output layer

## Example

```python
# XOR-like problem with 2 inputs, 2 hidden layers, 1 output
nn = Neuralnetwork(2, [2, 2], 1)

# Forward pass
result = nn.feedforward_sigmoid([1, -1])
print("Network output:", result)

# Softmax for multi-class classification
class_probs = nn.softmax([2, 1, 1])
print("Class probabilities:", class_probs)
```

## Current Limitations

- No backpropagation/training implementation yet
- Weights are randomly initialized and not updated
- No loss functions implemented
- No batch processing support

## Future Enhancements

Potential improvements for this project:
- Implement backpropagation algorithm
- Add training methods with gradient descent
- Include loss functions (cross-entropy, MSE)
- Support mini-batch training
- Add more activation functions
- Implement regularization techniques
- Add model saving/loading functionality


## Educational Purpose

This implementation is designed for learning and understanding neural network fundamentals. For production use cases, consider established frameworks like PyTorch, TensorFlow, or scikit-learn.
