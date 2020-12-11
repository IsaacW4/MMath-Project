# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:01:02 2020

@author: Isaac
"""

import timeit
import numba
import numpy as np
from numba import njit
import time




@njit
def question_1(x):
    """
    Solution to question 1 goes here
    """
    A = np.array([[1.0, 3.0, 4.0], [4.0, 5.0, 6.0], [1.0, 2.0, 3.0]])
    return np.linalg.matrix_power(A, x)



def question_1a(x):
    """
    Solution to question 1 goes here
    """
    A = np.array([[1.0, 3.0, 4.0], [4.0, 5.0, 6.0], [1.0, 2.0, 3.0]])
    return np.linalg.matrix_power(A, x)



timeit.timeit("question_1(1000)", number = 100, globals = globals())
timeit.timeit("question_1a(1000)", number = 100, globals = globals())