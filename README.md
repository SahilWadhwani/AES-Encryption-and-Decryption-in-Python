# AES Encryption and Decryption in Python

## Overview
This project implements **AES (Advanced Encryption Standard) encryption and decryption** using Python. It includes three scripts:
1. `aesencrypt.py` - Encrypts plaintext using AES.
2. `aesdecrypt.py` - Decrypts ciphertext using AES.
3. `aestest.py` - Automates encryption and decryption together.

AES is a symmetric encryption algorithm widely used for securing data. This implementation supports **AES-128**, meaning it operates on **16-byte blocks** and uses a **128-bit key**.

## Project Structure
* `aesencrypt.py`: Implements AES encryption.
* `aesdecrypt.py`: Implements AES decryption.
* `aestest.py`: Tests encryption and decryption by generating a random AES key.


## How to Run the Scripts

### **1. Running AES Encryption**
To encrypt plaintext using AES:

```bash
python aesencrypt.py <hex_key> <plaintext>
```
Example:
```bash
 python aesencrypt.py 3fa4b5c6d7e8f9a0b1c2d3e4f5a6b7c8 "Hello, AES!"
```
**Output:** Ciphertext in **hexadecimal format**.

### **2. Running AES Decryption**

To decrypt AES-encrypted ciphertext:
```bash
python aesdecrypt.py <hex_key> <hex_ciphertext>
```

Example:
```bash 
python aesdecrypt.py 3fa4b5c6d7e8f9a0b1c2d3e4f5a6b7c8 "87d9e4f3c2b1a8d4..."
```

**Output:** Decrypted plaintext.


### **3. Running Full Encryption & Decryption Test**

To test encryption and decryption together:

```bash
python aestest.py
```

-   The script generates a **random 16-byte AES key**.    
-   Asks the user for plaintext input.    
-   Encrypts and then decrypts it.    
-   Displays the original, encrypted, and decrypted messages.

**Example Output:**
```bash
Enter plaintext: Hello, AES!
Secret Key (hex): 3fa4b5...
Ciphertext (hex): 87d9e4f3...
Decrypted Plaintext: Hello, AES!
```

## Dependencies

-   Python 3.x
    
-   No external libraries required (uses built-in Python functionality).
    

----------


## Explanation of AES Process

### **AES Encryption Process**

1.  **SubBytes**: Each byte is substituted using an S-Box.
    
2.  **ShiftRows**: Rows of the state matrix are shifted.
    
3.  **MixColumns**: Columns are mixed using matrix multiplication in GF(2⁸).
    
4.  **AddRoundKey**: XOR the state with a round key.
    
5.  Repeat for **10 rounds** (AES-128).


### Padding Implementation

AES operates on fixed-size **16-byte blocks**. If the plaintext is not a multiple of 16 bytes, **PKCS7 padding** is applied before encryption and removed after decryption.

#### **Padding Process**

-   If plaintext length is not a multiple of 16, extra bytes are added.
    
-   Each padding byte contains the number of padding bytes added.
    

Example:

```
Original Text: "HELLO"
Bytes: [H, E, L, L, O]
After Padding (PKCS7): [H, E, L, L, O, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B]
```

-   The number `0x0B (11)` is used because **11 extra bytes** were needed to reach a full **16-byte block**.
    

### **Padding Removal**

-   When decrypting, the last byte of the plaintext tells how many padding bytes were added and should be removed.
    
-   If padding is invalid, decryption might produce incorrect results.


### **AES Decryption Process**

1.  **Inverse AddRoundKey**: XOR with the round key.
    
2.  **Inverse ShiftRows**: Reverse row shifts.
    
3.  **Inverse SubBytes**: Reverse byte substitution.
    
4.  **Inverse MixColumns**: Reverse column mixing.
    
5.  Repeat for **10 rounds**.


---
## Notes

-   This implementation only supports **AES-128 (16-byte key)**.
    
-   Input plaintext **must be padded** to be a multiple of 16 bytes.
    
-   The scripts handle **hexadecimal input/output** for easy cross-platform compatibility.

-   Note that this implementation is pure Python and not optimized for speed.
  
-   A faster alternative would use pycryptodome or cryptography libraries.  

---
