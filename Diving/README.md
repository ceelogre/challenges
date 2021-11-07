## Hold your breath

You will be given an array of numbers which represent your character's altitude above sea level at regular intervals:

Positive numbers represent height above the water.
0 is sea level.
Negative numbers represent depth below the water's surface.
Create a function which returns whether your character survives their unsupervised diving experience, given an array of integers.

Your character starts with a maximum breath meter of 10, and you can replenish your breath by 4 for every item in the array which you are at or above sealevel.

However, when diving underwater, your breath meter decreases by 2 per item in the array. Watch out, if your breath diminishes to 0, your character dies!

Worked Example
`divingMinigame([-5, -15, -4, 0, 5]) ➞ true`

Breath meter starts at 10.
-5 is below water, so breath meter decreases to 8.
-15 is below water, so breath meter decreases to 6.
-4 is below water, so breath meter decreases to 4.
0 is at sea level, so breath meter increases to 8.
5 is above sea level and breath meter is capped at 10 (would've been 12 otherwise).
Character survives!

Examples:
  `divingMinigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ true`
  `divingMinigame([-3, -6, -2, -6, -2]) ➞ false`
  `divingMinigame([2, 1, 2, 1, -3, -4, -5, -3, -4]) ➞ false`

Notes:
  Lists may be of any length.
  All arrays are valid.