"""
Define a class which descibes one point in a 2d platform
and provide the method to move one point to anther place
and the method to calculate the distance between two points
"""


from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        Initialization

        :params x: x axis
        :params y: y axis
        """

        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def move_by(self, x_step, y_step):
        self.x = self.x + x_step
        self.y = self.y + y_step
    
    def distance_to(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()