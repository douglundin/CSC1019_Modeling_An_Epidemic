import matplotlib.pyplot as plt
import numpy as np


def km_model(init_vals, params, t):
    x_0, y_0, z_0 = init_vals
    x, y, z = [x_0], [y_0], [z_0]
    l, k = params
    dt = t[2] - t[1]  # Assumes constant time steps
    for t_ in t[:-1]:
        next_x = x[-1] - (k * x[-1] * y[-1]) * dt
        next_y = y[-1] + (k * x[-1] * y[-1] - l * y[-1]) * dt
        next_z = z[-1] + (l * next_y) * dt
        x.append(next_x)
        y.append(next_y)
        z.append(next_z)

    return np.stack([x, y, z]).T


init_vals = [999, 1, 0]
params = [1e-1, 1e-3]
t_max = 100
dt = 0.1
t = np.linspace(0, t_max, int(t_max/dt))
km_results = km_model(init_vals, params, t)
# Plot results
plt.figure(figsize=(12,8))
plt.plot(km_results)
plt.legend(['Susceptible', 'Sick', 'Recovered'])
plt.xlabel('Time Steps')
plt.show()
