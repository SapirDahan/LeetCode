class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # Create an adjacency list for the graph
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        # Priority queue (max heap), initialized with the start node and probability 1
        pq = [(-1.0, start_node)]  # We use negative probability for max-heap behavior
        max_prob = [0.0] * n  # Max probability to reach each node, initialized to 0
        max_prob[start_node] = 1.0
        
        while pq:
            # Get the node with the current maximum probability
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob  # Convert back to positive probability
            
            # If we've reached the end node, return the probability
            if node == end_node:
                return curr_prob
            
            # Traverse neighbors
            for neighbor, edge_prob in graph[node]:
                # Calculate new probability for the neighbor
                new_prob = curr_prob * edge_prob
                
                # If the new probability is higher than the previously recorded one, update it
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))  # Push negative to simulate max-heap
        
        # If no path was found to the end node, return 0
        return 0.0