import math

# Cylinder class
class Cylinder:
    def __init__(self,r,h):
      self.r = r
      self.h = h

    def volume(self):
        # volume = pi * r2 * h
        return math.pi * (self.r ** 2) * self.h
    
    def surface_area(self):
        # area = 2*pi*r*h
        return 2 * math.pi * self.r * self.h
   