# gravitational_wave_simulation.py

import numpy as np
import matplotlib.pyplot as plt
from setup_simulation import setup_simulation_environment

def simulate_gravitational_wave(config, f_t):
    time_steps = int((config['constants']['time_range'][1] - config['constants']['time_range'][0]) / config['constants']['time_step'])
    h = np.zeros(time_steps)
    h_dot = np.zeros(time_steps)
    dt = config['constants']['time_step']

    for t in range(1, time_steps):
        time = t * dt
        f_value = f_t(time)
        h_ddot = -16 * np.pi * config['constants']['G'] / config['constants']['c']**4 * f_value
        h_dot[t] = h_dot[t-1] + dt * h_ddot
        h[t] = h[t-1] + dt * h_dot[t]

    return h

if __name__ == "__main__":
    config = setup_simulation_environment()
    f_t = config['entropy_functions']['exponential']
    h = simulate_gravitational_wave(config, f_t)

    plt.plot(np.linspace(0, config['constants']['time_range'][1], len(h)), h)
    plt.title("Gravitational Wave Dynamics")
    plt.xlabel("Time")
    plt.ylabel("Gravitational Wave Amplitude h(t)")
    plt.show()
