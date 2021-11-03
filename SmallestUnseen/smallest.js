const smallestUnseenInt = (arr) => {
  const sortedA = arr.sort((a, b) => a - b);
  let smallest = sortedA[0];
  while(sortedA.includes(smallest)) {
    smallest++
  }
  return smallest <= 0? 1 : smallest;
}

console.info(smallestUnseenInt([1, 3, 6, 4, 1, 2])) // 5
console.info(smallestUnseenInt([1, 2, 3])) // 4
console.info(smallestUnseenInt([-5, -3, -1])) // 1
console.info(smallestUnseenInt([10, 1, 2, 3, 4, 5])) // 6
console.info(smallestUnseenInt([1, 3, 6, 7, 9, 13])) // 2
console.info(smallestUnseenInt([-3, -2, -1, 0, 1, 2])) // 3