# Electric-Image-Method

This python script calculates the electrical capacitance matrix of a set of conductive spheres. See http://en.wikipedia.org/wiki/Capacitance for more on the theory.

### Updates

12/03/2015 : Updates to the program to include the possibility to calculate the Capacitance Matrix over a conductive plane + Readme updates

### How to use

The first step is to create the set of electrodes, to do this you must give them 4 caracteristics, the x,y,z coordinates and the radius.

example :

```python
import image_theory
  
# All distances are in m
  
x=5
y=5
z=3
radius = 0.1
    
electrode = sphere_propreties(x,y,z,radius)
```
Once you created a certain number of electrodes you can pass them to the capacity_matrix function, the ouput will be the capacitance matrix.

```python
import image_theory

... # Here we create the electrodes

capacitance_matrix = capacity_matrix(electrode1, electrode2, electrode3)
```
If you want to calculate the capacitance matrix over or under a plane you can use the capacity_matrix_over_conductive_interface function, but you must first create a condcutive plane with only one caracterisctic : the z value.

```python
import image_theory

z_plane = 2

plane  = PlaneProprieties(z_plane)

... # Here we create the electrodes

capacitance_matrix = capacity_matrix_over_conductive_interface(plane, electrode1, electrode2, electrode3)
```
Note that in this case you have to cheak for two things, first that all the electrodes are on the same side of the plane, then that no electrodes intersect each other or the plane


### Roadmap : 

* Capacitance Matrix over a conductive surface [done]
* Capacitance Matrix over a dielectric surface [work in progress]
* Capacitance Matrix over a 2 layer dielectric surface with complex permitivities [work in progress]
* Capacitance Matrix over a multi-layered dielectric surface with complex permitivities [standby]
* Graphical representation of the electrode system [standby]
* Custom error messages and geometry verification [standby]

### References :

[1] Introduction to Electrodynamics (3rd Edition) (1998) by David J. Griffiths

[2] Electromagnetic Wave Theory (1985) by James R Wait  


