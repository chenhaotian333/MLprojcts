class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(4,2)         # Instantiate an object of type Point
q = Point(3,5)         # Make a second point

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y