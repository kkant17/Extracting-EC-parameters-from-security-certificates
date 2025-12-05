# Extracting EC Curve Parameters from a TLS Certificate

This project extracts the **elliptic curve equation** and the **field characteristic** used in a website's TLS certificate. Modern websites that use ECDSA specify their elliptic curve using an **OID** inside the certificate. The certificate does **not** include the curve parameters themselves, so the parameters must be taken from the official NIST/SECG standards.

The program performs:

1. Loading the exported TLS certificate  
2. Extracting the elliptic-curve OID  
3. Identifying the NIST curve (`prime256v1`, `secp256r1`, etc.)  
4. Printing:
   - Field characteristic **p**
   - Curve equation:  
     \[
       y^2 = x^3 + ax + b \mod p
     \]

Only these two items are required for the assignment.

---

## Exporting the Certificate

**Chrome / Edge**

1. Open the website  
2. Click the lock icon → *Connection is secure* → *Certificate is valid*  
3. Open **Details** tab  
4. Click **Export…**  
5. Choose **Base‑64 encoded (.cer)**  
6. Save as `certificate.crt`

---

## Running the Program

Install dependency:

```bash
pip install cryptography
```

Run:

```bash
python parse_cert.py
```

The script expects a file named **certificate.crt**.

---

##  File Overview

### `parse_cert.py`
- Loads and parses the certificate  
- Extracts the elliptic-curve name  
- Prints:
  - Field characteristic **p**
  - Curve equation parameters **a**, **b**

### `curves.py`
Contains official NIST parameters for:
- `secp256r1` / `prime256v1` (P‑256)  
- `secp384r1` (P‑384)  
- `secp521r1` (P‑521)

These are required because X.509 certificates **do not contain EC parameters**, only the curve OID (per RFC 5480).

---

## Example Output

```
Curve Used: secp256r1

--- Field Characteristic ---
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

--- Curve Equation ---
y² = x³ + (-3)x + (0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b) mod p
```

