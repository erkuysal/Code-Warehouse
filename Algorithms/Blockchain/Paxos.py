import random


class PaxosNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.proposed_value = None
        self.accepted_value = None
        self.accepted_proposal_id = None

    def propose(self, proposal_id, value):
        if self.accepted_proposal_id is None or proposal_id > self.accepted_proposal_id:
            self.accepted_proposal_id = proposal_id
            self.proposed_value = value
            print(f"Accepted ID: {self.accepted_proposal_id}, Proposal Value: {self.proposed_value}")
            return True
        return False

    def accept(self, proposal_id, value):
        if proposal_id >= self.accepted_proposal_id:
            self.accepted_value = value
            print(f"Accepted Value: {self.accepted_value}")
            return True
        return False


class Paxos:
    def __init__(self, nodes):
        self.nodes = nodes

    def run_paxos(self, proposal_id, value):
        # Phase 1: Propose
        acceptances = []
        for node in self.nodes:
            if node.propose(proposal_id, value):
                acceptances.append(node)
                print(f'Acceptances: {acceptances}')

        if len(acceptances) < len(self.nodes) / 2:
            return None  # Consensus not reached

        # Phase 2: Accept
        accepted_value = None
        for node in acceptances:
            if node.accept(proposal_id, value):
                accepted_value = value
                print(f'Accepted Value: {accepted_value}')

        return accepted_value


# Example usage
nodes = [PaxosNode(i) for i in range(10)]
paxos = Paxos(nodes)
proposal_id = random.randint(0, 100)
value = "Value1"
consensus_value = paxos.run_paxos(proposal_id, value)

print("Consensus Value:", consensus_value)