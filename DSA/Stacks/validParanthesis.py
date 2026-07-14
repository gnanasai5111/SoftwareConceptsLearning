```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={
            '}':'{',
            ']':'[',
            ')':'('
        }
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif not stack:
                return False
            elif stack.pop()!=pairs[ch]:
                return False
        return not stack
  ```
