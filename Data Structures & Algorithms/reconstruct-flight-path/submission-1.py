class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort()

        for ticket in tickets:
            adjList[ticket[0]].append(ticket[1])

        itinerary = ["JFK"]

        def dfs (src):
            if len(itinerary) == len(tickets) + 1:
                return True

            if not adjList[src]:
                return False

            temp = list(adjList[src])

            for index, nextDest in enumerate(temp):
                itinerary.append(nextDest)
                adjList[src].pop(index)

                if dfs(nextDest): return True

                itinerary.pop()
                adjList[src].insert(index, nextDest)

            return False

        dfs("JFK")
        return itinerary
