# energy_transfer_simulation.py

import numpy as np
import matplotlib.pyplot as plt
from setup_simulation import setup_simulation_environment

def simulate_energy_transfer(config, f_t):
    time_steps = int((config['constants']['time_range'][1] - config['constants']['time_range'][0]) / config['constants']['time_step'])
    rho_1 = np.zeros(time_steps)
    rho_2 = np.zeros(time_steps)
    rho_1[0] = config['initial_conditions']['rho_1']
    rho_2[0] = config['initial_conditions']['rho_2']
    dt = config['constants']['time_step']

    for t in range(1, time_steps):
        time = t * dt
        f_value = f_t(time)
        rho_1[t] = rho_1[t-1] + dt * (-f_value / (1 + rho_1[t-1]))
        rho_2[t] = rho_2[t-1] + dt * (f_value / (1 + rho_2[t-1]))

    return rho_1, rho_2

if __name__ == "__main__":
    config = setup_simulation_environment()
    f_t = config['entropy_functions']['constant']
    rho_1, rho_2 = simulate_energy_transfer(config, f_t)

    time = np.linspace(0, config['constants']['time_range'][1], len(rho_1))
    plt.plot(time, rho_1, label="ρ₁ (Universe 1)")
    plt.plot(time, rho_2, label="ρ₂ (Universe 2)")
    plt.title("Energy Transfer Between Universes")
    plt.xlabel("Time")
    plt.ylabel("Energy Density ρ(t)")
    plt.legend()
    plt.show()
