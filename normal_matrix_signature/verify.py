import numpy as np
from constants import q, beta_r, beta_s
from hash_functions import H

def verify(mu, r, sig, pk):
    print("Verifying signature...")
    A, B = pk[0], pk[1]
    rho, s = sig["rho"], sig["s"]
    print(f"Message: {mu}\nVector r:\n{r}\nSignature: {sig}")
    if np.linalg.norm(r) > beta_r:
        print(f"Norm of r exceeds beta_r: {np.linalg.norm(r)} > {beta_r}")
        return False
    if np.linalg.norm(s) > beta_s:
        print(f"Norm of s exceeds beta_s: {np.linalg.norm(s)} > {beta_s}")
        return False
    H_rho_mu = H(rho, mu, q)
    lhs = (A @ s) % q
    rhs = (B @ r + H_rho_mu) % q
    print(f"LHS (A * s mod q): {lhs}")
    print(f"RHS (B * r + H mod q): {rhs}")
    if np.allclose(lhs, rhs):
        print("Signature is valid. ✅")
        return True
    else:
        print("Signature is invalid. ❌")
        return False
