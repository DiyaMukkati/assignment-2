try:
    #input from the user
    sentence = input("Enter a sentence: ")

    # Show of original sentence
    print("\nOriginal:", sentence)

    # Total characters (with spaces)
    characters_with_spaces = len(sentence)

    # Total characters (without spaces)
    characters_without_spaces = len(sentence.replace(" ", ""))

    # Splitting sentence into words
    words_list = sentence.split()

    # Total words
    total_words = len(words_list)

    # Case conversions
    upper_case = sentence.upper()
    lower_case = sentence.lower()
    title_case = sentence.title()

    # First and last word (checking if sentence is not empty)
    if total_words > 0:
        first_word = words_list[0]
        last_word = words_list[-1]
    else:
        first_word = ""
        last_word = ""

    # Reversing the sentence
    reversed_sentence = sentence[::-1]

    # Printing results
    print("Characters (with spaces):", characters_with_spaces)
    print("Characters (without spaces):", characters_without_spaces)
    print("Words:", total_words)
    print("UPPERCASE:", upper_case)
    print("lowercase:", lower_case)
    print("Title Case:", title_case)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Reversed:", reversed_sentence)

except Exception:
    print("I'm sorry your input is wrong. Please try again.")