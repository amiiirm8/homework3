def replace_english_numbers(input_file: str, output_file: str) -> None:
    """
    Reads the contents of an input file, replaces the English equivalent of numbers
    1 to 20 with their corresponding numerical values, and writes the modified text
    to an output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.

    Returns:
        None
    """
    # Define a dictionary to map English numbers to their corresponding numerical values
    english_to_numeric = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
        'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14',
        'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18',
        'nineteen': '19'
    }

    # Open the input file and read its contents
    with open(input_file, 'r') as f:
        text = f.read()

    # Replace the English numbers with their corresponding numerical values
    for english, numeric in english_to_numeric.items():
        text = text.replace(english, numeric)

    # Write the modified text to the output file
    with open(output_file, 'w') as f:
        f.write(text)




# Define the input and output file paths
input_file = 'zen.txt'
output_file = 'zen_of_python_numeric.txt'

# Call the replace_english_numbers function
replace_english_numbers(input_file, output_file)