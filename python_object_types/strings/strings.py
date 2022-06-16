vowels = 'aeiou'
print('a' in vowels)                                                       #operator for searching in sequence

# list_name[starting_point:ending_point]                                   # slice of vowels from i to j o:3 in longets word 012
# list_name[starting_point:ending_point:how_many_steps]                    # slice of s from i to j with step k

longest_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'

s = longest_word[0:3:1]
print(s)

y = longest_word[6:]
print(y)

z = longest_word[:6]
print(z)

x = longest_word.count('volcano')                                          # counts how many times volcanos happened
print(x)

o = longest_word.count('o')                                                # counts how many times o happened
print(o)


"""the in operator works in strings, tuples, and lists """
                                                                          