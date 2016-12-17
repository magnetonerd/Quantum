from numpy import *
from math import factorial
from hermitepoly import *

"""
The wavefunction of the quantum harmonic oscillator:
          1
____________________  exp(-x^2 /2) H_n (x)
sqrt(2^n n! sqrt(n))
"""

def psi(n,x):
    const = 1/sqrt(2**n*factorial(n)*sqrt(pi)) #Just to clean up the return call
    return const*exp(-(x**2/2))*H(n,x)
