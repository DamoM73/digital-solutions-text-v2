# Coding &mdash; Unit 4

## Compressing Files in Python

To compress a file in Python, you can use the `zipfile` module, which provides tools for creating, reading, writing, and extracting ZIP files. Here’s a simple example to demonstrate how to compress a file using this module:

### Compressing a File

```python
import zipfile
import os

def compress_file(file_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))

# Example usage
file_to_compress = 'example.txt'  # Replace with your file path
compressed_file = 'example.zip'   # Replace with your desired output file path

compress_file(file_to_compress, compressed_file)
print(f"File {file_to_compress} compressed to {compressed_file}")
```

In this example, `example.txt` is the file you want to compress, and `example.zip` is the output ZIP file. The `os.path.basename(file_path)` function ensures that only the file name is included in the ZIP archive, not the full path.

### Compressing Multiple Files

If you want to compress multiple files into a single ZIP archive, you can modify the function to accept a list of files:

```python
import zipfile

def compress_files(file_paths, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))

# Example usage
files_to_compress = ['example1.txt', 'example2.txt']  # Replace with your file paths
compressed_file = 'examples.zip'   # Replace with your desired output file path

compress_files(files_to_compress, compressed_file)
print(f"Files {files_to_compress} compressed to {compressed_file}")
```

### Compressing a Directory

To compress all files in a directory, you can walk through the directory and add each file to the ZIP archive:

```python
import zipfile
import os

def compress_directory(directory_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

# Example usage
directory_to_compress = 'example_directory'  # Replace with your directory path
compressed_file = 'example_directory.zip'    # Replace with your desired output file path

compress_directory(directory_to_compress, compressed_file)
print(f"Directory {directory_to_compress} compressed to {compressed_file}")
```

In this script, `os.walk(directory_path)` is used to iterate through all files in the specified directory and its subdirectories. `os.path.relpath(file_path, directory_path)` ensures that the directory structure is preserved in the ZIP archive.

## Encrypting files in Python

To encrypt files in Python, you can use the `cryptography` library, which provides a simple and secure way to encrypt and decrypt files.

### Install the `cryptography` library

First, you need to install the library. You can do this using pip:

```bash
pip install cryptography
```

### Encrypting a File

Here's a Python script that demonstrates how to encrypt a file using the `cryptography` library:

```python
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open('secret.key', 'rb').read()

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Example usage
generate_key()  # Run this only once to generate and save the key
file_to_encrypt = 'example.txt'  # Replace with your file path

encrypt_file(file_to_encrypt)
print(f"File {file_to_encrypt} encrypted.")
```

In this script:

- `generate_key()` generates and saves an encryption key to a file named `secret.key`.
- `load_key()` loads the encryption key from the file.
- `encrypt_file()` encrypts the specified file using the key.

### Decrypting a File

To decrypt the file, you can use the following script:

```python
from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    return open('secret.key', 'rb').read()

# Decrypt a file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path.replace('.enc', ''), 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
file_to_decrypt = 'example.txt.enc'  # Replace with your encrypted file path

decrypt_file(file_to_decrypt)
print(f"File {file_to_decrypt} decrypted.")
```

In this script:

- `load_key()` loads the encryption key from the file.
- `decrypt_file()` decrypts the specified file using the key and saves the decrypted data.

### Important Notes:

- **Key Management:** The encryption key (`secret.key`) must be kept secure. If it is lost, you won't be able to decrypt your files. If it is stolen, anyone with the key can decrypt your files.
- **File Extensions:** The encrypted file is saved with an `.enc` extension to differentiate it from the original file. You can change this as needed.

## Hashing files in Python

Hashing a file in Python can be done using the `hashlib` module, which provides various hash functions such as SHA-256, MD5, and others.

### Hashing a File

Here's a Python script that demonstrates how to hash a file using SHA-256:

```python
import hashlib

def hash_file(file_path):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file in chunks to handle large files
        for byte_block in iter(lambda: file.read(4096), b''):
            sha256_hash.update(byte_block)
    
    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

# Example usage
file_to_hash = 'example.txt'  # Replace with your file path

file_hash = hash_file(file_to_hash)
print(f"The SHA-256 hash of the file is: {file_hash}")
```

In this script:

- `hashlib.sha256()` creates a SHA-256 hash object.
- The file is opened in binary mode (`'rb'`) to ensure it works with all types of files, including text and binary files.
- The file is read in chunks of 4096 bytes to handle large files efficiently.
- The `update()` method is called for each chunk to update the hash object.
- The `hexdigest()` method returns the hash value as a hexadecimal string.

### Hashing with Other Algorithms

You can easily switch to other hash algorithms provided by `hashlib` (e.g., MD5, SHA-1) by replacing `hashlib.sha256()` with the desired hash function:

```python
import hashlib

def hash_file(file_path, algorithm='sha256'):
    # Create a hash object based on the chosen algorithm
    hash_obj = hashlib.new(algorithm)
    
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file in chunks to handle large files
        for byte_block in iter(lambda: file.read(4096), b''):
            hash_obj.update(byte_block)
    
    # Return the hexadecimal digest of the hash
    return hash_obj.hexdigest()

# Example usage
file_to_hash = 'example.txt'  # Replace with your file path

# Hash the file using SHA-256
file_hash_sha256 = hash_file(file_to_hash, 'sha256')
print(f"The SHA-256 hash of the file is: {file_hash_sha256}")

# Hash the file using MD5 (for example, though it's less secure)
file_hash_md5 = hash_file(file_to_hash, 'md5')
print(f"The MD5 hash of the file is: {file_hash_md5}")
```

This script allows you to specify the hash algorithm you want to use. Just pass the desired algorithm name (e.g., `'sha256'`, `'md5'`, `'sha1'`) to the `hash_file` function.

### Important Notes:

- **Security Considerations:** Some hash algorithms like MD5 and SHA-1 are considered weak and should not be used for security-critical applications. SHA-256 and SHA-3 are generally recommended for secure hashing.
- **File Integrity:** Hashing is commonly used to verify file integrity. By comparing the hash of a downloaded file with a known hash value, you can ensure the file has not been tampered with.
