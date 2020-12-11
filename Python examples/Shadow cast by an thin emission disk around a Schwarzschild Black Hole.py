#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:58:09 2020

@author: isaacwalter
"""
## This is an example based exercise on ray tracing 
## Shadow cast by an thin emission disk around a Schwarzschild Black Hole

import astropy.units as u
import numba
from numba import jit

from einsteinpy.rays import Shadow
from einsteinpy.plotting import ShadowPlotter


## This should be set to 1, however I get an error once I try to run it at exactly 1, so I run it as close to 1 as I possibly can
mass = 0.5 * u.kg
fov = 10 * u.km
# What field of view is the user expecting

@jit(parallel = True, fastmath = True)
def blackhole():
    
    shadow = Shadow(mass=mass, fov=fov, n_rays=100)

    obj = ShadowPlotter(shadow=shadow, is_line_plot=True)
    obj.plot()
    obj.show()

    obj = ShadowPlotter(shadow=shadow, is_line_plot=False)
    obj.plot()
    obj.show()