## Array Game
Given an array of integers, determine the number of moves to make all elements equal. Each move consists of choosing all but 1 element and incrementing their values by 1.

### Example
```
Input: [1,2,3]
Output: 3

Explanation:
[1,2,3] -> [2,3,3] -> [3,4,3] -> [4,4,4]

Input: [3,4,6,6,3]
Output: 7

Explanation:
[3,4,6,6,3] -> [4,5,7,6,4] -> [5,6,7,7,5] -> [6,7,7,8,6] -> [7,8,8,8,7] -> [8,9,9,8,8] -> [9,10,9,9,9] -> [10,10,10,10,10]
```

Source: Hackerrank