from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)

dataset = numpy.loadtxt("test_data.csv", delimiter=",")
print(type(dataset))

X = dataset[:,0:8]
print(type(X))
Y = dataset[:,8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))