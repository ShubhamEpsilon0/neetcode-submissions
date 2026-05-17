class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.s_len = len(s)
        self.p = p
        self.p_len = len(p)
        self.cache = {}
        return self.isMatchDFS(0,0)

    def isMatchDFS(self, s_index, p_index):
        if (s_index, p_index) in self.cache:
            return self.cache[(s_index, p_index)]

        if p_index == self.p_len and s_index == self.s_len:
            return True

        if p_index == self.p_len and s_index != self.s_len:
            return False 

        isAstricked = p_index != self.p_len - 1 and self.p[p_index + 1] == "*"
        
        if s_index == self.s_len or (self.p[p_index] != "." and self.s[s_index] != self.p[p_index]):
            self.cache[(s_index, p_index)] = isAstricked and self.isMatchDFS(s_index, p_index + 2)
            return self.cache[(s_index, p_index)]

        if not isAstricked:
            self.cache[(s_index, p_index)] = self.isMatchDFS(s_index + 1, p_index + 1)
        else:
            self.cache[(s_index, p_index)] = self.isMatchDFS(s_index + 1, p_index) or self.isMatchDFS(s_index, p_index + 2)

        return self.cache[(s_index, p_index)]
