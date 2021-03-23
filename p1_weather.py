def euclidean_distance(data_point1, data_point2):
    d = pow(data_point1['TMAX'] - data_point2['TMAX'],2) + pow(data_point1['PRCP'] - data_point2['PRCP'],2) + pow(data_point1['TMIN'] - data_point2['TMIN'],2)
    distance = pow(d,0.5)
    return distance

def read_dataset(filename):
    f = open(filename, "r")
    data = {}
    dataset = []
    for line in f:
        # divide the line by space
        d = line.split()
        data = {'DATE': d[0], 'TMAX': float(d[2]), 'PRCP': float(d[1]), 'TMIN': float(d[3]), 'RAIN': d[4]}
        # add the dictionary to the list
        dataset.append(data)
    f.close()
    return dataset

def majority_vote(nearest_neighbors):
    for neighbor in nearest_neighbors:
        i = 0
        j = 0
        if neighbor['RAIN'] == 'TRUE':
            i = i + 1
        if neighbor['RAIN'] == 'FALSE':
            j = j + 1
    # if 'TRUE' is more than 'FALSE'
    if i >= j:
        return 'TRUE'
    else:
        return 'FALSE'

def k_nearest_neighbors(filename, test_point, k):
    datalist = read_dataset(filename)
    distancelist = []

    # read every set in the dictionary
    for data_point in datalist:
        dis = euclidean_distance(test_point, data_point)
        # add the distance with the set into the list
        distancelist.append((data_point, dis))

    # sort the list by the distance
    distancelist = sorted(distancelist, key=lambda distancelist: distancelist[1])
    # use the first k list
    neighborslist = distancelist[:k]
    points = []
    # remove the distance in the list
    for neighbors in neighborslist:
        points.append(neighbors[0])
    return majority_vote(points)