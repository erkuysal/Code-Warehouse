# Proof Of Stake

import random


class Validator:
    def __init__(self, node_id, stake):
        self.node_id = node_id
        self.stake = stake


class ProofOfStake:
    def __init__(self, validators):
        self.validators = validators

    def select_validator(self):
        total_stake = sum(v.stake for v in self.validators)
        selection_point = random.uniform(0, total_stake)
        current = 0
        for v in self.validators:
            current += v.stake
            if current >= selection_point:
                return v.node_id


# Example usage
validators = [Validator(i, stake=random.uniform(1, 100)) for i in range(5)]
pos = ProofOfStake(validators)
selected_validator = pos.select_validator()

print("Selected Validator:", selected_validator)