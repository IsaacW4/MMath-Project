# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:31:15 2020

@author: Isaac
"""

import numpy as np
import astropy.units as u

from einsteinpy.plotting import StaticGeodesicPlotter
from einsteinpy.coordinates import SphericalDifferential
from einsteinpy.coordinates import CartesianDifferential
from einsteinpy.bodies import Body
from einsteinpy.geodesic import Geodesic
from astropy.constants import G, c


M = 6e30 * u.kg
R = (G*M)/(c*c)
bh_obj = CartesianDifferential(0*u.m, 0*u.m, 0*u.m,
                                0*u.m/u.s, 0*u.m/u.s, 0*u.m/u.s)
Attractor = Body(name="BH", mass = M, parent=None, differential = bh_obj)
cart_obj = CartesianDifferential(-1e5*u.m, 20000*u.m, 0*u.m,
                                c, 0*u.m/u.s, 0*u.m/u.s)
Object = Body(differential=cart_obj, parent=Attractor)
geodesic = Geodesic(body=Object, time=0 * u.s, end_lambda=1e-1, step_size=5e-8)

cart_obj2 = CartesianDifferential(-1e5*u.m, -20000*u.m, 0*u.m,
                                c, 0*u.m/u.s, 0*u.m/u.s)
Object2 = Body(differential=cart_obj2, parent=Attractor)
geodesic2 = Geodesic(body=Object2, time=0 * u.s, end_lambda=1e-3, step_size=5e-8)


#%matplotlib notebook
obj = StaticGeodesicPlotter()
obj.plot(geodesic)
obj.plot(geodesic2)
obj.show()

