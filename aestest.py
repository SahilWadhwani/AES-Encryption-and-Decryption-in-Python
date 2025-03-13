import os
import sys
import subprocess

def main():
    plaintext = input("Enter plaintext: ")
    
    # Generate a random 16-byte AES key
    key = os.urandom(16)
    key_hex = key.hex()
    print("Secret Key (hex):", key_hex)

    # Use the appropriate Python command based on the OS
    python_cmd = "python3" if sys.platform != "win32" else "python"

    try:
        # Encrypt plaintext using AES
        result = subprocess.run([python_cmd, "aesencrypt.py", key_hex, plaintext],
                                capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error during encryption:", e.stderr)
        sys.exit(1)

    ciphertext_hex = result.stdout.strip()
    print("Ciphertext (hex):", ciphertext_hex)

    try:
        # Decrypt ciphertext using AES
        result = subprocess.run([python_cmd, "aesdecrypt.py", key_hex, ciphertext_hex],
                                capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error during decryption:", e.stderr)
        sys.exit(1)

    decrypted = result.stdout.strip()

    # Ensure safe decoding of decrypted output
    try:
        decrypted = bytes.fromhex(decrypted).decode('utf-8', errors='ignore')
    except ValueError:
        pass  # If it's not a valid hex string, assume it's already plain text

    print("Decrypted Plaintext:", decrypted)

if __name__ == "__main__":
    main()
