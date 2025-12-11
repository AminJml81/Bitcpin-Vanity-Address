# Bitcoin-Vanity-Address
Implementing Bitcoin Vanity Address in Python Using real Algorithms.

<img width="1180" height="1468" style="width:50%" alt="procedure" src="https://github.com/user-attachments/assets/3981b1d2-db1c-4034-b4c0-5ee7d7f97026" />

## Algorithm:
1. Generate random 32 Bytes private key.
    ```
    private_key = os.urandom(32)
    ```
2. Get corresponding public key from SECP256k1 elliptic curve.
    ```
    sk = ecdsa.SigningKey.from_string(private_key, curve=secp256k1_curve)
    vk = sk.verifying_key
    public_key = vk.to_string()
    ```
3. Perform SHA256 on the public key.
    ```
    sha256_pk = hashlib.sha256(public_key).digest()
    ```
4. Perfrom RIPEMD-160 on the previous result.
    ```
    ripemd160_pk = hashlib.new('ripemd160')
    ripemd160_pk.update(sha256_pk)
    public_key_hash = ripemd160_pk.digest()
    ```
5. Extend with 1 byte version byte to the MSB(Most Significant Bit)(21 Bytes)
    ```
    version_payload = b'\x00' + public_key_hash
    ```
6. Perform SHA256 two times from the previous result and store its first 4 Bytes(MSB) as checksum.
    ```
    first_sha = hashlib.sha256(version_payload).digest()
    second_sha = hashlib.sha256(first_sha).digest()
    checksum = second_sha[:4]
    ```
7. place result of 5 in the left and result of 6 in the right.(total 25 Bytes)
    ```
    binary_address = version_payload + checksum
    ```
8. Encode the previous result to Base58.
    ```
   bitcoin_address = base58.b58encode(binary_address).decode('utf-8')
    ```

### Sample Output
finding address that starts with 1AJ.
<img width="965" height="107" alt="output1" src="https://github.com/user-attachments/assets/6878bef7-3498-4721-b7e9-8ba0a491dab5" />

finding address that starts with 1AJM.
 <img width="961" height="107" alt="output2" src="https://github.com/user-attachments/assets/9ae0c115-ade4-48b7-b534-afd01f5f97f4" />

