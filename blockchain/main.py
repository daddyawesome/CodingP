import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.pending_transactions=[]

        self.new_block(previous_hash="The Times 03/Jan/2009 Chancelor on brink of second bailout for banks.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.pending_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions =[]
        self.chain.append(block)

        return block
        