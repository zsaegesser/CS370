import java.util.*;

/* Names: Project Euler #43
 * Course: CS 370
 * Professor: Borowski
 * Assignment: Assignment 2
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

// d2d3d4=406 is divisible by 2
// d3d4d5=063 is divisible by 3
// d4d5d6=635 is divisible by 5
// d5d6d7=357 is divisible by 7
// d6d7d8=572 is divisible by 11
// d7d8d9=728 is divisible by 13
// d8d9d10=289 is divisible by 17

class SubstringDivision {

	public ArrayList<String> arrayOfDigits;				//initialize array of digits

	public SubstringDivision(ArrayList<String> arr) {	//Initialize the array
		arrayOfDigits = arr;
	}

	public long startAlgo() {							//initialize the algorithm
		return pandigitAlgo(this.arrayOfDigits, "");
	}

	public long pandigitAlgo(ArrayList<String> panDigits, String strBuild) {
		long total = 0;

		//if the number of digits is 0, print and return the str
		if (panDigits.size() == 0) {
			System.out.println(strBuild);
			return Long.valueOf(strBuild);
		}
		
		//if there are digits to process
		else {
			int countToLength = 0;
			while (countToLength < panDigits.size()) {
				long tempstore = 0;
				int strlen = strBuild.length() + 1;
				String digit = panDigits.remove(countToLength);

				//build integer one by one to save time in calculation
				strBuild = strBuild.concat(digit);

				//if the length of our string is <= 3 then call it on the algorithm
				if (strlen <= 3) {
					tempstore = pandigitAlgo(panDigits, strBuild);	
				}
				//if the current string (with length less than 3) isn't divisible, then stop considering it immediately
				//this is done to save time
				else if (isDivisibleBy(strBuild.substring(strlen - 3, strlen), strlen)) {
					tempstore = pandigitAlgo(panDigits, strBuild);
				}

				panDigits.add(countToLength, digit);
				strBuild = strBuild.substring(0, strBuild.length() - 1);
				countToLength++;
				total += tempstore;
			}
			return total;
		}
	}

	//check if current 3 digit number is divisible 
	//(with respect to its position in the string)
	public boolean isDivisibleBy(String threeDigits, int strlen) {
		long num = Long.valueOf(threeDigits);
		boolean answer;

		switch (strlen) {
		case 4:
			answer = ((num % 2) == 0);
			break;
		case 5:
			answer = ((num % 3) == 0);
			break;
		case 6:
			answer = ((num % 5) == 0);
			break;
		case 7:
			answer = ((num % 7) == 0);
			break;
		case 8:
			answer = ((num % 11) == 0);
			break;
		case 9:
			answer = ((num % 13) == 0);
			break;
		case 10:
			answer = ((num % 17) == 0);
			break;
		default:
			answer = false;
			break;
		}
		return answer;
	}

	//check if the number given has duplicate integers in it
	public static boolean checkForDuplicates(String input) {
		for (int i = 0; i < input.length() - 1; i++) {
			for (int j = i + 1; j < input.length(); j++) {
				if (input.charAt(i) == input.charAt(j)) {
					return false;
				}
			}
		}
		return true;
	}

	public static void main(String[] argv) {
		String input = argv[0].toString();

		if (input.length() <= 3) {
			throw new IllegalArgumentException("Input length must be greater than 4");
		}
		else if (input.length() >= 11) {
			throw new IllegalArgumentException("Input length must be less than 10");
		}
		else if (!checkForDuplicates(input)) {
			throw new IllegalArgumentException("Cannot have duplicate digits");
		}
		else {

			//take the input and generate it into a str array
			ArrayList<String> geninput = new ArrayList<String>();
			String str[] = input.split("");
			for (int i = 0; i < input.length(); i++) {
				geninput.add(str[i]);
			}
			
			//initialize sum and array
			SubstringDivision pandigits = new SubstringDivision(geninput);
			long sum;
			
			//start time calculation and start algorithm
			long start = System.nanoTime();
			sum = pandigits.startAlgo();
			System.out.println("Sum: " + sum);
			System.out.printf("Elapsed time: %.6f ms\n", (System.nanoTime() - start) / 1e6);
		}

	}

}
