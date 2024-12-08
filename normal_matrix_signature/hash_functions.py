import hashlib

def G(r):
    print(f"Computing G for vector r:\n{r}")
    r_bytes = r.tobytes()
    result = hashlib.sha256(r_bytes).hexdigest()
    print(f"G(r) = {result}")
    return result

def H(rho, mu, q):
    print(f"Computing H for rho: {rho} and mu: {mu}")
    data = rho.encode() + mu.encode()
    result = int(hashlib.sha256(data).hexdigest(), 16) % q
    print(f"H(rho, mu) = {result}")
    return result
