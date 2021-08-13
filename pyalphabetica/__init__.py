__all__=[
    'alphanum', 'numalpha', 'caesar_cipher', 'morse_code_encode', 'morse_code_decode',
    'titleize', 'reverse', 'combine', 'replace', 'uppercase', 'lowercase', 'sentence_case',
    'capitalize'
    ]

def alphanum(string):
    """Returns positions of each letter of the given string in the alphabet
e.g. abcdz ==> 1 2 3 4 26
Returns False if given string is not in the alphabet
e.g. 23 ==> False
Any characters other than numbers or letters will be unchanged"""
    end=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    string=str(string)
    for letter in string:
        letter=str(letter)
        if letter.isalpha():
            try:
                end.append(str(alphabet.index(letter)+1))
                end.append(' ')
            except:
                end=False
        else:
            try:
                letter=int(letter)
                end=False
            except:
                end.append(letter)
                end.append(' ')
    try:
        return "".join(end)
    except:
        return end
            

def numalpha(numbers):
    """Returns the letter in the alphabet the given number corresponds to
e.g. 26 ==> z
Returns False if given number is not an integer
e.g. q ==> False
e.g. 2.5 ==> False
Counting restarts from 1 if number is over 26
e.g. 27 ==> 'a'
Any characters other than numbers or letters will be unchanged
Any characters included must have a space between them otherwise a False value will be returned"""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    end=[]
    numbers=str(numbers)
    numbers=numbers.split()
    
    for num in numbers:
        if num in punctuation or num in quotation:
            end.append(num)
        elif num in alphabet:
            end=False
        else:
            try:
                end.append(alphabet[int(num)-1])
            except:
                if int(num)>26:
                    end.append(alphabet[int(num)%26-1])
                else:
                    end=False
    try:
        return " ".join(end)
    except:
        return end

def caesar_cipher(string, key):
    """Performs Caesar Cipher Encryption using given key
Caesar Cipher Encryption shifts each letter of a string with the given key
e.g. caesar_encode('abcde', 1) ==> 'bcdef'
Negative keys shift the letter to the left
e.g. caesar_encode('abcde', -1)==> 'zabcd'
Any characters other than letters will be unchanged"""
    end=[]
    for letter in string:
        if letter.isalpha():
            end.append(numalpha(int(alphanum(letter))+key))
        else:
            end.append(letter)
    try:
        return "".join(end)
    except:
        return end
    
def morse_code_encode(string):
    """Encodes a string into Morse code."""
    morse={'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',\
     'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',\
     'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',\
           '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',\
           '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',\
           ':': '-..-.', ';': '---...', '+': '-.-.-.', '-': '-....-', '=': '-...-'}
    end=[]
    string=str(string)
    for letter in string:
        letter=str(letter)
        try:
            end.append(morse[letter.lower()])
        except:
            end.append(letter)
    return " ".join(end)

def morse_code_decode(string):
    """Decodes morse code into string."""
    end=[]
    string=str(string)
    morse={'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i',\
           '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q',\
           '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',\
           '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',\
           '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.', '--..--': ',', '..--..': '?',\
           '.----.': "'", '-..-.': ':', '---...': ';', '-.-.-.': '+', '-....-': '-', '-...-': '='}
    end=[]
    string=string.split()
    for code in string:
        try:
            end.append(morse[code].upper())
        except:
            end.append(code)
    return "".join(end)

def titleize(string):
    """Converts a given string into a string suitable to use as a title
e.g. the day of doom ==> The Day of Doom"""
    untitleizes=['of', 'and', 'the', 'in', 'if', 'for', 'so', 'to', 'my']
    string=string.split()
    end=[]
    for word in string:
        if not word in untitleizes:
            end.append(word.capitalize())
        else:
            if word==string[0] or word==string[-1]:
                end.append(word.capitalize())
            else:
                end.append(word.lower())
    return " ".join(end)

