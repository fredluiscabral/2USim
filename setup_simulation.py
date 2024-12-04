# setup_simulation.py

import numpy as np

def initialize_constants():
    constants = {
        'G': 6.67430e-11,
        'c': 3.0e8,
        'hbar': 1.054571e-34,
        'kB': 1.380649e-23,
        'gamma': 0.05,
        'phi_0': 0.1,
        'rho_1_0': 1.0,
        'rho_2_0': 1.0,
        'time_step': 0.01,
        'time_range': [0, 100],
        'grid_points': 100
    }
    return constants

def generate_entropy_function(form, params):
    if form == 'constant':
        f0 = params.get('f0', 1.0)
        return lambda t: f0
    elif form == 'exponential':
        f0 = params.get('f0', 1.0)
        alpha = params.get('alpha', 0.1)
        return lambda t: f0 * np.exp(-alpha * t)
    elif form == 'sinusoidal':
        amplitude = params.get('amplitude', 1.0)
        omega = params.get('omega', 2 * np.pi)
        offset = params.get('offset', 0.0)
        return lambda t: amplitude * np.sin(omega * t) + offset
    elif form == 'stochastic':
        mean = params.get('mean', 0.0)
        std_dev = params.get('std_dev', 0.1)
        np.random.seed(params.get('seed', None))
        return lambda t: np.random.normal(mean, std_dev)
    else:
        raise ValueError(f"Unknown form: {form}")

def setup_simulation_environment():
    constants = initialize_constants()
    entropy_functions = {
        'constant': generate_entropy_function('constant', {'f0': 1.0}),
        'exponential': generate_entropy_function('exponential', {'f0': 1.0, 'alpha': 0.05}),
        'sinusoidal': generate_entropy_function('sinusoidal', {'amplitude': 1.0, 'omega': 0.1, 'offset': 0.5}),
        'stochastic': generate_entropy_function('stochastic', {'mean': 0.0, 'std_dev': 0.1, 'seed': 42})
    }
    initial_conditions = {
        'phi': constants['phi_0'],
        'rho_1': constants['rho_1_0'],
        'rho_2': constants['rho_2_0']
    }
    config = {
        'constants': constants,
        'entropy_functions': entropy_functions,
        'initial_conditions': initial_conditions
    }
    return config

if __name__ == "__main__":
    config = setup_simulation_environment()
    print("Simulation Environment Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")
