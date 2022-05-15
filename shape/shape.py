from math import sqrt

class Circle:

    def __init__(self, cent, rad):
        self.centre = cent
        self.radius = rad

    def __contains__(self, point):
        distance = sqrt((self.centre[0]-point[0])**2+(self.centre[1]-point[1])**2)
        return distance<self.radius

