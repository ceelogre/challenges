// Given a string, return unique letters followed by its number of occurrences.
const returnLettersAndOccurrences = (str) => {
  const uniqueLetters = new Set(str)
  const letters = Array.from(uniqueLetters).sort()
  const occurrences = letters.map(letter => str.split(letter).length - 1)
  return { letters, occurrences }
}

const returnLettersAndOccurrence = (str) => {
  const uniqueLetters = new Set(str)
  const lettersAndOccurrences = []
  for (const letter of uniqueLetters) {
    lettersAndOccurrences.push(
      // Add the letter and its occurrence to the array as an object
      {letter, occurrence: str.split(letter).length - 1}
      )
  }
  return lettersAndOccurrences
}

console.info(returnLettersAndOccurrences('ubluue'))