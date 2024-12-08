import numpy as np
from constants import q
from utils import random_polynomial

def keygen():
    """Generate a public-private key pair."""
    print("Generating keys...")
    f = random_polynomial()  # Secret key component in R
    g = random_polynomial()
    A = np.column_stack((f, g))  # Public matrix in R
    print(f"Matrix A (public key component):\n{A}")
    B = random_polynomial().reshape(1, -1)  # Another public component
    print(f"Matrix B (public key component):\n{B}")
    # Trapdoor is simplified for illustration
    T = np.linalg.pinv(A) % q  # Pseudoinverse approximation
    print(f"Trapdoor matrix T (secret key component):\n{T}")
    kappa = np.random.bytes(16)  # Random seed
    print(f"Random seed kappa: {kappa}")
    return {"pk": (A, B), "sk": (T, B, kappa)}
