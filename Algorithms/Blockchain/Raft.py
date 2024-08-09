import random
import time


class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.term = 0
        self.voted_for = None

    def request_vote(self, candidate_id, candidate_term):
        if candidate_term > self.term:
            self.term = candidate_term
            self.voted_for = candidate_id
            print(f"Node {self.node_id} voted for {self.voted_for} in term {self.term}")
            return True
        return False


class Raft:
    def __init__(self, nodes):
        self.nodes = nodes
        self.leader = None

    def elect_leader(self):
        candidate_id = random.choice([node.node_id for node in self.nodes])
        votes = 0
        term = random.randint(1, 100)
        for node in self.nodes:
            if node.request_vote(candidate_id, term):
                votes += 1
                print(f"Node{node}, voted {candidate_id} on term {term}")

        if votes > len(self.nodes) / 2:
            self.leader = candidate_id
            print(f'Candidate: {candidate_id}')
            return candidate_id
        return None


# Example usage
nodes = [RaftNode(i) for i in range(100)]
raft = Raft(nodes)
leader = raft.elect_leader()

print(f'Raft: {Raft}, Leader: {leader}')
