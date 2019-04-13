# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).
 
text = input("Please enter your text: ")
 
output = []
for x in text.split():
    output.append(len(x))
print(output)
 
# type your solution here:

# Saves the length of each work in the entered 'text'. - Jim
my_output = [len(my_word) for my_word in text.split()]
print(my_output)
 
# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):
 
output = []
for x in text.split():
    output.append((x, len(x)))
print(output)
 
# type the corresponding comprehension here:

my_output_2 = [(my_word, len(my_word)) for my_word in text.split()]
print(my_output_2)

my_set = {(my_word, len(my_word)) for my_word in text.split()}
print(my_set)