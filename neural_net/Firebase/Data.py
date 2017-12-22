from Firebase.FirebaseData import FirebaseData
class Data:
    def __init__(self):
        self.fir_data = FirebaseData()
        self.data = self.fir_data.aggregate()
        self.accel_data = [i[4:] for i in self.data]
        self.loc_data = [i[0:3] for i in self.data]
        self.time = [i[4] for i in self.data]
    def refactor(self):
        #TODO: need to implement the distance changes from place to place
        pass


