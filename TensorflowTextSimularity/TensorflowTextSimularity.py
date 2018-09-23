
import tensorflow as tf
from tensorflow import keras
import numpy as np
import io
import h5py

MAX_LENGTH = 100

model = keras.Sequential()

print("creating layers")
#Creating layers of neural network
model.add(keras.layers.Dense(64, activation = 'relu'))
model.add(keras.layers.Dense(64, activation = 'relu'))
model.add(keras.layers.Dense(2, activation = 'softmax'))

model.compile(optimizer=tf.train.AdamOptimizer(0.001), loss='mse', metrics=['mae'])

print("opening file")
d = open('data.txt')
dStr = d.read()
dIO = io.StringIO(dStr)
DatS = np.loadtxt(dIO, dtype=str, delimiter="\t", usecols = (0, 1))
x, y = DatS.shape
DatF = np.empty([x, y * MAX_LENGTH])

print("converting string to ints")
for i in range(0, x):
    for j in range(0, y):
        o = [ord(c) for c in DatS[i][j]]
        for k in range(0, len(o)):
            DatF[i][j*MAX_LENGTH + k] = o[k]

l = open('label.txt')
lStr = l.read()
lIO = io.StringIO(lStr)
Lab = np.loadtxt(lIO, dtype=int, delimiter="\t")

print("training")
model.fit(DatF, Lab, epochs=10, batch_size=32)

print("done training")
model.save('TextSimularity.h5')