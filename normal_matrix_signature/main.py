import numpy as np
from keygen import keygen
from sign import sign
from verify import verify
from constants import q

keys = keygen()
pk, sk = keys["pk"], keys["sk"]
mu = "message"
r = np.random.randint(-q // 2, q // 2, size=2)
print(f"Random vector r:\n{r}")

signature = sign(mu, r, sk)
if signature:
    print("Signing success!")
    print(f"Signature: {signature}")
    is_valid = verify(mu, r, signature, pk)
    if is_valid:
        print(f"Verification result: {is_valid} ✅")
    else:
        print(f"Verification result failed ❌")
else:
    print("Signing failed!")
