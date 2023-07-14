/*

 *  Exes and Ohs

 *  Check to see if a string has the same amount of 'x's and 'o's. 
 *  The method must return a boolean and be case insensitive.
 *  The string can contain any char.

 *  Examples:

 *  XO("ooxx")      => true
 *  XO("xooxx")     => false
 *  XO("ooxXm")     => true
 *  XO("zpzpzpp")   => true // when no 'x' and 'o' is present should return true
 *  XO("zzoo")      => false


 * Task URL: https://www.codewars.com/kata/55908aad6620c066bc00002a

*/

function XO(str) {

    let stringLower = str.toLowerCase();
    let charArr = stringLower.split('');
    let xoList = ['o', 'x'];
    let x = 0;
    let o = 0;

    let compare = charArr.filter((char) => {
        xoList.includes(char)
        if (char === 'x') return x += 1
        if (char === 'o') return o += 1
    });

    if (x !== o && compare !== []) {
        return false
    };

    if (compare !== [] || compare === []) {
        return true
    };

};

console.log(XO("zzoo"))

