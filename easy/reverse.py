def recursive(string, index, final_string):
    final_string += string[len(string)-1-index]
    if index == len(string)-1:
        return final_string
    return recursive(string, index+1, final_string)

final_string = recursive("string", 0, "")
print(final_string)
