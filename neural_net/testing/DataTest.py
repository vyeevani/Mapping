from neural_net.Firebase.Data import Data, conversion_matrix


data = Data()
print(data.data)
print(data.accel_data)
print(data.loc_data)
print(data.time)


print("\n\nConversion Matrix Test for [1, 2, 3]")

print(conversion_matrix([1, 2, 3]))