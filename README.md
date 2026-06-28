# Markova Chain

Discrete-time Markov chain simulation tools with both **stationary** and **non-stationary (time-varying)** transition matrices, implemented in Python with NumPy.

## Contents

| File | Description |
|------|-------------|
| `markov_chain.py` | Core module with `simulate_stationary()`, `simulate_non_stationary()`, and `print_distribution()` |
| `notebooks/markova-chain.ipynb` | Example: stationary Markov chain — 6-state system evolved over 3 steps |
| `notebooks/Non_Stationary_markov_chain.ipynb` | Example: time-varying Markov chain — weather model (Sunny / Cloudy / Rainy) with different transition matrices at each step |

## Usage

```python
from markov_chain import simulate_stationary, print_distribution
import numpy as np

P = np.array([
    [0.3, 0.3, 0.2, 0.1, 0.05, 0.05],
    [0.2, 0.4, 0.3, 0.05, 0.0, 0.05],
    [0.2, 0.3, 0.4, 0.0, 0.0, 0.1],
    [0.3, 0.0, 0.0, 0.4, 0.1, 0.2],
    [0.1, 0.1, 0.0, 0.1, 0.6, 0.1],
    [0.1, 0.3, 0.3, 0.1, 0.0, 0.2],
])

pi_0 = np.array([1, 0, 0, 0, 0, 0])
history = simulate_stationary(P, pi_0, steps=3)
print_distribution(history)
```

Non-stationary example:

```python
P1 = np.array([[0.8, 0.15, 0.05], [0.3, 0.6, 0.1], [0.2, 0.4, 0.4]])
P2 = np.array([[0.5, 0.4, 0.1],  [0.1, 0.7, 0.2], [0.1, 0.5, 0.4]])
P3 = np.array([[0.4, 0.4, 0.2],  [0.2, 0.4, 0.4], [0.1, 0.3, 0.6]])

history = simulate_non_stationary(
    np.array([0, 0, 1]),
    [P1, P2, P3],
)
print_distribution(history, state_names=["Sunny", "Cloudy", "Rainy"])
```

## Requirements

- Python ≥ 3.10
- NumPy
