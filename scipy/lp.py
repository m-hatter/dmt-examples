from scipy.optimize import linprog

c = [-1200, -2500, -1400]

A_ub = [[1,   1,   1],
        [0,   0,   1],
        [0,   8,   2],
        [1,   0,   0],
        [0,   1,   0],
        [0,   0,   1],
        [0.8, 0.6, 0.7]]

b_ub = [40, 20, 80, 35, 25, 30, 50]

def print_iteration(x, **kwargs):
    print(kwargs)

print(linprog(c, A_ub, b_ub
              #,callback=print_iteration
             ))
