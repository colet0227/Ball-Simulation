# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
import model
from prey import Prey
import math


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self, x, y):
        self.set_location(x,y)
        Simulton.__init__(self, x=self._x, y=self._y, width=self.radius * 2, height=self.radius * 2)
    
    
    def update(self): # model
        copy_set = model.simultons.copy()
        prey = model.find(lambda x: issubclass(type(x), Prey))
        eaten = set()
        
        for obj in model.simultons:
            if obj in prey:
                if self.contains(obj):
                    eaten.add(obj)
                    copy_set.remove(obj)
        
        model.simultons = copy_set
        return eaten
    
    
    def display(self,canvas):
       canvas.create_oval(self._x-self._width / 2, self._y-self._height / 2, self._x+self._width / 2, self._y+self._height / 2, fill="black")
    
    
    def contains(self, obj):
        if type(obj) == tuple:
            return self._x - self._width/2  <= obj[0] <= self._x + self._width/2 and self._y - self._height/2 <= obj[1] <= self._y + self._height/2
        
        distance = self.distance(obj.get_location())
        return distance < self._width / 2
        
