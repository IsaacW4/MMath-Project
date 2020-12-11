# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:49:10 2020

@author: Isaac
"""

from astropy import units as u
import numpy as np
from einsteinpy.metric import Schwarzschild
from einsteinpy.coordinates import SphericalDifferential

# Define position and velocity vectors in spherical coordinates
# Earth is at perihelion
M = 1.989e30 * u.kg  # mass of sun
distance = 147.09e6 * u.km
speed_at_perihelion = 30.29 * u.km / u.s
omega = (u.rad * speed_at_perihelion) / distance

sph_obj = SphericalDifferential(distance, np.pi / 2 * u.rad, np.pi * u.rad,
                               0 * u.km / u.s, 0 * u.rad / u.s, omega)


# Set lambda to complete an year.
# Lambda is always specified in secs
end_lambda = ((1 * u.year).to(u.s)).value
# Choosing stepsize for ODE solver to be 5 minutes
stepsize = ((5 * u.min).to(u.s)).value

obj = Schwarzschild.from_coords(sph_obj, M)
ans = obj.calculate_trajectory(
    end_lambda=end_lambda, OdeMethodKwargs={"stepsize": stepsize}, return_cartesian=True
)


ans[0].shape, ans[1].shape

r = np.sqrt(np.square(ans[1][:, 1]) + np.square(ans[1][:, 2]))
i = np.argmax(r)
(r[i] * u.m).to(u.km)


((ans[1][i][6]) * u.m / u.s).to(u.km / u.s)


xlist, ylist = ans[1][:, 1], ans[1][:, 2]
i = np.argmax(ylist)
x, y = xlist[i], ylist[i]
eccentricity = x / (np.sqrt(x ** 2 + y ** 2))
eccentricity


from einsteinpy.bodies import Body
from einsteinpy.geodesic import Geodesic
Sun = Body(name="Sun", mass=M, parent=None)
Object = Body(name="Earth", differential=sph_obj, parent=Sun)
geodesic = Geodesic(body=Object, time=0 * u.s, end_lambda=end_lambda, step_size=stepsize)
from einsteinpy.plotting import StaticGeodesicPlotter
obj = StaticGeodesicPlotter()
obj.animate(geodesic, interval=2)
obj.show()