def reverse(obj):
    """Returns the reverse of the given object
e.g. 'Hello World' ==> 'dlroW olleH'
e.g. [1, 2, 3, 4, 5] ==> [5, 4, 3, 2, 1]
e.g. {1:'a', 2:'b', 3:'c'} ==> {'a':1, 'b':2, 'c':3}
e.g. 146 ==> 641
Any floats will be returned as is with no changes"""
    if isinstance(obj, str):
        return "".join(reversed(obj))
    if isinstance(obj, list):
        return [obj[-x] for x in range(1, len(obj)+1)]
    if isinstance(obj, dict):
        ret={}
        for item in obj:
            ret[obj[item]]=item
        return ret
    if isinstance(obj, int):
        return int("".join(reversed(str(obj))))
    if isinstance(obj, float):
        return obj

def combine(*args):
    """Combines given arguments into a string value"""
    return "".join([str(x) for x in args])

def replace(sentence, word, replacement):
    """Replaces every given word in the given sentence with the given replacement
However, the word to be replaced must be seperated from the words around it with
a space
If the given word appears more than once in the given sentence,
all of the words will be replaced"""
    i=0
    if not isinstance(sentence, str):
        raise TypeError("Invalid sentence type '%s'"%str(type(sentence)))
    if not word in sentence.split():
        raise Exception("Word to replace '%s' cannot be found in given sentence '%s'"%(word, sentence))
    else:
        sentence=sentence.split()
        for each in sentence:
            if each==word:
                sentence[i]=replacement
            i+=1
        return " ".join(sentence)

def uppercase(obj):
    """Turns an object into uppercase. If the object is a string, it will make all the
letters in the string uppercase.
If the object is a list of strings, it will make all the items in the list uppercase."""
    if not (isinstance(obj, str) or isinstance(obj, list)):
        raise TypeError("Expected list or str instance, recieved instance of '%s'"%str(type(obj)))
    else:
        if isinstance(obj, str):
            return obj.upper()
        if isinstance(obj, list):
            try:
                end=[string.upper() for string in obj]
                return end
            except:
                raise ValueError("Invalid list input '%s'"%obj)

def lowercase(obj):
    """Turns an object into lowercase. If the object is a string, it will make all the
letters in the string lowercase.
If the object is a list of strings, it will make all the items in the list lowercase."""
    if not (isinstance(obj, str) or isinstance(obj, list)):
        raise TypeError("Expected list or str instance, recieved instance of '%s'"%str(type(obj)))
    else:
        if isinstance(obj, str):
            return obj.lower()
        if isinstance(obj, list):
            try:
                end=[string.lower() for string in obj]
                return end
            except:
                raise ValueError("Invalid list input '%s'"%obj)

def sentence_case(obj):
    """Changes the case of a string into 'sentence' case, where only the first
word is capitalised. If the given object is a list of strings, it will make all
the items in the list 'sentence' capitalised."""
    case=0
    end=[]
    if not (isinstance(obj, str) or isinstance(obj, list)):
        raise TypeError("Expected list or str instance, recieved instance of '%s'"%str(type(obj)))
    else:
        if isinstance(obj, str):
            end.append(obj.split()[0].capitalize())
            for word in obj[len(obj.split()[0]):len(obj)+1].split():
                end.append(word)
            return " ".join(end)
        if isinstance(obj, list):
            return [sentence_case(str(string)) for string in obj]

def capitalize(obj):
    """Capitalises all the words in a given string.
If the given object is a list instead, it will capitalise all the words in each of
the items in the list."""
    if not (isinstance(obj, str) or isinstance(obj, list)):
        raise TypeError("Expected list or str instance, recieved instance of '%s'"%str(type(obj)))
    else:
        if isinstance(obj, str):
            return " ".join([string.capitalize() for string in obj.split()])
        if isinstance(obj, list):
            return [capitalize(str(string)) for string in obj]
