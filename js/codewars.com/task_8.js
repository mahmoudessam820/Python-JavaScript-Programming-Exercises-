/*
 *  Extract the domain name from a URL
 *  
 * 
 *  Write a function that when given a URL as a string, 
 *  parses out just the domain name and returns it as a string.
 *  
 * 
 * Example
 *  
 * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
 * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
 * url = "https://www.cnet.com"                -> domain name = cnet"
 * 
 * 
 * Task URL: https://www.codewars.com/kata/514a024011ea4fb54200004b/javascript
 *  
*/


function domainNameOne(url) {

    return url.replace(/^https?:\/\//, "").replace(/^www\./, "").replace(/\..*/, "");

};


function domainNameTwo(url) {

    return url.match(/(?:http(?:s)?:\/\/)?(?:w{3}\.)?([^\.]+)/i)[1];
}


function domainNameThree(url) {

    return url.replace(/.+\/\/|www.|\..+/g, '');
}


console.log(domainNameThree('http://github.com/carbonfive/raygun'));
console.log(domainNameThree('http://www.zombie-bites.com'));
console.log(domainNameThree('https://www.cnet.com'));
console.log(domainNameThree('https://www.google.com'));