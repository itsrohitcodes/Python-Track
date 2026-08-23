# ----------------------------------------
# Function to count words
# ----------------------------------------

def count_words(sentence):

    # Convert the sentence to lowercase
    # so that "Python" and "python"
    # are treated as the same word
    sentence = sentence.lower()

    # Split the sentence into individual words
    #
    # Example:
    # "Python is easy"
    #
    # becomes:
    # ["python", "is", "easy"]
    words = sentence.split()


    # Create an empty dictionary
    #
    # We will store:
    # word -> number of times it appears
    word_count = {}


    # Check each word in the list
    for word in words:

        # Check if the word already exists
        # in our dictionary
        if word in word_count:

            # The word already exists,
            # so increase its count by 1
            word_count[word] += 1

        else:

            # This is the first time we found
            # this word, so start its count at 1
            word_count[word] = 1


    # Return both the dictionary and
    # the list of words
    return word_count, words


# ----------------------------------------
# Get sentence from the user
# ----------------------------------------

sentence = input("Enter a sentence: ")


# Send the sentence to the function
# and get back two values
word_frequency, words = count_words(sentence)


# ----------------------------------------
# Calculate basic information
# ----------------------------------------

# len(words) gives the total number of words
total_words = len(words)

# len(word_frequency) gives the number
# of different words
unique_words = len(word_frequency)


# ----------------------------------------
# Find the most frequent word
# ----------------------------------------

# We don't know the most frequent word yet,
# so start with an empty string
most_frequent_word = ""

# Start the highest frequency at zero
highest_frequency = 0


# Check every word and its frequency
for word, frequency in word_frequency.items():

    # If this word appears more times
    # than our current highest frequency
    if frequency > highest_frequency:

        # Save the new highest frequency
        highest_frequency = frequency

        # Save the word that has this frequency
        most_frequent_word = word


# ----------------------------------------
# Display word frequencies
# ----------------------------------------

print("\n----- Word Frequencies -----")

# Display every word and its frequency
for word, frequency in word_frequency.items():

    print(word, ":", frequency)


# ----------------------------------------
# Display final results
# ----------------------------------------

print("\nTotal Number of Words:", total_words)

print("Number of Unique Words:", unique_words)

print("Most Frequent Word:", most_frequent_word)
