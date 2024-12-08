import numpy as np

# Constants and parameters
q = 7933  # Modulus for lattice
d = 512  # Degree of cyclotomic ring R
sigma = 232  # Gaussian sampling deviation
beta_r = 2 * np.sqrt(d)  # Norm bound for r
beta_s = sigma * np.sqrt(2 * d)  # Norm bound for s
