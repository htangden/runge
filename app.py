import numpy as np
from functions import *
from plot import *

def input_function(x):
    return 1/(1 + x**2)

functions = [[], []] #first element for spaced function, second for runge functions
points = [[], []] # --||--
 
amount_of_points = [11, 41] #the different amount of points for which to approximate function
approximation_domain = [-20, 20] #values of x between which the input function will be approximated

spaced_points = gen_spaced_points(approximation_domain, amount_of_points, input_function)
runge_points = gen_rugne_points(approximation_domain, amount_of_points, input_function)

points[0] = spaced_points
points[1] = runge_points



for i, a in enumerate(points):
    for j, b in enumerate(a):
        functions[i].append(fit_poly_function(b))

plot_functions(points, input_function, functions, amount_of_points, approximation_domain)