# comp_challenge_1.py

# Lesson 204: Challenges
# Fizz Buzz game.

# - Jim
# (Contact info)

fizzbuzz_list = ["fizz buzz" if x % 15 == 0
                 else "fizz" if x % 3 == 0
                 else "buzz" if x % 5 == 0
                 else str(x) for x in range(1, 31)]

for num in fizzbuzz_list:
    print(num)

for word in fizzbuzz_list:
    print(word.center(12, "*"))