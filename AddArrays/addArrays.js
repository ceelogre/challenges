const addArrays = (arr1, arr2) => {
  let arr3 = []
  for (let i = 0; i < arr2.length;  ++i)
    arr3.push(arr1[i] + arr2[i])
  return arr3
}

console.info(addArrays([7, 8, 2], [1, 3, 8]))
console.info(addArrays([3, 5, -2], [9, 1, 0]))