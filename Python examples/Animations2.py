# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:04:15 2020

@author: Isaac
"""

import numpy as np
from einsteinpy.geodesic import Geodesic
from einsteinpy.plotting import StaticGeodesicPlotter

## Constant Radius Orbit
position = [4, np.pi / 3, 0.]
momentum = [0., 0.767851, 2.]
a = 0.99
end_lambda = 200.
step_size = 0.5


geod = Geodesic(
    position=position,
    momentum=momentum,
    a=a,
    end_lambda=end_lambda,
    step_size=step_size,
    return_cartesian=True,
    julia=True
)


#%matplotlib nbagg
sgpl = StaticGeodesicPlotter()
sgpl.animate(geod, interval=1)
sgpl.show()

sgpl.ani.save('animation.gif', writer='imagemagick', fps=60)


