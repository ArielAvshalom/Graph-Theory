"""Single Source Shortest Path Using the Bellman Ford Moore Algorithm. 

This algorithm takes as input a 
    directed graph G= (N, E)
    Edge lengths l from one node to another
    The starting Node s

Output from this algo is:
    All reachable nodes from s, with shortest distances from s to any node n
"""
for node in N:
    dist(node) = infinity
    prev(node) = None

dist(s) = 0

#We have nodes in the set of nodes N. Logically we can get the length of N. The number of nodes is |N| = 10 then we are going to traverse all of the edges 9 times

for traversal in range(len(N)-1):
    for edge in E:
        relax(edge)

def relax(node1, node2):
    dist(node2) = min(dist(node2), dist(node1)+ l(node1,node2))
