from btc_utils import generate_address
import time


# 1 is crusial (it is version number).
TARGET_PREFIX = "1AJM"

attempts = 0

start_time = time.time()
while True:
    attempts += 1
    private_key, address = generate_address()
    if attempts % 100 == 0:
        print(f"Attempts: {attempts}...", end="\r")

    if address.startswith(TARGET_PREFIX):
        elapsed_time = time.time() - start_time
        print(f"\nfound target prefix {TARGET_PREFIX} After {attempts} attempts in {elapsed_time:.2f} seconds")
        print(f"Private Key (Hex): {private_key.hex()}")
        print(f"Address: {address}")
        end_time = time.time()
        
        break