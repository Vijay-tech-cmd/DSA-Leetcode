class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [False] * n
        count = 0
        def Dfs(node):
            visit[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visit[neighbor]:
                    Dfs(neighbor)
        for i in range(n):
            if not visit[i]:
                Dfs(i)
                count += 1
        return count