/*
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
*/

let productArr = (arr) => {
  let array = []
  for(let x = 0; x < arr.length; x++) {
    let prod = 1
    for(let j = 0; j < arr.length; j++) {
      if(x == j) {
        continue
      } else {
        prod *= arr[j]
      }
    }
    array.push(prod)
  }
  return array
}

let products = (arr) => {
  // NOTE: pre & post arrays have same length as original arr
  // Takes a running total of the products starting with the first array value
  let pre_products = []
  let post_products = []
  let array = []

  if(arr.length <= 2) { return ([...arr]) }

  for(let num of arr) {
    if(pre_products.length == 0) { pre_products.push(num) }
    else { pre_products.push(pre_products[pre_products.length - 1] * num) }
  }

  for(let num of arr.reverse()) {
    if(post_products.length == 0) { post_products.push(num) }
    else { post_products.push(post_products[post_products.length - 1] * num) }
  }
  post_products = post_products.reverse()

  for(let num in arr) {
    if(num == 0) { array.push(post_products[1]) }
    else if (num == arr.length - 1) { array.push(pre_products[arr.length - 2]) }
    else { array.push(pre_products[--num] * post_products[++num + 1]) }
  }
  return array
}

/*
Thought Process
---------------
Without using division, we just move through the loop within a nested loop to make sure
that we take the product of every position except the current index. This process
basically just takes the products of every element except the ith index which can be
broken down a bit more to escape the O(n^2) time.

The improved solution is slightly less intuitive
*/
