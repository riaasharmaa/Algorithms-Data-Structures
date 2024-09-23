import sys
#O(n+m) time
from typing import Dict, List
Node = str
NodeList = List[Node]
Graph = Dict[Node, NodeList]

def dfs(graph: Graph, nodes: NodeList) -> NodeList:
    #track unvisited nodes
    visited = {node: False for node in nodes}
    result: NodeList = [] 
    total_nodes: int = len(nodes)
    current_index: int = 0  
    #loop through all nodes, in case there are disconnected components
    while current_index < total_nodes:
        stack: NodeList = [nodes[current_index]]
        while stack:
            current_node: Node = stack.pop()
            if not visited[current_node]:
                result.append(current_node) 
                visited[current_node] = True
                #add all its neighbors (in reverse order) to the stack if they are unvisited
                neighbors: NodeList = graph.get(current_node, [])
                for neighbor in reversed(neighbors):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        #move to the next unvisited node for another dfs if there are disconnected components
        while current_index < total_nodes and visited[nodes[current_index]]:
            current_index += 1
    return result

def read_graph(num_nodes: int) -> (Graph, NodeList):
    #parse the input
    graph: Graph = {}
    node_order: NodeList = []
    for _ in range(num_nodes):
        parts: NodeList = input().split()
        #node & neighbor
        graph[parts[0]] = parts[1:]
        #maintain order
        node_order.append(parts[0])
    return graph, node_order

if __name__ == "__main__":
    num_cases = int(input())
    for _ in range(num_cases):
        nodes_count: int = int(input())
        graph, nodes = read_graph(nodes_count)
        print(" ".join(dfs(graph, nodes)))