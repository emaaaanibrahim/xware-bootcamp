# leetcode solutions :

## link :  https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/

```
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/len(salary)
```
