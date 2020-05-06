1. 暴力解法
class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for i in s:
            if i in ['(', '{', '[']:
                left.append(i)
            elif i in [')', '}', ']']:
                if left and left.pop() + i in ['()', '{}', '[]']:
                    continue
                else:
                    return False
            else:
                return False
        if left == []:
            return True
        else:
            return False