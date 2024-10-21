class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'(': ')', '{':'}', '[': ']'}

        check = []

        for i in s:
            if i in chars.keys():
                check.append(chars[i])
            elif i in chars.values():
                
                if not check or i != check.pop():
                    return False
            
        
        return not check
                
        