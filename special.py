# This special simulton (green) is essentially a slightly faster hunter (7 instead of 5)
# who also gets smaller twice as fast. Once reduced to 0, the special simulton will explode
# with all of the balls it has eaten
from hunter import Hunter
import model
from prey import Prey
from blackhole import Black_Hole
from math import atan2


class Special(Hunter): 
    def __init__(self, x, y):
        self.container = set()
        self.counter = 0
        Hunter.__init__(self, x, y)
        self.set_speed(7)
    
    
    def update(self): # model
        found = model.find(lambda x: (issubclass(type(x), Prey) and self.distance(x.get_location()) < self.dist))
        
        closest = 201
        closest_obj = None
        for obj in found:
            if self.distance(obj.get_location()) < closest:
                closest = self.distance(obj.get_location())
                closest_obj = obj
        
        if closest_obj != None:
            x, y = closest_obj._x - self._x, closest_obj._y - self._y
            self._angle = atan2(y, x)
        
        self.counter += 1
        eaten = Black_Hole.update(self)
        self.container.update(eaten)
        
        for obj in eaten:
            self.change_dimension(1,1)
            self.counter = 0
        
        if self.counter == self.count:
            self.change_dimension(-2,-2)
            self.counter = 0
        
        if self._width <= 0:
            for obj in self.container:
                obj.set_location(self._x, self._y)
                model.simultons.add(obj)
            model.simultons.remove(self)
    
        self.move()
        self.wall_bounce()
    
    
    def display(self,canvas):
       canvas.create_oval(self._x-self._width / 2, self._y-self._height / 2, self._x+self._width / 2, self._y+self._height / 2, fill="green")
