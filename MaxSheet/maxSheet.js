
const convert = (s, c) => {
  // get the first row
  firstRow = s.split('\n', 1)
  // get the columns
  columns = firstRow.join().split(',')

  dataRowsLength = s.split('\n').length -1
  allRowsValues = s.split('\n')

  dataArray = []
  
  for (let index = 1 ; index < allRowsValues.length; ++index) {
    values = allRowsValues[index].split(',')
    dataArray.push(values)
  }

  // find the index of c
  cIndex = columns.findIndex(elt => elt === C)
  columnValues= []
  // convert
  for (let i = 0; i < dataRowsLength; i++) {
    columnValues.push(dataArray[i][cIndex])
  }

  // convert to numbers
  nVals = columnValues.map (Number)
  return Math.max.apply(null, nVals)
}

S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"
S= 'city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto,-1,-2'
C = 'temp'
m = convert(S, C)
console.info(m)
S = "city,seaLevel\nPrague,-10\nBrno,-5\nOstrava,-7\nPraha,-8"
C = "seaLevel"
console.info(convert(S, C))


S = "area,land\n34,West\n18,East\n40,North\n12,South" 
C = "area"
console.info(convert(S, C))