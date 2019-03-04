/*
DCP #4
------
Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
 does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/

let missingPositive = (arr) => {
  arr = arr.sort()
  for(let num of arr) {
    if(num < 0) {
      arr.shift()
    }
  }

  let i = arr[0]
  while(i in arr) {
    i++
    if(i != arr[i]) { return i }
  }
}

/*
Thought Process
---------------
The algorithm still needs improvement but the reasoning is that I take in an array
of arbitrary values and filter out all the negative values. Set i to be equal to the
first value in the array and iterate through the array, breaking if the incremented
value of i isn't found in the array.
*/
