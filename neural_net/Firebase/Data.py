from neural_net.Firebase.FirebaseData import FirebaseData
from geopy.distance import vincenty
import numpy as np

DATA_TIME_INTERVAL = 0.5

def distance(coor1, coor2):
    '''
    Returns array of distance vectors for two coordinates of form (latitude, longitude, altitude)
    :param coor1: (latitude, longitude, altitude)
    :param coor2: (latitude, longitude, altitude)
    :return: [x-distance, y-distance, z-distance]
    '''
    return [vincenty(coor1[:2], [coor2[0], coor1[1]]).meters, vincenty(coor1[:2], [coor1[0], coor2[1]]).meters, coor1[2]-coor2[2]]

class Data:
    def __init__(self):
        '''
        Initializes a Data object by fetching from the FirebaseData object
        fir_data - FirebaseData
            Wrapper for pyrebase methods
        fir_data_agg - List(List(DictValues)))
            List of information stored in firebase with the smallest
            container as a Dictionary(String:String)
        data - List(List(List)))
            List of information with the dictionary unpacked
        accel_data - List(List(List)))
            List of accel information from all sessions of the
            data collection app. Also the first accel value is discarded
            from the second list because that accel value does not have
            a reference distance
        location_reference - List(List)
            List of all starting locations from all session of the
            data collection app
        distance - List(List(List)))
            List of distances from the location_reference where the
            smallest level is [x-distance, y-distance, z-distance]. The
            first value is sacrificed because the accel data did not have
            a reference measurement.
        counter - int
            Used for the __next__ function to provide a StopIteration
            error once all values have been cycled
        '''
        self.fir_data = FirebaseData()
        self.fir_data_agg = self.fir_data.aggregate()
        self.counter = 0

        #Initialize methods
        self.fetch()
        self.physics()

    def fetch(self):
        '''
        DESCRIPTIONS OF ALL VARIABLES IN THE __INIT__ FUNCTION
        data - List(List(List)))
        accel_data - List(List(List)))
        location_reference - List(List)
        distance - List(List(List)))
        :return:
        '''
        self.data = [[[k for k in j.values()] for j in i] for i in self.fir_data_agg]
        self.accel_data = [[j[4:] for j in i][1:] for i in self.data]
        self.location_reference = [i[0][1:3]+[i[0][0]] for i in self.data]
        self.distance = [[distance(reference, j[1:3]+[j[0]]) for j in i][1:] for i, reference in zip(self.data, self.location_reference)]

    def physics(self):
        #TODO: Function should modify self.distance to remove the effects of prior accelerations so that each acceleration can be considered individually of the rest
        '''

        :return: None
        '''
        return

    def __iter__(self):
        '''
        Creates a self object that can be iterated on as well as
        restarts the local counter of the object
        :return: self
        '''
        self.counter = 0
        return self
    def __next__(self):
        '''
        Returns the next value in the accel, distance 3rd dimensional list
        :return: Tuple(numpy.ndarray, numpy.ndarray)
        '''
        self.counter += 1
        if self.counter - 1 >= len(self.data):
            raise StopIteration
        else:
            return (np.array(self.accel_data[self.counter-1]), np.array(self.distance[self.counter-1]))
