# Proof Of Work
"""
    Principle: A solution that is difficult to find but is easy to verify.
"""

import hashlib
import time


class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine(self, block_data):
        nonce = 0
        while True:
            hash_result = hashlib.sha256(f'{block_data}{nonce}'.encode()).hexdigest()
            if hash_result[:self.difficulty] == "0" * self.difficulty:
                return nonce, hash_result
            nonce += 1


# Example usage
pow = ProofOfWork(difficulty=5)  # Adjust difficulty by increasing/decreasing the number of leading zeros required
block_data = "Block #1 Data"
start_time = time.time()
nonce, hash_result = pow.mine(block_data)
end_time = time.time()

print(f"Nonce: {nonce}")
print(f"Hash: {hash_result}")
print(f"Time taken: {end_time - start_time} seconds")