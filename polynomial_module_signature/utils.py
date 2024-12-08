import numpy as np
from constants import d

def random_polynomial():
    """Generate a random polynomial in R with coefficients in [-2, 2]."""
    return np.random.randint(-2, 3, size=d)
