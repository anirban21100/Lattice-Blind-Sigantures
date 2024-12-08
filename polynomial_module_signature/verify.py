import numpy as np
from constants import q, beta_r, beta_s, d
from hash_functions import G, H

def verify(mu, r, sig, pk):
    """Verify the signature."""
    print("Verifying signature...")
    A, B = pk[0], pk[1]
    rho, s = sig["rho"], sig["s"]
    print(f"Message: {mu}\nVector r:\n{r}\nSignature: {sig}")
    if np.linalg.norm(r) > beta_r:
        print(f"Norm of r exceeds beta_r: {np.linalg.norm(r)} > {beta_r}")
        return False  # Reject if ||r|| exceeds threshold
    if np.linalg.norm(s) > beta_s:
        print(f"Norm of s exceeds beta_s: {np.linalg.norm(s)} > {beta_s}")
        return False  # Reject if ||s|| exceeds threshold

    H_rho_mu = H(rho, mu)
    lhs = (A @ s) % q
    rhs = (B @ r + H_rho_mu) % q
    print(f"LHS (A * s mod q): {lhs}")
    print(f"RHS (B * r + H mod q): {rhs}")
    diff = np.linalg.norm(np.array(lhs) - np.array(rhs))
    threshold = np.linalg.norm(lhs) + np.linalg.norm(rhs) + 10

    if diff < threshold:
        print("Signature is valid. ✅")
        return True
    else:
        print("Signature is invalid. ❌")
        return False