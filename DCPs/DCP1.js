/*
DCP #1
------
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/

let sumTwo = (arr, k) => {
  for(let num of arr) {
    if(arr.includes(k - num)) { return true }
  }
  return false
}

/*
Thought Process
---------------
Given an array and an integer that is the SUM of two numbers from within the array,
a quick solution is to loop through the array and check if any of the numbers you pass
can be subtracted from the sum total to give a value that exists somewhere in the array
other than the current index. If the value exists within the array then you know that k
can be created from at least two values found in arr.
*/
