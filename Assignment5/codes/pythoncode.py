
#Q:-	 We now assume that p = 0.6 and we wish to find n such that the probability that k
#   is between 0.59n and 0.61n is at least 0.98
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
print("2* G(.01*math.sqrt(13254/.24)-1=",2*G(.01*math.sqrt(13254/.24))-1)

   


plt.grid()
X=np.linspace(0,5,100)
Y=[G(x) for x in X]
plt.plot(X,Y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()
