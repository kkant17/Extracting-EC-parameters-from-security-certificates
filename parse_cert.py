from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec

from curves import CURVE_PARAMS


def load_certificate(path):
    with open(path, "rb") as f:
        data = f.read()

    try:
        return x509.load_pem_x509_certificate(data)
    except ValueError:
        return x509.load_der_x509_certificate(data)


def extract_curve_info(cert):
    pubkey = cert.public_key()

    if not isinstance(pubkey, ec.EllipticCurvePublicKey):
        raise ValueError("Certificate does not use EC keys (ECDSA).")

    curve = pubkey.curve
    curve_name = curve.name
    print("Curve Used:", curve_name)

    if curve_name not in CURVE_PARAMS:
        raise ValueError(f"Curve parameters not defined for {curve_name}")

    params = CURVE_PARAMS[curve_name]

    p = params["p"]
    a = params["a"]
    b = params["b"]

    print("\n--- Field Characteristic ---")
    print(f"p = {hex(p)}")

    print("\n--- Curve Equation ---")
    print(f"y² = x³ + ({a})x + ({hex(b)})  mod p")


if __name__ == "__main__":
    cert = load_certificate("certificate.crt")  # change filename as needed
    extract_curve_info(cert)
