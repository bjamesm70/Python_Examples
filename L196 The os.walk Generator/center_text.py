# center_text.py

# Lesson 199: List Comprehensions

# - Jim
# (contact info)

# print(__file__)

##############
# Functions: #
##############


def centre_text(*args):
    # text = ""
    # for arg in args:
    #     # Add a space at the end of each arg b/c, if we pass a list
    #     # to this function, it needs to add spaces b/t the items.
    #     text += str(arg) + " "
    text = "-".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


#################
# End Functions #
#################

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")
centre_text()