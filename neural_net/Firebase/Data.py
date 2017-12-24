from neural_net.Firebase.FirebaseData import FirebaseData
import numpy as np
import math

#The time interval that the data is recorded at
DATA_TIME_INTERVAL = 0.5

def differences(distances):
    '''
    Function finds the differences between distances this will sacrifice the final data point as well
    :param distances: list of distance coordinates
    :return: a list of the differences

    >>>differences([[1, 2, 3, 4], [2, 3, 4, 5]])
    >>>[[1, 1, 1, 1]]
    '''
    for i in range(len(distances)-1):
        distances[i] = [second - first for first, second in zip(distances[i], distances[i+1])]
    return distances[:-1]

def conversion_matrix(distances, length):
    '''
    Function generates a conversion matrix that can convert d -> v
    :param distances: list of distances
    :return: list of lists
    >>>conversion_matrix([1, 2, 3])
    >>>[[8.0, 0.0, 0.0], [-16.0, 8.0, 0.0], [-16.0, -16.0, 8.0]]
    '''
    #TODO write this
    dimension = length
    conversion_matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            if j == i:
                row.append(2)
            elif j < i:
                row.append(-4)
            else:
                row.append(0)
        conversion_matrix.append(row)
        return [[j for j in i] for i in conversion_matrix]
    #return [[j/math.pow(DATA_TIME_INTERVAL, 2) for j in i] for i in conversion_matrix]
class Data:
    def __init__(self):
        self.fir_data = FirebaseData()
        self.data = [[[k for k in j.values()] for j in i] for i in self.fir_data.aggregate()]
        self.accel_data = [[j[4:] for j in i] for i in self.data]
        self.loc_data = [[j[:3] for j in i] for i in self.data]
        self.time = [[j[3] for j in i] for i in self.data]
    def process(self):
        #TODO: need to implement the distance changes from place to place
        '''
        This function process the data to provide distance differences along with also containing time differences
        '''
        self.conversion_matrices = [[conversion_matrix(j, len(i)) for j in i] for i in self.loc_data]
        self.conversion_matrices = [[np.array(j) for j in i] for i in self.conversion_matrices]
        self.dis_data = [np.array(i) for i in self.loc_data]
        length = len(self.conversion_matrices)
        self.distances = []
        for i in range(length):
            row = []
            for j in range(len(self.conversion_matrices[i])):
                row.append(np.matmul(self.conversion_matrices[i][j], self.dis_data[i]))
            self.distances.append(row)
