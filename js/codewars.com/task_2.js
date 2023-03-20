/*

 *  Isograms

 *  An isogram is a word that has no repeating letters 
 *  consecutive or non-consecutive. 

 *  Implement a function that determines whether a string that 
 *  contains only letters is an isogram. Assume the empty string is an isogram.

 *  Ignore letter case.

 *  Examples:

 *  "Dermatoglyphics" --> true
 *  "aba" --> false
 *  "moOse" --> false (ignore letter case)
 * 
 * Task URL: https://www.codewars.com/kata/isograms/train/javascript

*/

// My solution

function isIsogramOne(str) {
    let strLower = str.toLowerCase(); // convert to lowercase
    let charArr = strLower.split(''); // split into array 
    let result = []; // create empty array to store unique characters
    for (let i = 0; i < charArr.length; i++) { // loop through array
        if (result.indexOf(charArr[i]) === -1) { // if chraacter is not in array
            result.push(charArr[i]); // push character to array 
        }
    }
    return result.length === charArr.length;
}
console.log(isIsogramOne('Dermatoglyphics'));
console.log(isIsogramOne('aba'));


// Another solution 

function isIsogramTow(str) {
    return str.toLowerCase().split('').filter((item, index, array) =>
        array.indexOf(item) === index).length === str.length;
}

console.log(isIsogramTow("Dermatoglyphics"));
