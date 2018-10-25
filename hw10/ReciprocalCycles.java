//  Name: ReciprocalCycles
//  Course: CS 370
//  Professor: Borowski
//  Assignment: Assignment 10
//  @file ReciprocalCycles.py
//  @author: Aimal Wajihuddin
//  			Zach Saegesser
//  			Ryan Edelstein
//
//  I pledges my honor that I have abided by the Stevens Honor System
// 							- Aimal Wajihuddin
//  							- Zach Saegesser
//  							- Ryan Edelstein

public class ReciprocalCycles {
	//Global Variables
	private int intervalLen;
	public int denominator;
	//array of decimal values #1
	private int[] decVal1;
	//array of decimal values #2
	private int[] decVal2;
	private int indEnd;
	private int indInit;
	// has leading decimal --> confirmed
	private boolean ldconfirm;

	/*
		Function: divisorFind -
		This function checks to see if the input num is divisible by 2 or 5.
	*/
	public boolean divisorFind(int num) {
		if ((num % 2) == 0) {
			return false;
		}
		else if((num%5) ==0){
			return false;
		}
		return true;
	}
	/*
		function: cycleLen -
		This function checks and finds the length of the decimal cycle.
	*/
	public int cycleLen(int num, int rem) {
		if (rem == 0) {
			intervalLen = 1;
			int remainder = 2;
			int product = 10;
			while (remainder != rem) {
				decVal1[++indInit] = product / num;
				remainder = product % num;
				product = remainder * 10;
				intervalLen++;
			}
		} else {
			intervalLen = 0;
			int remainder = 2;
			int product = 10;
			while (remainder != rem) {
				if (!ldconfirm) {
					decVal2[++indEnd] = product / num;
				}
				remainder = product % num;
				product = remainder * 10;
				intervalLen++;
			}
		}
		return intervalLen;
	}
	/*
		Function: decimalRep -
		This function takes in a number and, should the number have any
		2's or 5's, the leading decimal then dictates the repeating deicmal.
	*/
	public void decimalRep(int oddNum) {
		//the remainder == decimal value array #1 mod input(oddNum)
		int remainder = decVal1[0] % oddNum;
		decVal1[0] = decVal1[0] / oddNum;
		int tempOne = 1;
		int tempZero = 0;
		while(tempOne <= indInit){
			remainder = remainder * 10 + decVal1[tempOne];
			decVal1[tempOne] = remainder / oddNum;
			remainder = remainder % oddNum;
			tempOne++;
		}
		while(tempZero<= intervalLen){
			remainder = remainder * 10;
			decVal2[tempZero] = remainder / oddNum;
			remainder = remainder % oddNum;
			indEnd++;
			tempZero++;
		}
		indEnd--;
	}
	/*
		Function: ReciprocalCycles
		calls other functions and initiates everything.
	*/
	public ReciprocalCycles(int inputNum) {
		int leadingProd;
		intervalLen = 1;
		// set denominator as input
		denominator = inputNum;
		decVal2 = new int[inputNum];
		indInit = -1;
		indEnd = -1;
		ldconfirm = false;
		int oddNum = 1;
		// If not divisorFind on the input,
		// (divisor find checks to see if the number has 2 or 5 as factors)
		if (!divisorFind(inputNum)) {
			leadingProd = 1;
			int numOne = 0;
			// while the denominator is divisible by 2 and the remainder is 0.
			// divide by 2, multiply the leading product by 2 and increment the
			// number of evens.
			while ((inputNum % 2) == 0) {
				inputNum = inputNum / 2;
				leadingProd = leadingProd * 2;
				numOne++;
			}
			// while the denominator is divisible by 5 and the remainder is 0.
			// divide by 2, multiply the leading product by 5 and increment the
			// number of evens.
			while ((inputNum % 5) == 0) {
				inputNum = inputNum/5;
				leadingProd = leadingProd * 5;
				numOne++;
			}
			ldconfirm = true;
			decVal1 = new int[numOne];
			cycleLen(leadingProd, 0);
			oddNum = denominator / leadingProd;
		}
		if (inputNum > 1) {
			int numZero = cycleLen(inputNum, 1);
			if (ldconfirm) {
				decimalRep(oddNum);
			}
		}
	}

	/*
		Function: toString -
		This prints the answer given an input. In this case, denominator refers to
		the value given by the user within range [1, 2000]
	*/
	public String toString() {
		String ans = "1/"+denominator+" = 0.";
		int indCheck = 0;
		while(indCheck <= indInit){
			ans += decVal1[indCheck];
			indCheck++;
		}
		if (indEnd > -1) {
			ans += "(";
		}
		for (int i = 0; i <= indEnd; ++i) {
			ans += decVal2[i];
		}
		if (indEnd > -1) {
			ans += "), cycle length "+intervalLen;
		}
		return ans;
	}
	/*
		Function: isInt -
		This function is here to check if the input argument is an intger.
		str refers to args[0], or the input from the command line, and then is
		checked to see if it is an integer. if it is an integer, return true,
		else return false.
	*/
	public static boolean isInt(String str){
	try{
			Integer.parseInt(str);
			return true;
		} catch (NumberFormatException e){
			 return false;
		}
	}
	/*
		Function: Main -
		The main function in which everything is initiated and called. The error checking
		is as follows:
			- is the argument of at least lenth 1
			- is the argument provided the correct data type.
			- is the argument within the bounds of the assignment. In this case,
				the bounds are [1, 2000]
			- if all other conditions pass, proceed with rest of the function calls.
	*/
	public static void main(String[] args) {
		if (args.length != 1) {
			System.out.println("Usage: java ReciprocalCycles <denominator>");
		} else {
			int inputDenominator = 0;
			if (isInt(args[0]) == false) {
				System.out.println("Error: Denominator must be an integer in [1, 2000]. Received '" + args[0] + "'.");
				return;
			}
			inputDenominator = Integer.parseInt(args[0]);
			if (inputDenominator < 1 || inputDenominator > 2000) {
				System.out.println("Error: Denominator must be an integer in [1, 2000]. Received '" + args[0] + "'.");
			}
			// check to see if the input is 1.
			else if (inputDenominator == 1) {
				System.out.println("1/1 = 1");
			} else {
				ReciprocalCycles rc = new ReciprocalCycles(inputDenominator);
				System.out.println(rc.toString());
			}
		}
	}
}