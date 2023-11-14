def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Check if each letter of the alphabet is present in the sentence
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return False

    return True


# Example usage calling the functions here
input_sentence = input("Enter a sentence: ")
if is_pangram(input_sentence):
    print("The entered sentence is a pangram.")
else:
    print("The entered sentence is not a pangram.")