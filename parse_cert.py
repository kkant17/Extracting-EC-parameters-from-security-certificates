from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from curves import get_curve_params
import binascii

def load_certificate(path):
    with open(path, "rb") as f:
        data = f.read()
    try:
        return x509.load_pem_x509_certificate(data, default_backend())
    except ValueError:
        return x509.load_der_x509_certificate(data, default_backend())

def extract_ec_info(cert):
    pubkey = cert.public_key()

    if not isinstance(pubkey, ec.EllipticCurvePublicKey):
        raise ValueError("Certificate does not use EC keys")

    curve = pubkey.curve
    numbers = pubkey.public_numbers()

    print(f"Curve Name: {curve.name}")
    print(f"Public Key Point (Q):")
    print(f"  x = {hex(numbers.x)}")
    print(f"  y = {hex(numbers.y)}")

    # Get full curve parameters
    params = get_curve_params(curve.name)

    if params:
        print("\n--- Elliptic Curve Parameters ---")
        print(f"Field characteristic p:\n  {hex(params['p'])}")
        print(f"Curve equation: y^2 = x^3 + {params['a']}x + {params['b']} (mod p)")
        print(f"Generator G:")
        print(f"  Gx = {hex(params['Gx'])}")
        print(f"  Gy = {hex(params['Gy'])}")
        print(f"Order n:\n  {hex(params['n'])}")
        print(f"Cofactor h: {params['h']}")
    else:
        print("\nCurve parameters not found for this curve.")

if __name__ == "__main__":
    cert = load_certificate("certificate.crt")  # <-- rename to your file
    extract_ec_info(cert)
