"""Markov chain simulation tools.

Includes stationary and non-stationary (time-varying) discrete-time
Markov chains with utilities for state evolution and visualization.
"""

import numpy as np


def simulate_stationary(
    P: np.ndarray,
    pi_0: np.ndarray,
    steps: int,
) -> np.ndarray:
    """Simulate a stationary Markov chain.

    π_n = π_0 × P^n

    Parameters
    ----------
    P : (n, n) array
        Transition probability matrix (rows sum to 1).
    pi_0 : (n,) array
        Initial state distribution.
    steps : int
        Number of steps to simulate.

    Returns
    -------
    history : (steps+1, n) array
        State distributions at each time step (including t=0).
    """
    history = [pi_0]
    pi = pi_0.copy()
    for _ in range(steps):
        pi = pi @ P
        history.append(pi)
    return np.array(history)


def simulate_non_stationary(
    pi_0: np.ndarray,
    transition_matrices: list[np.ndarray],
) -> np.ndarray:
    """Simulate a non-stationary Markov chain with time-varying transitions.

    Parameters
    ----------
    pi_0 : (n,) array
        Initial state distribution.
    transition_matrices : list of (n, n) arrays
        Transition matrices P_1, P_2, ..., P_k
        where P_i governs the transition from step i-1 to step i.

    Returns
    -------
    history : (k+1, n) array
        State distributions at each time step (including t=0).
    """
    history = [pi_0]
    pi = pi_0.copy()
    for P in transition_matrices:
        pi = pi @ P
        history.append(pi)
    return np.array(history)


def print_distribution(
    history: np.ndarray,
    state_names: list[str] | None = None,
) -> None:
    """Print state distributions over time.

    Parameters
    ----------
    history : (T, n) array
        State distributions at each time step.
    state_names : list of str, optional
        Labels for each state.  Defaults to 'State 0', 'State 1', ...
    """
    n = history.shape[1]
    if state_names is None:
        state_names = [f"State {i}" for i in range(n)]

    for t, dist in enumerate(history):
        print(f"Time {t}:")
        for name, prob in zip(state_names, dist):
            print(f"  {name}: {prob:.4f}")
