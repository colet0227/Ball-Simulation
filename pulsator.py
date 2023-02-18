# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import model


class Pulsator(Black_Hole): 
    count = 30
    
    def __init__(self, x, y):
        self.counter = 0
        self.set_location(x,y)
        
        Black_Hole.__init__(self, x=self._x, y=self._y)
    
    
    def update(self): # model
        self.counter += 1
        eaten = Black_Hole.update(self)
        for obj in eaten:
            self.change_dimension(1,1)
            self.counter = 0
        
        if self.counter == self.count:
            self.change_dimension(-1,-1)
            self.counter = 0
        
        if self._width == 0:
            model.simultons.remove(self)
        
        return eaten
