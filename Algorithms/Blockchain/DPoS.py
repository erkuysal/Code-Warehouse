# Delegated Proof Of Stake
import random

class Delegate:
    def __init__(self, delegate_id):
        self.delegate_id = delegate_id
        self.votes = 0


class DPoS:
    def __init__(self, delegates):
        self.delegates = delegates

    def vote_for_delegate(self, voter_id, delegate_id):
        for delegate in self.delegates:
            if delegate.delegate_id == delegate_id:
                delegate.votes += 1
                break

    def elect_delegate(self):
        elected_delegate = max(self.delegates, key=lambda d: d.votes)
        return elected_delegate.delegate_id


# Example usage
delegates = [Delegate(i) for i in range(10)]
dpos = DPoS(delegates)
# Simulating voting
# dpos.vote_for_delegate(1, 2)
# dpos.vote_for_delegate(2, 2)
# dpos.vote_for_delegate(3, 3)
# dpos.vote_for_delegate(4, 2)


elected_delegate = dpos.elect_delegate()
print("Elected Delegate:", elected_delegate)