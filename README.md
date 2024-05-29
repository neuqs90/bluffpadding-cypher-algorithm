# BluffPadding Cipher Algorithm

🔒 **BluffPadding Cipher Algorithm** is a Python-based encryption tool that combines random prefixes and suffixes with character shifts to provide enhanced text obfuscation. Ideal for lightweight data security. 🛡️

## Features

- Generates random prefixes and suffixes for added security
- Shifts characters by a random value for encoding
- Simple encryption and decryption functions

## Installation

You can install the `bluffpadding-cypher-algorithm` package from PyPI using pip:

```sh
pip install bluffpaddingcypher
```

## Usage

Here is how you can use the bluffpaddingcypher package to encrypt and decrypt text:

- Encrypting Text :

    ```python
    from bluffpaddingcypher.cypher import encrypt

    text = "Hello, World!"
    encrypted_text = encrypt(text)
    print("Encrypted:", encrypted_text)
    ```
- Decrypting Text : 

    ```python
    from bluffpaddingcypher.cypher import decrypt

    encrypted_text = """MI{~rCb6o'PS\ZfRovvy6*ay|vn+)S'h,3YvNs*=]yz,c{]SWeC5^.:syM|Xt}^$I(G9%W:NL]b?VTLZ+-OY3_$},Lf?*p<=L5F0T6S~'Bkhv82S"""  # Use the output from the encryption step
    decrypted_text = decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)
    ```

- Example : 

    ```python
    from bluffpaddingcypher.cypher import encrypt, decrypt

    # Original text
    text = "Hello, World!"

    # Encrypt the text
    encrypted_text = encrypt(text)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text)
    print("Decrypted Text:", decrypted_text)
    ```

- Expected Output : 

    ```python
    Encrypted: =Hzw@<UXf!x{9Rovvy6*ay|vn+VJx!RIG@XGZ)'af&>pbG8/O|q6B$YxP"\nP*fbI)/xUd$pf!do2

    Decrypted: Hello, World!
    ```

# How It Works :

1. Encrypt Function

    - Generates a random prefix and suffix of random lengths (between 2 and 100 characters).
    - Shifts each character in the input text by a random value (between 1 and 10).
    - Combines the prefix, shifted text, suffix, and the shift value into the final encoded text.

2. Decrypt Function

    - Extracts the prefix length and removes the prefix.
    - Extracts the suffix length and removes the suffix.
    - Extracts the shift value.
    - Reverses the character shift to retrieve the original text.
      
## Example ScreenShot : 

![image](https://github.com/neuqs90/bluffpadding-cypher-algorithm/assets/166356026/0ac613fb-0c2c-4b1f-94a5-dedd5b94be48)

# Contribution : 

Contributions are welcome! Please open an issue or submit a pull request on GitHub [Repository](https://github.com/neuqs90/bluffpadding-cypher-algorithm.git).

# Author : 

Name : Bhavya Padaliya
