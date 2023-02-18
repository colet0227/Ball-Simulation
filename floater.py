# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y):
        self.randomize_angle()
        self.set_location(x,y)
        
        Prey.__init__(self, x=self._x, y=self._y, width=self.radius * 2, height=self.radius * 2, angle=self._angle, speed=5)
    
    
    def update(self): # model
        if random.random() <= .3:
            speed = 0
            while speed < 3 or speed > 7:
                speed = self._speed + random.randrange(-1, 1) * .5
            angle = self._angle + random.randrange(-1, 1) * .5
            
            self.set_speed(speed)
            self.set_angle(angle)
        
        self.move()
        self.wall_bounce() # model
    
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius, fill="red")

