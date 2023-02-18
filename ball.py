# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    
    def __init__(self, x, y):
        self.randomize_angle()
        self.set_location(x,y)
        
        Prey.__init__(self, x=self._x, y=self._y, width=self.radius * 2, height=self.radius * 2, angle=self._angle, speed=5)
    
    
    def update(self): # model
        self.move()
        self.wall_bounce() # model
    
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius, fill="blue")
