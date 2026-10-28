def main():
    # reading the txt from the input
    user_string = input()
    
    letter_counts = {}
    
    # go thru every letter 
    for char in user_string:
        # look for the capitalized letters
        if char.isalpha():
            # make it lowercase
            low_char = char.lower()
            # increment the count inside dict
            letter_counts[low_char] = letter_counts.get(low_char, 0) + 1
            
    # get tuples and sort by index in order
    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    
    # unpack it and show how much each letter is displayed
    for letter, count in sorted_letters:
        print(f"'{letter}': {count}")

if __name__ == "__main__":
    main()
