## Boring Numbers
From Google Kick Start 2020.

### Problem
Ron read a book about boring numbers. According to the book, a positive number is called boring if all of the digits at even positions in the number are even and all of the digits at odd positions are odd. The digits are enumerated from left to right starting from 1. For example, the number 1478 is boring as the odd positions include the digits {1, 7} which are odd and even positions include the digits {4, 8} which are even.

Given two numbers L and R, Ron wants to count how many numbers in the range [L, R] (L and R inclusive) are boring. Ron is unable to solve the problem, hence he needs your help.
### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line with two numbers L and R.

### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the count of boring numbers.

### Limits
Time limit: 20 seconds.  
Memory limit: 1 GB.  
1 ≤ T ≤ 100.  
Test Set 1 . 
1 ≤ L ≤ R ≤ 10<sup>3</sup>.  
Test Set 2 . 
1 ≤ L ≤ R ≤ 10<sup>18</sup>.  

Sample

Input
 	
 
3  
5 15  
120 125  
779 783  

Output  
  
Case #1: 6  
Case #2: 3  
Case #3: 2  

Original challenge: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6