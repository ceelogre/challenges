const smallestUnseenInt = (arr) => {
  const set = new Set()
  arr.forEach(num => {
    set.add(num)
  })
  for (let i = 1; i < set.size; i ++) {
    if (set.has(i)) {
      continue
    } else {
      return i
    }
  }
  return set.size
  }

console.info(smallestUnseenInt([1, 2, 3])) // 4
console.info(smallestUnseenInt([9,9,9,9,9]))
console.info(smallestUnseenInt([10, 1, 2, 3, 4, 4, 5])) // 6
console.info(smallestUnseenInt([139, 394, 309,0932, 240]))
console.info(smallestUnseenInt([10, 1, 2, 3, 4, 4, 5])) // 6
console.info(smallestUnseenInt([1, 3, 6, 7, 9, 13])) // 2
console.info(smallestUnseenInt([-3, -2, -1, 0, 1, 2])) // 3
console.info(smallestUnseenInt([139, 394, 309,0932, 240])) // 1
console.info(smallestUnseenInt([-394, -4, 3490394]))
