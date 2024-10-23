import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len (magazine):
            return False
        # check = magazine
        # for x in ransomNote:
        #     if x in check:
        #         check = check.replace(x,"",1)
        #     else:
        #         return False
        # return True

        check = collections.Counter(magazine)

        for x in ransomNote:
            if check[x] <= 0:
                return False
            check[x] -= 1

        return True
