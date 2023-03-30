/*
 *  Break camelCase
 *  
 * 
 *  Complete the solution so that the function will
 *  break up camel casing, using a space between words.
 * 
 * Example
 *  
 *  "camelCasing"  =>  "camel Casing"
 *  "identifier"   =>  "identifier"
 *  ""             =>  ""
 * 
 * 
 * Task URL: https://www.codewars.com/kata/5208f99aee097e6552000148/javascript
 *  
*/

function solution(string) {

    let charPosition = string.search(/[A-Z]/);

    if (charPosition) {
        return string.split(/(?=[A-Z])/).join(' ');

    } else if (!charPosition) {
        return string;

    } else if (string === '') {
        return '';
    }

};

console.log(solution("camelCasingTest"))