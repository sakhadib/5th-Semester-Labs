#include <stdio.h>
#include <stdlib.h>

int main() {

    char *ptrName;
    char fullName[] = "Md. Ishmam Uddin";

    // TODO : initialize ptrName to point to fullName. Problem is uninitialized pointer
    ptrName = fullName;  
    printf("My name is %s\n",ptrName);

    int *ptrSalary = (int*) malloc(sizeof(int));

    // TODO : Typo -> extra 'l' in salary
    *ptrSalary = 1000;
    printf("My salary is %d\n",*ptrSalary);
    free(ptrSalary); // Free memory after use

    // TODO : Again Allocating to an int pointer
    ptrSalary = (int*) malloc(sizeof(int));
    *ptrSalary = 2000; 
    printf("After promotion my salary will be %d\n",*ptrSalary);


    // TODO : Free after use
    free(ptrSalary);
    ptrSalary = NULL; 


    // TODO : Alphabet size is 26
    char* alphabet = (char*) malloc(27);
    for(int i = 0; i < 26; i++){
        alphabet[i] = i + 'A';
    }
    alphabet[26] = '\0';

    // TODO : Use alphabet as it is instead of subtracting 26. Problem was accessing invalid memory
    // char* revAlphabet = alphabet - 26;
    // for(int i=0;i<26;i++)revAlphabet[i] = 'Z'-i;

    // TODO : Make the order reverse
    for(int i = 0; i < 26; i++){
        alphabet[i] = 'Z' - i;
    }

    // TODO : Print alphabet in reverse order
    printf("Reverse Alphabet : %s\n", alphabet);

    return 0;
}