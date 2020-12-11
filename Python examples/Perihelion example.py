# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:45:01 2020

@author: Isaac
"""

## Perihelion

from einsteinpy.plotting import StaticGeodesicPlotter
from einsteinpy.examples import perihelion
import timeit
from numba import jit
from numba import njit



def perihelion_procession():
    a = StaticGeodesicPlotter()
    a.animate(perihelion(), interval=2)
    a.show()
    
    
    
@jit   
def perihelion_procession_jit():
    a = StaticGeodesicPlotter()
    a.animate(perihelion(), interval=2)
    a.show()    


timeit.timeit("perihelion_procession()", number = 2, globals = globals())
timeit.timeit("perihelion_procession_jit()", number = 2, globals = globals())




#a = StaticGeodesicPlotter()
#a.animate(perihelion(), interval=2)
#a.show()