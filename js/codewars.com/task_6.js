/*
 *  Scramblies
 *  
 *  Complete the function scramble(str1, str2) that returns true if 
 *  a portion of str1 characters can be rearranged to match str2, 
 *  otherwise returns false.
 * 
 * Notes:
 * 
 * Only lower case letters will be used (a-z). 
 * No punctuation or digits will be included.
 * Performance needs to be considered.
 * 
 * Examples:
 * 
 * scramble('rkqodlw', 'world') ==> True
 * scramble('cedewaraaossoqqyt', 'codewars') ==> True
 * scramble('katas', 'steak') ==> False
 * 
 * 
 * Task URL: https://www.codewars.com/kata/55c04b4cc56a697bb0000048
 *  
*/

function scramble(str1, str2) {

    const stringOne = str1.split('');
    const stringTwo = str2.split('');
    const charCounts = {};

    for (let i = 0; i < stringOne.length; i++) {

        const char = stringOne[i];

        if (charCounts[char]) { // character already seen

            charCounts[char]++;

        } else {  // first time seeing character

            charCounts[char] = 1;
        }
    };

    for (let i = 0; i < stringTwo.length; i++) {

        const char = stringTwo[i]

        if (!charCounts[char]) {

            return false;
        }
        charCounts[char]--;
    };

    return true;

};

console.log(scramble('scriptjavx', 'javascript'))
