#1.  For a list of words, print each on a seperate line in uppercase
#2.  Turn #1 into a function called:  print_upper_words
#3.  Change this function so it only prints words that start with 'e'
#4.  Pass a set of letters and only prints words that start with those letters

#1
words = list(["this", "is", "a", "test"])
for word in words:
    print(word.upper())

#2
def print_upper_words(words):
    #words = list(["this", "is", "a", "test"])  jfc I was right the first time
    for word in words:
        print(word.upper()) 

#3
def print_upper_words_e(words):
    for word in words:
        if word[0] == 'e':
            return word
        """stops with first 'e' ?"""
    
#4
def print_upper_words_starts(words, must_start_with):
    for word in words:
        if word[0]  == must_start_with:
            print(word.upper())
                  
        