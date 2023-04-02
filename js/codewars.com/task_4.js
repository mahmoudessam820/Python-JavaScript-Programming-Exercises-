/*
 *  Credit Card Mask
 * 
 *  Usually when you buy something, you're asked whether your credit card number,
 *  phone number or answer to your most secret question is still correct. 
 *  However, since someone could look over your shoulder, 
 *  you don't want that shown on your screen. Instead, we mask it.
 * 
 *  Your task is to write a function maskify, 
 *  which changes all but the last four characters into '#'.
 * 
 * Examples:
 * 
 *  "4556364607935616"      --> "############5616"
 *  "64607935616"           -->      "#######5616"
 *  "1"                     -->                "1"
 *  ""                      -->                 ""
 * 
 *  "What was the name of your first pet?"
 * 
 *  "Skippy"                                    --> "##ippy"
 *  "Nananananananananananananananana Batman!"  --> "####################################man!"
 * 
 *  Task URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
 * 
*/


function maskify(cc) {

    const creditCardNumber = cc.toString();

    if (creditCardNumber.length === 1 || creditCardNumber.length === 4) return cc;
    if (creditCardNumber === "") return "";

    let start = creditCardNumber.slice(0, -4);
    let end = creditCardNumber.slice(-4);
    let hash = '#';

    let hashedCreditCardNumber = hash.repeat(start.length).concat(end);

    return hashedCreditCardNumber;
}

console.log(maskify("Nananananananananananananananana Batman!"));