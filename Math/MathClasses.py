'''
Create classes to perform math functions.

Object Oriented Programming approach to math. In specific, geometry
First I will create classes for right triangles and use it to perform trigonmetry

'''
from math import *

class Triangle:
    '''
    Creates a Triangle. Parameters are optional 
    '''
    def __init__(self, hypotenuse=0, adjacent=0, opposite=0, theta_angle=0, angle=0):
        '''
        Creates Right angled Triangle object with optional parameters for side lengths and angles.
        Note that there are only 2 angle parameters. This is because right triangles always have one right angle.
        Be careful when setting Theta angle, it will be the referance angle for the triangle object.
        '''
        self.hypotenuse = hypotenuse
        self.adjacent = adjacent
        self.opposite = opposite
        self.theta = theta_angle
        self.angle = angle
        

    #Set sides methods
    def set_hypotenuse(self, h):
        '''
        Allows you manually set hypotenuse length
        '''
        assert isinstance(h, int), "Hypotenuse is not an integer"
        if h.type(int): #Trying the .type method (Object oreinted approach)
            self.hypotenuse = h
        
    def set_adjacent(self, a):
        '''
        Allows you to manually set adjacent length
        '''
        assert isinstance(a, int), "Adjacent is not an integer"
        if a is int: #Trying the 'is int' approach
            self.adjacent = a
        
    def set_opposite(self, o):
        '''
        Allows you to manually set opposite length
        '''
        assert isinstance(o, int), "Opposite is not an integer"
        if o is int:
            self.opposite = o

    #Set angles
    def set_theta(self, angle):
        '''
        Manually set the theta angle. 
        '''
        self.theta = angle
    def set_angle(self, angle):
        '''
        Manually set a second angle 
        '''
        self.angle = angle

    #Calculate sides
    def find_hypotenuse(self):
        '''
        Calculates hypotenuse 
        '''
        #NOTE: there are different cases where sides may be used. Have program check what is possible
        a = self.adjacent
        o = self.opposite
        theta = self.theta

        #Simple pythagorean thearum
        if a != 0 and o != 0:
            self.hypotenuse = sqrt(a**2 + o**2)
        #Cosine function//When Opposite is known
        if theta != 0 and a != 0:
            h = acos(theta)*a
        #Sin function//When Adjacent is known
        if theta != 0 and o != 0:
            h = asin(theta*o)

        assert isinstance(theta, int), "Theta is not an integer"
        assert isinstance(o, int), "Opposite is not an integer"
        

tri = Triangle(0,0,0,'h','d')
tri.find_hypotenuse()
