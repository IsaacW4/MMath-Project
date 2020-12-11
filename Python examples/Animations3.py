# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:40:24 2020

@author: Isaac
"""

import numpy as np
import astropy.units as u

from einsteinpy.plotting import StaticGeodesicPlotter
from einsteinpy.coordinates import SphericalDifferential
from einsteinpy.bodies import Body
from einsteinpy.geodesic import Geodesic
from astropy.constants import G, c


M = 6e24 * u.kg
R = (2*G*M)/(c*c)
Attractor = Body(name="BH", mass = M, parent=None)
sph_obj = SphericalDifferential(R, np.pi/2*u.rad, 0*u.rad,
                                0*u.m/u.s, 0*u.rad/u.s, (c/R)/(2*np.pi)*u.rad)
Object = Body(differential=sph_obj, parent=Attractor)
geodesic = Geodesic(body=Object, time=0 * u.s, end_lambda=1e-3, step_size=5e-8)

#%matplotlib notebook
obj = StaticGeodesicPlotter()
obj.animate(geodesic, interval=10)
obj.show()





