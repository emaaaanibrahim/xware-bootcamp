# leetcode solutions :

## link : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/submissions/

```
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        difference = high-low
        count = difference//2 + max(high%2,low%2)
        return count
```






