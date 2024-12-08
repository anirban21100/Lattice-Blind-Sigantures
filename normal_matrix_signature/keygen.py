import numpy as np
from constants import q

def keygen():
    print("Generating keys...")
    f = np.random.randint(-q // 2, q // 2, size=2)
    g = np.random.randint(-q // 2, q // 2, size=2)
    A = np.column_stack((f, g))
    print(f"Matrix A (public key component):\n{A}")
    B = np.random.randint(-q // 2, q // 2, size=(1, 2))
    print(f"Matrix B (public key component):\n{B}")
    T = np.linalg.inv(A) % q
    print(f"Trapdoor matrix T (secret key component):\n{T}")
    kappa = np.random.bytes(16)
    print(f"Random seed kappa: {kappa}")
    return {"pk": (A, B), "sk": (T, B, kappa)}
