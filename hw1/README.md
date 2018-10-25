Assignment 1: Project Euler 13
===

## Team Members
- Aimal Wajihuddin
- Zach Saegesser
- Ryan Edelstein


## Steps to run the assignment
1. Install NodeJS.

    You can install it for your respective system/package manager by looking [here](https://nodejs.org/en/download/package-manager/).
2. After installing Node.JS, navigate into the folder with `largesum.js` and package.json in your desired shell, and run the following command

        npm install

    This will install the required packages required to run the homework assignment. We only used `fs-extra` in order to parse data from files.

3. To run the test cases that we made, you will need to go into `testfiles` and run `testscript.py`.

    Note: In order to run `testscript.py` you will need to install naked through pip by running the following command. Also, this is in Python 2, NOT Python 3.

        pip install naked

    If you do not have pip installed, you can do so by following the guide [here](https://pip.pypa.io/en/stable/installing/).

4. We oriinally used the 'testscript.py' file to generate the 'output.txt' files. We could do this because Python has built in BigIntegers, but after generating the output files we changed its use to just reading the output files and comparing them with the output of 'largesum.js'.
5. In order to run the 'largesum.js' program with any set of data, you will need to put the data in the file called `input.txt`. The output will be given in the terminal window.


