# coding: utf8
import numpy  # По некоторым причинам для используемой сборки CVXOPT под Windows
              # это оказывается важно
from cvxopt import matrix
from cvxopt.modeling import variable, op

# Три переменные
x = variable(3, 'x')

# Ограничения
mass1 = (x[0] + x[1] + x[2] <= 40)
mass2 = (x[2] <= 20)
manual3 = (8*x[1] + 2*x[2] <= 80)
# Ограничения могут использовать векторные операции
demand = (x <= matrix([35, 25, 30], tc='d'))
# Можно и так:
#demand1 = (x[0] <= 35)
#demand2 = (x[1] <= 25)
#demand3 = (x[2] <= 30)
material = (0.8*x[0] + 0.6*x[1] + 0.7*x[2] <= 50)
# Неотрицательность переменных сама собой не подразумевается
x_non_negative = (x >= 0)

problem = op(-1200*x[0] -2500*x[1] - 1400*x[2], 
             [mass1,
              mass2,
              manual3,
              demand,
              material,
              x_non_negative])
problem.solve(
              #solver='glpk'  # Если раскомментировать, то будет использоваться
                              # внешний решатель GLPK
              )

problem.status
print(problem.objective.value())
print(x.value)
