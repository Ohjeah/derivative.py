import numpy as np
import matplotlib.pyplot as plt

from derivative import derivative, methods


def f(x):
    return np.sin(x)

n_points = 150
noise_amplitude = 0.02

x = np.linspace(0, 6 * np.pi, n_points)
y = f(x) + noise_amplitude * np.random.normal(size=x.shape)
y = y.reshape(-1, 1)

plt.plot(x, np.cos(x), "x--", label="f'")
for method in methods:
    y_deriv = derivative(x, y, kind=method)
    plt.plot(x, y_deriv, "o--", label=method)

plt.legend()
plt.show()
