def thirtString():
    string_A = input()
    string_B = input()

    string_C = ""
    for char in string_B:
        if char not in string_A:
            string_C += char
    for char in string_A:
        if char not in string_B:
            string_C += char
    
    return string_C

print(f"{thirtString()}")