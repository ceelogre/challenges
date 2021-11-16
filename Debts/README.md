## Debts evader

A company has a list of expected revenues and payments for the upcoming year in chronological order. The problem is that at some moments in time, the sum of previous payments can be larger than the total previous revenue, which would put the company in debt.  To avoid this, the company takes an approach of rescheduling some expenses to the end of of the year.

You are given an array of integers, where positive numbers represent revenues and negative numbers represent expenses, all in chronological order. In one step, you can relocate any expense (negative numbers) to the end of the array. What is the minimum number of such relocations to make sure the company never falls into debt? In other words, ensure that there is no consecutive sequence of elements starting from the beginning of the array that sums up to a negative number.

You can assume the sum of all elements in S is non-negative (there are some positive numbers)

Write a function that given an array S of N integers, returns the minimum number of relocations so the company never falls into debt.

### sample input
`S = [10, -10, -1, -1, 10] => 1`   
It's enough to move -10 to the end of the array
`S = [-1, -1, -1, 1, 1, 1, 1] => 3`  
The negative elements at the beginning must be moved to the end to avoid debt at the start of the year  
`S = [5, -2, -3, 1] => 0`  
The schedule is already debt free

Assumptions:
* N is an integer within the range [1, 100,000]
* Each element of S is an integer within the range [-10,000,000, 10,000,000]
* The sum of all elements in S is non-negative
