# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:32:54 2020

@author: Isaac
"""
# Program to display the Fibonacci sequence up to n-th term

import timeit
import numba
import numpy as np
from numba import njit
import time

@njit
def fibonacci_njit(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
            print("Fibonacci sequence upto",nterms,":")
            print(n1)
    else:
        while count < nterms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


def fibonacci(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
            print("Fibonacci sequence upto",nterms,":")
            print(n1)
    else:
        while count < nterms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            

#    timeit.timeit("fibonacci(1000)", number = 100, globals = globals())
#    timeit.timeit("fibonacci_njit(1000)", number = 100, globals = globals())

