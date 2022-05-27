import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

x=sy.Symbol("x")

f= lambda y : math.exp(-1*y**2/2)/math.sqrt(2*math.pi)

def G(x):
	y,err=quad(f,-math.inf,x)
	return y
print('\n')
plt.grid()
X=np.linspace(0,5,100)
Y=[G(x) for x in X]
plt.plot(X,Y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
