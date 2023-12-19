import numpy as np

def gen_spaced_points(domain, amount_of_points, input_function):
    points = []
    for n in amount_of_points:
        n_points = []
        for i in range(n):
            x_value = domain[0] + (i) * ((domain[1]-domain[0])/(n-1))
            n_points.append((x_value, input_function(x_value)))
        points.append(n_points)
    return points

def gen_rugne_points(domain, amount_of_points, input_function):
    points = []
    for n in amount_of_points:
        n_points = []
        angle = np.pi/(n-1)
        for i in range(n):
            non_adjusted_x = np.cos(np.pi - i*angle)
            adjusted_x = (non_adjusted_x*(domain[1]-domain[0])/2) + ((domain[1]-domain[0])/2)+domain[0]
            n_points.append((adjusted_x, input_function(adjusted_x)))
        points.append(n_points)
    return points

def fit_poly_function(points): # A X = Y
    n = len(points)
    X = np.zeros((n, n))
    Y = np.zeros((n, 1))

    for i, (x, y) in enumerate(points):
        for j in range(n):
            X[i][j] = x**j
        Y[i] = y

    A = np.matmul(np.linalg.inv(X), Y)

    return A

def var_to_poly(A):
    def func(x):
        s = 0
        for i, a in enumerate(A):
            s += a * x**i
        return s 
    return func