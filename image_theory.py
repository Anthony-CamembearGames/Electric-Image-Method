import numpy as np
from scipy.constants import *


class sphere_propreties: 

    def __init__(self,x = 0,y = 0,z = 0, radius=0.01): 

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

class ChargeProprieties: 

    def __init__(self,x = 0,y = 0,z = 0, charge = 0): 

        self.x = x
        self.y = y
        self.z = z
        self.q = charge

def calculate_distance (object1, object2):
    return np.sqrt(abs(object1.x-object2.x)**2+abs(object1.y-object2.y)**2+abs(object1.z-object2.z)**2)

def potential(initial_charge, measured_point):
    return  initial_charge.q/(4*pi*epsilon_0*calculate_distance(initial_charge, measured_point))

def capacity_matrix(*args) :
    potential_matrix = np.zeros(shape=(len(args),len(args)))
    electrode_selected = 0
    for electrode in args :
        potential_matrix[electrode_selected][electrode_selected] = 1/(4*pi*epsilon_0*(electrode.radius**2))
        electrode_iterated = 0
        while electrode_iterated < len(args) :
            if electrode_iterated != electrode_selected :
                potential_matrix[electrode_selected][electrode_iterated] = 1/(4*pi*epsilon_0*calculate_distance(args[electrode_iterated], args[electrode_selected])**2)
            electrode_iterated += 1
        electrode_selected +=1
    return np.linalg.inv(potential_matrix)

