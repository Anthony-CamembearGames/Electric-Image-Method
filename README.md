# Electric-Image-Method

This python program calculates the electrical capacitance matrix of a set of conductive spheres. See http://en.wikipedia.org/wiki/Capacitance for more on the theory.

### Updates

12/03/2015 : Updates to the program to include the possibility to calculate the Capacitance Matrix over a conductive plane + Readme updates

### How to use

The first step is to create the set of electrodes, to do this you must give them 4 caracteristics, the x,y,z coordinates and the radius of the eletrodes.

example :

```python
import image_theory
  
# All distances are in m
  
x=5
y=5
z=3
radius = 0.1
    
electrode1 = sphere_propreties(x,y,z,radius)
```

### Roadmap : 

* Capacitance Matrix over a conductive surface [done]
* Capacitance Matrix over a dielectric surface [work in progress]
* Capacitance Matrix over a 2 layer dielectric surface with complex permitivities [work in progress]
* Capacitance Matrix over a multi-layered dielectric surface with complex permitivities [standby]

### References :

[1] Introduction to Electrodynamics (3rd Edition) (1998) by David J. Griffiths

[2] Electromagnetic Wave Theory (1985) by James R Wait  


