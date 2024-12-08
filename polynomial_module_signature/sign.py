import numpy as np
from constants import q, beta_r, beta_s, d
from hash_functions import G, H


def sign(mu, r, sk):
    """Sign the message."""
    print("Signing the message...")
    T, B, kappa = sk  # Correctly unpack tuple
    print(f"Message: {mu}\nVector r:\n{r}")
    if np.linalg.norm(r) > beta_r:
        print(f"Norm of r exceeds beta_r: {np.linalg.norm(r)} > {beta_r}")
        return None  # Abort if ||r|| is too large

    rho = G(r)
    H_rho_mu = H(rho, mu)
    c = (B @ r + H_rho_mu) % q
    print(f"Computed value c = (B * r + H(rho, mu)) mod q: {c}")

    c_poly = np.full(d, c)  # Extend c to match the polynomial dimension
    print(f"Computed polynomial c:\n{c_poly}")

    # Use c_poly for matrix multiplication
    s = (T @ c_poly) % q
    print(f"Computed value s = (T * c) mod q: {s}")

    if np.linalg.norm(s) > beta_s:
        print(f"Norm of s exceeds beta_s: {np.linalg.norm(s)} > {beta_s}")
        return None  # Abort if ||s|| is too large

    print("Message signed successfully!")
    return {"rho": rho, "s": s}
