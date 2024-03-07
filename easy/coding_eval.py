def create_triangular_number_sequence(n, len_of_elements, triangular_sequence):
    if (n * (n + 1)/ 2) == len_of_elements:
        triangular_sequence.add(len_of_elements)
        n = n + 1
    return triangular_sequence, n

def decode(message_file):
    # Initialize variables
    triangular_sequence = set()
    all_elements_in_file = []

    # Open the file and process each line
    with open(message_file, "r") as file:
        line_no = 0
        n = 1
        for line in file:
            # Split the line into words and convert the first element to an integer
            words = line.strip().split(" ")
            words[0] = int(words[0])

            # Append the words to the all_elements_in_file list
            all_elements_in_file.append(words)

            # Check if the line number matches the triangular number sequence
            triangular_sequence, n = create_triangular_number_sequence(n, len(all_elements_in_file), triangular_sequence)

    # Sort all_elements_in_file based on the first element of each inner list
    all_elements_in_file.sort(key=lambda x: x[0])

    # Create the text by appending words from all_elements_in_file with line numbers in triangular_sequence
    text = ""
    for elements in all_elements_in_file:
        if elements[0] in triangular_sequence:
            text += elements[1] + ' '
    return text.strip()  # Strip trailing whitespace before returning the text
print(decode("coding_qual_input.txt"))
