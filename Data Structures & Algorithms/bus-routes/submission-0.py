from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Build Nodes to Route Map
        node_to_route_map = defaultdict(list)
        for index, route in enumerate(routes):
            for node in route:
                node_to_route_map[node].append(index)

        bfs_queue = deque()
        bfs_queue.append(source)
        min_busses = 0
        visited_routes = set()
        while bfs_queue:
            queue_size = len(bfs_queue)
            min_busses += 1
            for _ in range(queue_size):
                cur_node = bfs_queue.popleft()

                routes_from_cur_node = node_to_route_map[cur_node]

                for route_index in routes_from_cur_node:
                    if route_index in visited_routes:
                        continue
                    visited_routes.add(route_index)
                    for node in routes[route_index]:
                        if node == target:
                            return min_busses
                        if node != cur_node:
                            bfs_queue.append(node)
        return -1



        