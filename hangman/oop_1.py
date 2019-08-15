#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:14:55 2019

@author: sansuikyo
"""
import math

class Apple:
    def __init__(self, variety, flavor):
        self.variety = variety
        self.flavor = flavor
    
    def get_variety(self):
        return self.variety
    
    def get_flavor(self):
        return self.flavor
    
    def set_variety(self, variety):
        self.variety = variety
        
    def set_flavor(self, flavor):
        self.flavor =  flavor

fuji_apple = Apple("Fuji", "Sweet")
granny_smith = Apple("Granny Smith", "Sour")

print(fuji_apple.get_variety() + " apples are " + fuji_apple.get_flavor())
print(granny_smith.get_variety() + " apples are " + granny_smith.get_flavor())


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
circle1 = Circle(3)
circle2 =  Circle(7)
print("Circle of radius " + str(circle1.radius) + " has circumference of " + \
      str(circle1.get_circumference()) + " and an area of " + \
      str(circle1.get_area()))
print("Circle of radius " + str(circle2.radius) + " has circumference of " + \
      str(circle2.get_circumference()) + " and an area of " + \
      str(circle2.get_area()))
