from pathlib import Path
import requests

import pickle
import gzip

from matplotlib import pyplot
import numpy as np

import torch

import math

import torch.nn.functional as F

from torch import nn
 
class Mnist_Logistic(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(784, 10) / math.sqrt(784))
        self.bias = nn.Parameter(torch.zeros(10))
 
    def forward(self, xb):
        return xb @ self.weights + self.bias


class Mnist_Logistic(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = nn.Linear(784, 10)
 
    def forward(self, xb):
        return self.lin(xb)

def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1)
 
def model(xb):
    return log_softmax(xb @ weights + bias)

def nll(input, target):
    return -input[range(target.shape[0]), target].mean()
 
def accuracy(out, yb):
    preds = torch.argmax(out, dim=1)
    return (preds == yb).float().mean()

def model(xb):
    return xb @ weights + bias

def fit():
    for epoch in range(epochs):
        for i in range((n - 1) // bs + 1):
            start_i = i * bs
            end_i = start_i + bs
            xb = x_train[start_i:end_i]
            yb = y_train[start_i:end_i]
            pred = model(xb)
            loss = loss_func(pred, yb)
 
            loss.backward()
            with torch.no_grad():
                for p in model.parameters():
                    p -= p.grad * lr
                model.zero_grad()
 

loss_func = nll

DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"
 
#PATH.mkdir(parents=True, exist_ok=True)
 
URL = "http://deeplearning.net/data/mnist/"
FILENAME = "mnist.pkl.gz"
 
if not (PATH / FILENAME).exists():
        content = requests.get(URL + FILENAME).content
        (PATH / FILENAME).open("wb").write(content)

with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f)
 
pyplot.imshow(x_train[0].reshape((28, 28)), cmap="gray")
print(x_train.shape)
 
x_train, y_train, x_valid, y_valid = map(
    torch.tensor, (x_train, y_train, x_valid, y_valid)
)
n, c = x_train.shape
x_train, x_train.shape, y_train.min(), y_train.max()
print(x_train, y_train)
print(x_train.shape)
print(y_train.min(), y_train.max())
 
weights = torch.randn(784, 10) / math.sqrt(784)
weights.requires_grad_()
bias = torch.zeros(10, requires_grad=True)

bs = 64  # batch size
xb = x_train[0:bs]  # a mini-batch from x
preds = model(xb)  # predictions
preds[0], preds.shape
print(preds[0], preds.shape)

yb = y_train[0:bs]
print(loss_func(preds, yb))

print(accuracy(preds, yb))

#from IPython.core.debugger import set_trace
lr = 0.5  # learning rate
epochs = 2  # how many epochs to train for
for epoch in range(epochs):
    for i in range((n - 1) // bs + 1):
        #         set_trace()
        start_i = i * bs
        end_i = start_i + bs
        xb = x_train[start_i:end_i]
        yb = y_train[start_i:end_i]
        pred = model(xb)
        loss = loss_func(pred, yb)
 
        loss.backward()
        with torch.no_grad():
            weights -= weights.grad * lr
            bias -= bias.grad * lr
            weights.grad.zero_()
            bias.grad.zero_()

print(loss_func(model(xb), yb), accuracy(model(xb), yb))
 
loss_func = F.cross_entropy
print(loss_func(model(xb), yb), accuracy(model(xb), yb))

model = Mnist_Logistic()
print(loss_func(model(xb), yb))

with torch.no_grad():
    for p in model.parameters(): p -= p.grad * lr
    model.zero_grad()

fit()

print(loss_func(model(xb), yb))

model = Mnist_Logistic()
print(loss_func(model(xb), yb))

fit()
print(loss_func(model(xb), yb))