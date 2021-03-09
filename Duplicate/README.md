## About this challenge
Returns a count of distinct case-insensitive alphabetic characters and numeric digits occurring more than once in an input string.
### Example
`klow` => `0 #no character repeated`
`klooww` => `2 # o and w are repeated once`
`indivisibility` => `1 # i is repeated six times`
`Indivisibilities` => `2 #i occurs seven times and s twice`
`Aa977` => `2 # a and 7 appears twice`
`OOBB` => `2`
### How to test
Pass the sentence argument on the terminal enclosed in quotes  
`python3 duplicate.py "DoesLifetellsuswhichwaybutwekeepignoring"`
Original challenge: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/