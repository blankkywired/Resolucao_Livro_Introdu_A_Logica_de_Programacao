
def thirtString():
    string_A = input()
    string_B = input()
    string_C = ""
    for char in string_A:
        if char in string_B:
            string_C += char
    return string_C
print(thirtString())