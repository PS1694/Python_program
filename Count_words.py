def count_words(text):
    """
    Function to count the number of words in a given text.
    :param text: str: The input text
    :return: int: The number of words in the text
    """
    # Split the text into words based on whitespace
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    """
    Main function to run the Word Counter program.
    Handles user input, counts words, and displays the result.
    """
    print("Welcome to the Word Counter Program!")
    print("Enter 'exit' to quit the program at any time.")

    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("\nPlease enter a sentence or paragraph: ").strip()

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Check for empty input
        if not user_input:
            print("Error: You entered an empty string. Please try again.")
            continue

        # Count the number of words in the input
        word_count = count_words(user_input)

        # Display the word count
        print(f"The number of words in the given text is: {word_count}")

if __name__ == "__main__":
    main()
  
