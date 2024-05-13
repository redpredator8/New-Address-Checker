import time
start_time = time.time()


import os
from pycoin.symbols.btc import network
secret_exponent = int.from_bytes(os.urandom(32), 'big')

key = network.keys.private(secret_exponent)  
address = key.address()
private_key_wif = key.wif()

print(f"Bitcoin Address: {address}")
print(f"Private Key: {private_key_wif}")







end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
