def countChar():
    string_user = input(': ').upper()
    dictionary = {}
    for char in string_user:
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1
    for elements in dictionary:
        print(elements,":", dictionary[elements],"X")
countChar()

# exemplo = {}
#
# exemplo['key'] = 1
# exemplo['key'] += 1
# print(exemplo)