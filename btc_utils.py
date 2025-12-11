import os, ecdsa, hashlib, base58


def create_address():
    """
    Generates a random Private Key and its corresponding Bitcoin Address.
    Returns:
        tuple: (bitcoin_address, private_key_hex)
    """
    # 1) Generate 32 random bytes (256 bits) as the Private Key.
    private_key = os.urandom(32)

    # 2) compute private key*G (G is Generator of elliptic curve (SECP256k1))
    secp256k1_curve = ecdsa.SECP256k1

    # SECP256k1 curve Generator X,Y values:
    # generator_point = secp256k1_curve.generator
    # print(hex(generator_point.x()))
    # print(hex(generator_point.y()))

    # the private_key which is bytes, turns into decimal number and gets verified 
    # whether or not it is in the specified curve range.
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    # compute key * Generator
    vk = sk.verifying_key

    # 3) the output of the above is a point, concat its x and y(it is in bytes format)
    public_key = vk.to_string()

    # 4) Perform SHA-256 hashing on the Public Key(result of 3), followed by RIPEMD-160 hashing.
    sha256_pk = hashlib.sha256(public_key).digest()
    ripemd160_pk = hashlib.new('ripemd160')
    ripemd160_pk.update(sha256_pk)
    public_key_hash = ripemd160_pk.digest()

    # 5) add version number which is 1 byte to its left(MSB)
    version_payload = b'\x00' + public_key_hash

    # 6) get 2 times SHA256 from output of 5 and append the first 4 (MSB) bytes to the output of 5.
    first_sha = hashlib.sha256(version_payload).digest()
    second_sha = hashlib.sha256(first_sha).digest()
    checksum = second_sha[:4]
    binary_address = version_payload + checksum

    # 7) encode the output of 6 in BASE58-ENCODING.
    bitcoin_address = base58.b58encode(binary_address).decode('utf-8')

    return private_key, bitcoin_address