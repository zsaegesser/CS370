/* Name: SPOJ #29 - HASHIT
 * Course: CS 370
 * Professor: Borowski
 * Assignment: Assignment 4
 * @file contacts.c
 * @author: Aimal Wajihuddin
 * 			Zach Saegesser
 * 			Ryan Edelstein
 *
 * I pledge my honor that I have abided by the Stevens Honor System
 *							- Aimal Wajihuddin
 * 							- Zach Saegesser
 * 							- Ryan Edelstein
 */

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define TABLE_SIZE 101

//deleting a key isn't the same as it never existing
//use this to keep track of if something existed and now doesn't
char* DELETED = "deleted";

typedef struct {
	char* keys[TABLE_SIZE];
	int num_keys;
} hash_set;

void clear_table(hash_set* set) {

	int counter = 0;

	//while iterating through the table
	while (counter < TABLE_SIZE) {

		//re-initialize all values to NULL
		set->keys[counter] = NULL;
		++counter;
	}

	return;

}

int hash(char* key) {

	int total = 0;
	int counter = 0;
	int len = strlen(key);

	//for each character in the key
	while (counter < len) {
		
		//do ascii(keyletter) * position of letter
		total += (key[counter]) * (1 + counter);
		++counter;
	}

	//return as formula stated in SPOJ prompt
	//h(key)=19 *(ASCII(a1)*1+...+ASCII(an)*n).
	//Hash(key)=h(key) mod 101
	return (total * 19) % TABLE_SIZE;

}

int key_already_exists(hash_set* set, char* key) {

	int keyHash = hash(key);
	int curr = keyHash;
	int attempts = 0;

	//while we are under 20 attempts
	while (attempts < 20) {
		
		//set value of curr hashIndex as SPOJ states
		//(Hash(key)+j2+23*j) mod 101
		curr = (keyHash + (attempts * attempts) + (attempts * 23)) % TABLE_SIZE;

		//if value is null, nothing was ever set here, therefore return
		//it never existed
		if (set->keys[curr] == NULL) {
			return 0;
		}

		//if exists then return 1
		else if (strcmp(set->keys[curr], key) == 0) {
			return 1;
		}

		//came accross DELETED value for index
		//repeat until NULL found, key found, or 20 attempts
		++attempts;

	}

	return 0;

}

int insert_key(hash_set* set, char* key) {

	int keyHash = hash(key);
	int curr = keyHash;
	int attempts = 0;

	//if the key is already in the hash set, return early with "error" 1
	if (key_already_exists(set, key) != 0) {
		return 1;
	}

	//while under 20 attempts
	while (attempts <= 20) {

		//if current field (hash key) isn't populated
		if (set->keys[curr] == DELETED || set->keys[curr] == NULL) {
			//set current hash key to value and return
			set->keys[curr] = key;
			return 0;
		}

		//calculate collision resolvence as stated by SPOJ
		//(Hash(key)+j2+23*j) mod 101
		curr = (keyHash + (attempts * attempts) + (attempts * 23)) % TABLE_SIZE;
		++attempts;

	}

	return 1;

}

int delete_key(hash_set* set, char* key) {

	int keyHash = hash(key);
	int curr = keyHash;
	int attempts = 0;

	//while under 20 attempts
	while (attempts < 20) {

		//if hashKey index of key is already NULl, it never existed
		//exit out with "error" 1
		if (set->keys[curr] == NULL) {
			return 1;
		}
		
		//if value at current hashKey index isn't DELETED then a key exists here
		if (set->keys[curr] != DELETED) {
			//if this is the key we are looking for
			if (strcmp(key, set->keys[curr]) == 0) {
				//delete it and free the memspace and return
				free(set->keys[curr]);
				set->keys[curr] = DELETED;
				return 0;
			}
		}

		//calculate collision resolvence as stated by SPOJ
		//(Hash(key)+j2+23*j) mod 101
		curr = (keyHash + (attempts * attempts) + (attempts * 23)) % TABLE_SIZE;
		++attempts;

		//continue until 20 attempts

	}

	//the key we are looking to delete wasn't found
	//return with "error" 1
	return 1;

}

void display_keys(hash_set* set) {

	int counter = 0;

	//pretty straight forward
	//print all of the keys and hashes
	while (counter < TABLE_SIZE) {
		if (set->keys[counter] != NULL && set->keys[counter] != DELETED) {
			printf("%i:%s\n", counter, set->keys[counter]);
		}
		++counter;
	}

	return;

}

int main() {

	//initialize the testCase and operations variables
	int testCases;
	int operations;

	//initialize hashSet, inputStr, and key, and malloc accordingly
	hash_set* hashSet = (hash_set*) malloc(sizeof(hash_set));
	char* inputStr = (char*) malloc(sizeof(char) * 19);
	char* key;

	scanf("%d", &testCases);

	//while we have more testCases to run
	while (testCases > 0) {

		//get number of operations to take in and run
		scanf("%d", &operations);

		//while we have more operations to execute
		while (operations > 0) {

			//take in current inputString
			scanf("%s", inputStr);
			//is command 'A' for ADD or 'D' for DEL
			char command = inputStr[0];

			key = (char*) malloc(sizeof(char) * 15);
			//copy the actual string to the key variable
			strncpy(key, inputStr + 4, 15);

			//if command is delete
			if (command == 'D') {
				//if no error encountered with delete, decrement num_keys
				if (delete_key(hashSet, key) == 0) {
					--hashSet->num_keys;
				}
			}

			//if command is add
			else {
				//if no error encountered with add, increment num_keys
				if (insert_key(hashSet, key) == 0) {
					++hashSet->num_keys;
				}
			}
			
			//decrement operations after current operation executed
			--operations;

		}

		printf("%i\n", hashSet->num_keys);		//print current number of keys
		display_keys(hashSet);					//display all keys
		clear_table(hashSet);					//clear the table

		hashSet->num_keys = 0;					//reinitialize num_keys to 0
		--testCases;							//decrement testCases 
		free(key);								//free the key

	}

	//free the rest of the variables and exit out.
	free(hashSet);
	free(inputStr);

}