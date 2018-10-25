/* Names: Project Euler #13
 * Course: CS 370
 * Professor: Barresi
 * Assignment: Assignment 1
 * @file largesum.js
 * @author: Aimal Wajihuddin
 * 			Zach Saegesser
 * 			Ryan Edelstein
 *
 * I pledge my honor that I have abided by the Stevens Honor System
 *							- Aimal Wajihuddin
 * 							- Zach Saegesser
 * 							- Ryan Edelstein
 */

const fs = require("fs-extra");


/**
 * Resolves a string with the contents of the files in the path
 * @async
 *
 * @param {string} path - a file path
 */
async function listOfNumbers(path) {

	try {
		if (typeof(path) != 'string') {
			throw TypeError('Path must be a string!');
		}
		if (!(await fs.exists(path))) {
			throw Error("The data file 'input.txt' does not exist")
		}
		let file = await fs.readFile(path,'utf-8');
		let list = file.split("\n");

		return list;
	}
	catch (e) {
		throw e;
	}

}

/**
 * Adds two numbers that are represented as a string
 *
 * @param {string} num1 - a string representation of a number
 * @param {string} num2 - a string representation of a number
 */
function addTwoNumbers(num1, num2) {

	try{
		let carry = 0
		let retStr = ""
		let num1Index = num1.length - 1;
		let num2Index = num2.length - 1;

		while (num1Index >= 0 || num2Index >= 0 || carry != 0) {
			let digit1 = num1Index >= 0 ? parseInt(num1.charAt(num1Index--)) : 0;
			let digit2 = num2Index >= 0 ? parseInt(num2.charAt(num2Index--)) : 0;
			let newDigit = digit1 + digit2 + carry;

			if (newDigit < 10) {
				carry = 0;
			}
			else {
				carry = 1;
				newDigit -= 10;
			}

			retStr = newDigit + retStr;
		}

		return retStr;
	}
	catch(e) {
		throw e;
	}
}

/**
 * Adds all numbers (that are represented as strings) in a list
 *
 * @param {object} num1 - a list of numbers represented as strings
 */
function addAllNumbers(listOfNums) {

	try{
		let retNumber = addTwoNumbers(listOfNums[0],listOfNums[1]);
		let newListOfNums = listOfNums.slice(2);
		let listLength = newListOfNums.length
		let i = 0

		while (i < listLength) {
			retNumber = addTwoNumbers(retNumber,newListOfNums[i++]);
		}

		return retNumber
	}
	catch(e) {
		throw e;
	}

}

/**
 * Takes in a file and returns the sum of all of the numbers inside
 * @async
 *
 * @param {string} fileOfNums - the path to a file
 */
async function addNums(fileOfNums) {

	try {
		let nums = await listOfNumbers(fileOfNums);
		let totalSum = 0;

		if (nums == undefined || nums[0] == "") {
			throw Error("The file input.txt does not contain any numbers");
		}
		else if (nums.length == 1) {
			totalSum = parseInt(nums[0]).toString();
		}
		else {
			totalSum = addAllNumbers(nums).replace(/^0+/,'');
		}

		if (totalSum === "") {
			totalSum = "0";
		}

		console.log(`Full sum: ${totalSum}\nFirst 10 digits: ${totalSum.substr(0,10)}`);
	}
	catch(e) {
		throw e;
	}
}

//This flag is used for the calling largesum.js from testscript.py for comapring answers
//This is NOT to be used by the user manually. It WILL NOT work
if(process.argv.length > 2){
	if(process.argv[2] == '-test'){
		addNums(`test${process.argv[3]}.txt`).catch(e => console.error(e));
	}
}

//This is for all normal calls to largesum.js by the user
else {
	addNums("input.txt").catch(e => console.error(e));
}
