import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import *

def plot_functions(points, function, variables, amount_of_points, domain):
    fig, axs = plt.subplots(nrows=2, ncols=len(amount_of_points), figsize = (7, 7))
    x_axis = np.linspace(domain[0], domain[1], 10000)

   

    for i, a in enumerate(points):
        for j, b in enumerate(a):
            x = []
            y = []

            for (x1, y1)  in b:
                x.append(x1)
                y.append(y1)

            axs[i][j].scatter(x, y)
            axs[i][j].plot(x_axis, function(x_axis))
            axs[i][j].plot(x_axis, var_to_poly(variables[i][j])(x_axis))
        
    plt.show()

    
