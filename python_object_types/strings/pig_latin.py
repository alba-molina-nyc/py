"""
Pig Latin (http://mng.bz/YrON) is a common childrens “secret” language in English- speaking countries. (Its normally secret among children who forget that their parents were once children themselves.) The rules for translating words from English into Pig Latin are quite simple:
 If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.
”"""

from pytest import console_main


def pig_latin():
    word = input('please enter a word to translate from english => piglatin: ')
    way = 'way'
    ay = 'ay'

    while word != None: 
        for i in word:
            if word[0] in 'aeiou':
                word = word + way
                print(word)
                return word
            else:
                if word[0] not in 'aeiou': 
                    word = word[1:] + word[:1] + ay 
                    print(word)
                    return word
# pig_latin()

def pig_latin_sentence():
    sentence = input('please enter a word to translate from english => piglatin: ')
    way = 'way'
    ay = 'ay'
    
    

    while sentence != None:
        splitting = sentence.split()                                # use built in split method to split the words in a sentence
        print(splitting)

        for s in splitting:                                         # use built in "in" operator
            if s[0] in 'aeiou':
                s = s + way
                print(s)
            else: 
                if s[0] not in 'aeiou':
                    s = s[1:] + s[:1] + ay 
                    print(s)
        return s             
# pig_latin_sentence()


def pig_latin_elite():
    word = input('please enter a word to translate from english => piglatin: ')

    if word[0] in 'aeiou':
        print(f'{word}way')
        return f'{word}way'

    print(f'{word[1:]}{word[0]}ay')
    return f'{word[1:]}{word[0]}ay'

# pig_latin_elite()


def pig_latin_elite_sentence():
    sentence = input('please enter a word to translate from english => piglatin: ')
    output = []

    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    print(' '.join(output))
    return ' '.join(output)

pig_latin_elite_sentence()


