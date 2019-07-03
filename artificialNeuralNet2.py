#Joseph Harrison 2019
from matrixUtilities1 import *
import random

class Node:

    def __init__(self):
        self.links = Vector()
        self.weights = Vector()
        #initially this is an input node
        self.inputnode = True
        self.value = value

    def link(self, nodes, weights=None):
        #if weights argument not used
        #generate random weights
        if weights == None:
            weights = [random.random()
                       for i in range(len(nodes))]    
        #this node is no longer an
        #input node
        self.inputnode = False
        #link each node to self
        for i in range(len(nodes)):
            self.links.elems.append(nodes[i])
            self.weights.elems.append(weights[i])

    @property
    def weighted_sum(self, evaluated):
        if self.inputnode:
            return self.value
        elif self in evaluated:
            return self.value
        else:
            x = Vector([self.child.weighted_sum(evaluated)
                 for child in self.links])
            self.value = dot(x, self.weights) + self.bias
            

if __name__ == '__main__':
    root = Node()
    hidden = [Node() for i in range(3)]
    inputs = [Node() for i in range(2)]
    
    #specifying weights argument
    root.link(hidden, [2, 4, 6])
    #random weights
    for node in hidden:
        node.link(inputs)

    print(f'root is input node? {root.inputnode}')

    print(f'hidden nodes:')
    for node in hidden:
        print(f'input node? {node.inputnode}')

    print('input nodes:')
    for node in inputs:
        print(f'input node? {node.inputnode}')

