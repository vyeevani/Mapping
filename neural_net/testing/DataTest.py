from neural_net.Firebase.Data import Data

print("Testing the data collection and splitting")
data = Data()

print(data.data)
print(data.location_reference)

print()

print("Testing Vincenty distance")
print(data.distance)

print()

print("Testing accel data")
print(data.accel_data)

print()

print("Testing data generator")
for i in data:
    print(i)

