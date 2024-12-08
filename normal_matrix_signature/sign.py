import numpy as np
from constants import q, beta_r, beta_s
from hash_functions import G, H

def sign(mu, r, sk):
    print("Signing the message...")
    T, B, kappa = sk
    print(f"Message: {mu}\nVector r:\n{r}")
    if np.linalg.norm(r) > beta_r:
        print(f"Norm of r exceeds beta_r: {np.linalg.norm(r)} > {beta_r}")
        return None
    rho = G(r)
    H_rho_mu = H(rho, mu, q)
    c = (B @ r + H_rho_mu) % q
    print(f"Computed value c = (B * r + H(rho, mu)) mod q: {c}")
    s = (T @ np.array([c, c])) % q
    print(f"Computed value s = (T * c) mod q: {s}")
    if np.linalg.norm(s) > beta_s:
        print(f"Norm of s exceeds beta_s: {np.linalg.norm(s)} > {beta_s}")
        return None
    print("Message signed successfully!")
    return {"rho": rho, "s": s}
