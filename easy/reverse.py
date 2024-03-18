def reverse_string(string, index, final_string):
    final_string += string[len(string)-1-index]
    if index == len(string)-1:
        return final_string
    return reverse_string(string, index+1, final_string)

final_string = reverse_string("string", 0, "")
print(final_string)
