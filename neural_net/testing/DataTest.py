from neural_net.Firebase.Data import Data, distance

print("Testing the data collection and splitting")
data = Data()

print(data.data)
print(data.location_reference)

print()

print("Testing Vincenty distance")
print(data.distance)