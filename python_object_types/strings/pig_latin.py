"""
Pig Latin (http://mng.bz/YrON) is a common childrens “secret” language in English- speaking countries. (Its normally secret among children who forget that their parents were once children themselves.) The rules for translating words from English into Pig Latin are quite simple:
 If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”"""

from pytest import console_main


def pig_latin():
    word = input('please enter a word to translate from english => piglatin: ')
    way = 'way'
    ay = 'ay'
    vowel_word = None
    consonant_word = None

    while word != None: 
        for i in word:
            if word[0] in 'aeiou':
                word = word + way
                vowel_word = word
                print(vowel_word)
                return vowel_word
            else:
                if word[0] not in 'aeiou': 
                    print(word[0])
                    word = word[1:] + word[:1] + ay 
                    consonant_word = word
                    print(consonant_word)
                    return consonant_word
pig_latin()