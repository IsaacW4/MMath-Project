# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:27:06 2020

@author: Isaac
"""

import timeit
import numba
import numpy as np
from numba import njit
import time


@njit
def ident_np(x):
    return np.cos(x) ** 2 + np.sin(x) ** 2

@njit
def ident_loops(x):
    r = np.empty_like(x)
    n = float(len(x))
    for i in range(n):
        r[i] = np.cos(x[i]) ** 2 + np.sin(x[i]) ** 2
    return r


def ident_npno(x):
    return np.cos(x) ** 2 + np.sin(x) ** 2


def ident_loopsno(x):
    r = np.empty_like(x)
    n = len(x)
    for i in range(n):
        r[i] = np.cos(x[i]) ** 2 + np.sin(x[i]) ** 2
    return r



np.empty_like(1)



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


time1 = timeit.timeit("question_1(1000)", number = 100, globals = globals())
time2 = timeit.timeit("question_1a(1000)", number = 100, globals = globals())

timeit.timeit("question_1(1000)", number = 100, globals = globals())
timeit.timeit("question_1a(1000)", number = 100, globals = globals())


print("Time with numba acceleration is", time1)
print("Time with without numba acceleration is", time2)



# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
#start = time.time()
#question_1a(1000)
#end = time.time()
#print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
#start = time.time()
#question_1a(1000)
#end = time.time()
#print("Elapsed (after compilation) = %s" % (end - start))