## Read First
The program allows the user to create and place different types of objects, referred to as "simultons," into a simulation where they behave and interact differently.

To run the simulation, the script.py file must be executed to create the necessary view and controller modules, with the controller importing the model module.

The Mobile_Simulton class stores information on the angle and speed of mobile objects in the simulation, with methods for querying and updating this data. Prey is a base class that initializes Mobile_Simultons for all classes that produce "edible" objects. The Ball and Floater classes are subclasses of Prey that represent balls and floaters, respectively, with the former moving in straight lines and the latter moving erratically. Black_Hole is a stationary object that removes Prey objects from the simulation when their centers enter its perimeter. Pulsator is a type of Black_Hole that grows and shrinks based on whether it is eating Prey or not, and can ultimately remove itself from the simulation. Hunter is a type of Pulsator that is mobile and pursues Prey within its range of vision.

The program includes several types of buttons, such as the Ball button that places balls on the canvas, the Start button that starts the simulation, the Stop button that stops it, the Step button that advances it by one cycle, the Remove button that removes clicked objects, and the Reset button that clears the simulation. Additionally, there are buttons to place different types of objects on the canvas, such as the Floater button, the Black_Hole button, the Pulsator button, and the Hunter button.

## View
<img width="1440" alt="Screenshot 2023-02-18 at 11 32 01 AM" src="https://user-images.githubusercontent.com/10394057/219884674-25754d72-35a3-449c-a903-1ac1aa83efae.png">
