from Firebase.FirebaseData import FirebaseData
class Data:
    def __init__(self):
        self.fir_data = FirebaseData()
        self.data = self.fir_data.aggregate()
        self.accel_data = self.data[:,0:2]
        self.loc_data = self.data[:,2:3]
print(Data().data)

