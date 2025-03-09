import math

# Line class
class Line:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def distance(self):
        # find out distance of the line
        y_diff_square = (self.source.y - self.destination.y)**2
        x_diff_square = (self.source.x - self.destination.x)**2
        return (math.sqrt(x_diff_square + y_diff_square))
        
    def slope(self):
        # slope of the line
        return  (self.source.y - self.destination.y)/(self.source.x - self.destination.x)
