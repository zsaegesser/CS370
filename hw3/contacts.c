/* Name: HackerRank -> Trie -> Contacts
 * Course: CS 370
 * Professor: Borowski
 * Assignment: Assignment 3
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

//We were able to pass all the tests on Hackerrank

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ALPHABET_LENGTH			26      //Length of the alphabet
#define OPERATION_BUF_SIZE		5       //Buffer size for operation string
#define NAME_BUF_SIZE			22      //Buffer size for contact name
#define ASCII_OFFSET			97	    //ASCII offset for lowercase characters

//Basic trie node struct
typedef struct node {
    int num_children;
    struct node *children[ALPHABET_LENGTH];
} trie_node;

trie_node* newNode() {
	trie_node* new = (trie_node*) malloc(sizeof(trie_node));

	new->num_children = 0;

	for (int i = 0; i < ALPHABET_LENGTH; ++i) {
		new->children[i] = NULL;
	}

	return new;
}

//find function to find number of contacts that match at least the partial 
//name given, searchterm.
int find(struct node* trie, char* searchTerm) {
	
    //if the trie is NULL, the 0 entries match at least searchTerm
    if (trie == NULL) {
		return 0;
	}

    //if the searchTerm is not NULL, return find on the trie of the next character in the searchTerm
	else if (*searchTerm){
        //if the next entry is null, it will return 0
		return find(trie->children[*searchTerm - ASCII_OFFSET], searchTerm + 1);
	}

    //the searchTerm is null terminated, therefore we have found the node we are looking for
	else {
        //return the number of children this node has
		return trie->num_children;
	}
}

//add the given name to the contacts trie and update values accordingly
void add(struct node* trie, char* name) {
    //increment the number of children of this ndoe
    //each node we visit will be incremented
    ++trie->num_children;

    //if the name value is null or is an empty string, return
	if (!*name) {
		return;
	}

    //if the node we are looking for doesn't exist, create it
	else if (!trie->children[*name - ASCII_OFFSET]) {
		trie->children[*name - ASCII_OFFSET] = newNode(); 
	}

    //continue calling add until the name string is empty
	add(trie->children[*name - ASCII_OFFSET], name + 1);
}

int main() {
	struct node* trie = newNode();   //create newNode that will be our Trie
	int numOperations;                                                                  //initialize numOperations

    //take in value for the number of operations we will undergo
	scanf("%d\n", &numOperations);
	for (int counter = 0; counter < numOperations; ++counter) {

		char* operation = (char *)malloc(OPERATION_BUF_SIZE * sizeof(char));    //allocate memory for possible length of operation string
		char* contact = (char *)malloc(NAME_BUF_SIZE * sizeof(char));           //allocate memory for possible length of name string

		scanf("%s %s", operation, contact);                                     //assign values to operation and contact name string

		//if add command
		if (operation[0] == 'a' && operation[1] == 'd' && operation[2] == 'd' && strlen(operation) == 3) {                                              //add operation
			add(trie, contact);
		}

		//if find command
		else if (operation[0] == 'f' && operation[1] == 'i' && operation[2] == 'n' && operation[3] == 'd' && strlen(operation) == 4) {                                         //find operation
			printf("%d\n", find(trie, contact));
		}

		//command entered is not supported
		else {
			printf("'add' and 'find' are the only supported commands...");
		}
		
        //free operation and contact in between iterations as we are done with them
        //and they are no longer required
		free(operation);
		free(contact);
	}

    //free trie from memory after execution of program
	free(trie);
}