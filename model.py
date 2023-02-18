import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycle_count = 0
running = False
selected = None
stepping = False

simultons = set()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#step just one update in the simulation
def step ():
    global running, cycle_count, stepping
    stepping = True
    if running:
        running = False
        
    update_all()
    stepping = False
        

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected
    selected = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if selected != None:
        if selected != 'Remove':
            eval(f"simultons.add({selected}(x,y))")
            eval(f"add({selected}(x,y))")
        else:
            new_set = set()
            
            for obj in simultons:
                if obj.contains((x, y)):
                    new_set.add(obj)
            
            for i in new_set:
                remove(i)


#add simultons to the simulation
def add(s):
    s.update()
    

# remove simultons from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    all_set = set()
    for s in simultons:
        if p(s):
            all_set.add(s)
    
    return all_set 


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count, running, stepping
    if running or stepping:
        cycle_count += 1
        for s in simultons:
            s.update()

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons/"+str(cycle_count)+" cycles")
