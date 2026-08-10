# Clean and Analyze a sentence

# Read the sentence and position from the user
sentence = input()
position = int(input())

# Remove outer spaces and convert the sentence to lowercase
striped_sentence = sentence.strip()
lower_sentence = striped_sentence.lower()

# Replace the required punctuation marks with spaces
new_sentence = lower_sentence.replace(".", " ")
new_sentence = new_sentence.replace(",", " ")
new_sentence = new_sentence.replace("!", " ")
new_sentence = new_sentence.replace("?", " ")
new_sentence = new_sentence.replace(";", " ")
new_sentence = new_sentence.replace(":", " ")

# Split the sentence into words and rebuild the cleaned sentence
new_words = new_sentence.split()
cleaned_sentence = " ".join(new_words)

# Extract the required words and slices
word_count = len(cleaned_sentence.split())
first_word = new_words[0]
last_word = new_words[-1]
first_prefix = cleaned_sentence[:3]
last_prefix = cleaned_sentence[-3:]

# Display the complete analysis
print(f"Cleaned Sentence: {cleaned_sentence}")
print(f"Word Count: {word_count}")
print(f"First Word: {first_word}")
print(f"Last Word: {last_word}")
print(f"Selected Word: {new_words[position-1]}")
print(f"First Word Prefix: {first_prefix}")
print(f"Last Word Suffix: {last_prefix}")