# scalar_field_simulation.py

import numpy as np
import matplotlib.pyplot as plt
from setup_simulation import setup_simulation_environment

def simulate_scalar_field(config, f_t):
    time_steps = int((config['constants']['time_range'][1] - config['constants']['time_range'][0]) / config['constants']['time_step'])
    phi = np.zeros(time_steps)
    phi_dot = np.zeros(time_steps)
    phi[0] = config['initial_conditions']['phi']
    dt = config['constants']['time_step']

    for t in range(1, time_steps):
        time = t * dt
        f_value = f_t(time)
        phi_ddot = -3 * config['constants']['gamma'] * phi_dot[t-1] + f_value
        phi_dot[t] = phi_dot[t-1] + dt * phi_ddot
        phi[t] = phi[t-1] + dt * phi_dot[t]

    return phi

if __name__ == "__main__":
    config = setup_simulation_environment()
    f_t = config['entropy_functions']['sinusoidal']
    phi = simulate_scalar_field(config, f_t)

    plt.plot(np.linspace(0, config['constants']['time_range'][1], len(phi)), phi)
    plt.title("Scalar Field Dynamics")
    plt.xlabel("Time")
    plt.ylabel("Scalar Field φ(t)")
    plt.show()
