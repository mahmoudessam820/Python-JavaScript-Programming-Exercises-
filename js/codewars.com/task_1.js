/*
    Array.diff

    - Your goal in this kata is to implement a difference function.
    - Which subtracts one array from another and returns the result.
    - It should remove all values from array [a].
    - Which are present in array [b] keeping their order.

    Examples:

    arrayDiff([1,2],[1]) == [2]

    If a value is present in b, 
    All of its occurrences must be removed from the other:

    ArrayDiff([1,2,2,2,3],[2]) == [1,3]

    Task URL: https://www.codewars.com/kata/523f5d21c841566fde000009

*/

// My solution:

let arr1 = [1, 2, 2, 2, 3];
let arr2 = [2];

function arrayDiff(a, b) {
    let result = []
    for (let i = 0; i < a.length; i++) {
        if (b.indexOf(a[i]) === -1) {
            result.push(a[i])
        }
    }
    return result;
}
console.log(arrayDiff(arr1, arr2))