# Warehouse Manager
In a warehouse, a manager would like to sort items in a stock. Given a list of n items, sort them in ascending order, first by the number of items with a certain value, and then by the value of the items.

*Example*: 
n = 6
items = [4,5,6,5,4,3]

* There are 2 values that occur twice: [4,4, 5,5]
* There are 2 values that occur once: [3,6]
* The items sorted by quantity then by value in ascending order is: [3,6,4,4,5,5]

*Example 2*
n = 10
items = [8,5,5,5,5,1,1,1,4,4]
output: [8, 4,4,1,1,1,5,5,5,5]

*Note:* for the first solution with lists of size 100,000 there won't be any output as the program will run out of memory with a `maximum recursion depth exceeded` error.