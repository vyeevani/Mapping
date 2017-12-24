from neural_net.Firebase.FirebaseData import FirebaseData
from geopy.distance import vincenty
import numpy as np

DATA_TIME_INTERVAL = 0.5

def distance(coor1, coor2):
    return [vincenty(coor1[:2], [coor2[0], coor1[1]]).meters, vincenty(coor1[:2], [coor1[0], coor2[1]]).meters, coor1[2]-coor2[2]]

class Data:
    def __init__(self):
        self.fir_data = FirebaseData().aggregate()
        self.data = [[[k for k in j.values()] for j in i] for i in self.fir_data]
        self.location_reference = [i[0][1:3]+[i[0][0]] for i in self.data]
        self.distance = [[distance(reference, j[1:3]+[j[0]]) for j in i] for i, reference in zip(self.data, self.location_reference)]
