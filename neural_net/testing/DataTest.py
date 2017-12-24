from neural_net.Firebase.Data import Data, conversion_matrix

print("Testing the data collection and splitting")
data = Data()
print(data.data)
print(data.accel_data)
print(data.loc_data)
print(data.time)


print("\n\nConversion Matrix Test for [1, 2, 3]")

print(conversion_matrix([1, 2, 3], 3))

print("\n\nTesting Conversion Matrix")

data.process()
print(data.conversion_matrices)
print(data.dis_data)
print("\n")

print("Distances")
print(data.distances[0][0],data.distances[1][0])