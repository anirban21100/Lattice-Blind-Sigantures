from keygen import keygen
from utils import random_polynomial
from sign import sign
from verify import verify

# Retesting the implementation
keys = keygen()
pk, sk = keys["pk"], keys["sk"]
mu = "message"  # Message to sign
r = random_polynomial()  # Random polynomial
print(f"Random polynomial r:\n{r}")

# Sign the message
signature = sign(mu, r, sk)
if signature:
    print("Signing success!")
    print(f"Signature: {signature}")
    # Verify the signature
    is_valid = verify(mu, r, signature, pk)
    if is_valid:
        print(f"Verification result: {is_valid} ✅")
    else:
        print(f"Verification result failed ❌")
else:
    print("Signing failed!")
