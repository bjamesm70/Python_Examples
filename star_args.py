# star_args.py

# Lesson 178: Star Args

# - Jim
# (Contact info)


def average(*args):
    
    print("type(args): {}".format(type(args)))
    print("args is {}:".format(args))
    print("*args is:", *args)

    total = 0
    for arg in args:
        total = total + arg

    return total / len(args)


def build_tuple(*args):

    # print(args)
    # print(*args)
    
    return args


# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     # Default Value = None --> If no default value
#     # is supplied, then the program throws an error
#     # "KeyError", and program will crash!
#     kwargs.pop('end', None)
#
#     my_end=" "
#     for key, value in kwargs.items():
#         print(key, "==>", value)
#
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#


def print_backwards(*args, **kwargs):
    
    # Default Value = \n--> If no default value
    # is supplied, then the program throws an error
    # "KeyError", and program will crash!
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    
    # print("end character is: [{}]".format(end_character))
    
    # We are making repeated calls to the print statement.
    # The default "end" character is a <CR>.  As we are not
    # calling 1 print statement but many, we need to substitution the
    # user's desired separator (held in 'sep_character') with
    # the print's 'end' in the for loop below.  This will give
    # us the effect desired by the user.
    
    # (Print all but the 1st passed word.)
    # (See after the "for" loop for more info.)
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    
    # Now that we are done printing the user's strings
    # in reverse, we want to print the user's requested
    # end character.  (This is how the instructor wanted
    # it done.)
    print(args[0][::-1], end=end_character, **kwargs)
    #print(end=end_character, **kwargs)


# print(average(1, 2, 3, 4))

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

print()

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

print("")
print("-" * 40)
print("")

# Opening, and closing the file.
backwards_FH = open("backwards.txt", mode="w")

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards_FH)
print("Another String", file=backwards_FH)
print("Another String", file=backwards_FH)

backwards_FH.close()

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep="|")
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep="|")
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')