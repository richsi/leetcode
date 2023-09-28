#FIRST SOLUTION
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = []
        maxlen = 0

        for i in s:
            while i in result:
                result.pop(0)
            
            result.append(i)
            print(result)
            maxlen = max(maxlen, len(result))
    
        return maxlen
    
  
    

  