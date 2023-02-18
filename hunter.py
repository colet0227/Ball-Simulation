# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator, Mobile_Simulton):  
    dist = 200
    
    def __init__(self, x, y):
        self.randomize_angle()

        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, self._x, self._y, self._width, self._height, self._angle, 5)
    
    
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
        
        Pulsator.update(self)
        self.move()
        self.wall_bounce()