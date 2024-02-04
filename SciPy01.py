import numpy as np
import scipy as sp
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
def filler():
    print()
    print("-------------------")
    print()

a1 = np.array([3,5,7])
print(a1)
a2 = np.random.random(10)
a3 = np.random.randn(10)
print(a2, a3, sep="\n")

a6 = np.linspace(0,10,100) # 0 to 10 with 100 values 
filler()
print(a6)
a7 = np.arange(0,10,0.02) #0 to 10 with 0.02 as steps
filler()
print(a7)

filler()

def f(x):
    return x**2 * np.sin(x) / np.exp(-x)

x = np.linspace(0,10,100)
y = f(x)


#filler()
names = np.array(["Jim","Luke","Josh","Pete"])

#first_letter_J = np.vectorize(lambda s: s[0])(names) =="J" #vectorize is like a for loop, inside it a lambda function
#lambda s: strings first letter (from an array) equals "J"
first_letter_J = np.vectorize(lambda s: s[0])(names) == "J"
print(names[first_letter_J])

filler()

print("Calculus")

c1 = 2*np.random.randn(1000) + 10 # 1000 number with mean 10 and std of 2
print(np.mean(c1))
print(np.std(c1))
print(np.percentile(c1,80)) # 80% of the number are smaller then the number that it gives back

filler()
print("Derivations and Integrals")
c2 = np.linspace(0,10,100)
c3 = 1/c2**2 + np.sin(c2)
dydx = np.gradient(c3,c2) #derivative
c3_int = np.cumsum(c3) * (c2[1]-c2[0])

filler()
print("SCIPY")
filler()

def f(x):
    return (x-3)**2
res = minimize(f,2)
print(res.x)
func1 = lambda x: (x[0]-1)**2 + (x[1]-2.5)**2 #we need to minimize this
cons = ({"type":"ineq","fun":lambda x: x[0]-2*x[1]+2},
        {"type":"ineq","fun":lambda x: -x[0]-2*x[1]+6},
        {"type":"ineq","fun":lambda x: -x[0]+2*x[1]+2})
bnds = ((0,None),(0,None))
result = minimize(func1,(2,0),bounds=bnds,constraints=cons)
print(result.x)

filler()
print("Interpolation")

d1 = np.linspace(0,10,10)
d2 = d1**2 * np.sin(d1)
i1 = interp1d(d1,d2,kind='cubic')
d1_dense = np.linspace(0,10,100)
d2_dense = i1(d1_dense)

print("Curve Fitting")
x_data = np.linspace(0,10,10)
y_data = 3*x_data**2 +2
def func(x,a,b):
    return a*x**2 + b
popt,pcov = curve_fit(func,x_data,y_data,p0=(1,1))
print(popt,pcov)

