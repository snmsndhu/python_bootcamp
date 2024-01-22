##Use Dictionary Comprehension to create a dictionary called result that takes,
# each word in the given sentence and calculates the number of letters in each word.


sentence = "What is the total of the all letters?"

result = {word:len(word) for word in sentence.split()}

print(result)