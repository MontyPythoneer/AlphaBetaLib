## General Description
Pyalphabetica is a module to make editing and tweaking strings, lists, and dictionaries, easier. This module has many useful function and more will be coming. Here is a list of the ones that are available in pyalphabetica version 0.1.0: 
* alphanum
* numalpha
* caesar_cipher
* morse_code_encode
* morse_code_decode
* titleize
* reverse
* combine
* replace
* uppercase
* lowercase
* sentence_case
* capitalize

****

## Function Descriptions
**alphanum**:
Alphanum returns positions of each letter of the given string in the alphabet
e.g. abcdz ==> 1 2 3 4 26
It returns False if given string is not in the alphabet
e.g. 23 ==> False
Any characters other than numbers or letters will be unchanged

**numalpha**:
Numalpha returns the letter in the alphabet the given number corresponds to
e.g. 26 ==> z
It returns False if given number is not an integer\
Counting restarts from 1 if number is over 26
e.g. 27 ==> 'a'
Any characters other than numbers or letters will be unchanged
Any characters included must have a space between them otherwise a False value will be returned

**caesar_cipher**:
Caesar_cipher performs a Caesar Cipher Encryption using given key
Caesar Cipher Encryption shifts each letter of a string with the given key
e.g. caesar_encode('abcde', 1) ==> 'bcdef'
Negative keys shift the letter to the left
e.g. caesar_encode('abcde', -1) ==> 'zabcd'
Any characters other than letters will be unchanged

**morse_code_encode**:
Morse_code_encode converts a given string into Morse code with a dash as '-' and a dot as '.'

**morse_code_decode**:
Morse_code_decode converts a given morse code string back into a string.

**titleize**
Titleize converts a given string into a string suitable to use as a title.
e.g. the day of doom ==> The Day of Doom

**reverse**
Reverse returns the reverse of the given object
e.g. 'Hello World' ==> 'dlroW olleH'
e.g. [1, 2, 3, 4, 5] ==> [5, 4, 3, 2, 1]
e.g. {1:'a', 2:'b', 3:'c'} ==> {'a':1, 'b':2, 'c':3}
Any floats will be returned as is with no changes

**combine**
Combine combines the given arguments, regardless of the number, into a string value

**replace**
Replace replaces every given word in the given sentence with the given replacement. However, the word to be replaced must be seperated from the two words surrounding it with a space.
If the given word appears more than once in the given sentence, all of the words will be replaced.

**uppercase**
Uppercase turns an object into fully uppercase. If the object is a string, the letters in the string are made uppercase. If the object given is a list of strings, it will make all of the items in the list uppercase.

**lowercase**
Lowercase turns an objct into fully lowercase. If the object is a string, it will make all the letters in the string lowercase. If the object is a list of strings, it will make all the items in the list fully lowercase.

**sentence_case**
Sentence_case changes the case of a string into 'sentence' case, where only the first word is capitalised. If the given object is a list of strings, it will make all the items in the list 'sentence' capitalised.

**capitalize**
Capitalize capitalises all the words in a given string. If the given object is a list instead, it will capitalise all the words in each of the items in the list.

****

## Example Code
```
from pyalphabetica import morse_code_encode
message=input('What would you like to translate: ')
print('Morse Code: %s'%morse_code_encode(message))
```
```
from pyalphabetica import reverse
message=input('Enter a message to reverse: ')
print(reverse(message))
```
