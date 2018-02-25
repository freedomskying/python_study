import numpy as np
import scipy.stats as stats
import scipy.optimize as opt


def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


x_0 = np.array([0.5, 1.6, 1.1, 0.8, 1.2])
res = opt.minimize(rosen, x_0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print("Result of minimizing Rosenbrock function via Nelder-Mead Simplex algorithm:")
print(res)


# 梯度计算
def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200 * (xm - xm_m1 ** 2) - 400 * (xm_p1 - xm ** 2) * xm - 2 * (1 - xm)
    der[0] = -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])
    der[-1] = 200 * (x[-1] - x[-2] ** 2)
    return der


res = opt.minimize(rosen, x_0, method='BFGS', jac=rosen_der, options={'disp': True})
print("Result of minimizing Rosenbrock function via Broyden-Fletcher-Goldfarb-Shanno algorithm:")
print(res)
