from keras.models import Sequential
from keras.layers import Dense
from Firebase.Data import Data
import numpy

data = Data()
accel_data = data.accel_data
print(accel_data)
loc_data = data.loc_data
print(loc_data)


model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(accel_data, loc_data, epochs=0, batch_size=100)

scores = model.evaluate(accel_data, loc_data)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



