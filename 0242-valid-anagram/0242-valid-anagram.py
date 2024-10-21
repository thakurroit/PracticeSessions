class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        # for i in s:
        #     if i not in t:
        #         return False
        #     else:
        #         t = t.replace(i, "", 1)

        check = defaultdict(int)

        for i in range(len(t)):
            check[s[i]] += 1
            check[t[i]] -= 1

        for val in check.values():
            if val != 0:
                return False
        
        return True

