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


function domainName(url) {

    return url.replace(/^https?:\/\//, "").replace(/^www\./, "").replace(/\..*/, "");

};

console.log(domainName('http://github.com/carbonfive/raygun'));
console.log(domainName('http://www.zombie-bites.com'));
console.log(domainName('https://www.cnet.com'));