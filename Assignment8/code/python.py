import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from math import sqrt

#ṇ x=sy.Symbol("x")
p=.7

# f= lambda y : math.exp(-1*y**2/2)/math.sqrt(2*math.pi)

def G(x):
 	return p*(1-p)**(sqrt(x**2))/(1+1-p)

plt.grid()
X=np.linspace(-5,5,100)
Y=[G(x) for x in X]
plt.plot(X,Y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()
