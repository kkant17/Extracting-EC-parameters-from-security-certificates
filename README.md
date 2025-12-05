# README

## Overview
This project extracts elliptic-curve parameters from a website’s TLS certificate. Modern websites using ECDSA include an EC public key and an OID (Object Identifier) that specifies which standard curve is used. The program reads the certificate, identifies the curve, and prints the curve equation, field characteristic, generator point, order, and public key.

## Usage
1. Export the website certificate in Base‑64 (.cer/.crt) format.
2. Install dependencies:
```
pip install cryptography
```
3. Run:
```
python parse_cert.py
```

## Files
### `parse_cert.py`
Loads the certificate, extracts the EC public key, detects the curve from its OID, and prints parameters.

### `curves.py`
Defines parameters for common NIST curves: P‑256 (prime256v1 / secp256r1), P‑384, P‑521.

## Notes
- `prime256v1` and `secp256r1` are two names for the same curve.
- Only EC certificates are supported.
- OIDs uniquely identify curves (e.g., P‑256 → 1.2.840.10045.3.1.7).

## Output Example
```
Curve Name: secp256r1
Public Key Point (Q): x, y
Field characteristic p: …
Equation: y² = x³ − 3x + b mod p
Generator G: Gx, Gy
Order n, Cofactor h
```
