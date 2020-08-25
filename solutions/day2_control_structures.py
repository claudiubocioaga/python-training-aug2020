# Write a Python program for checking the speed of drivers.
# If speed is less than or equal to 50, it should print "OK".
# Otherwise, for every 5 km above the speed limit (50), it should give the driver
# one demerit point and print the total number of demerit points.
# For example, if the speed is 60, it should print: "Points: 2".
# If the driver gets more than 12 points, it should print: "License suspended".
# Define a variable called speed and assign an integer value to it.
# After running the program once, change its value and notice the changed output.

MAX_SPEED = 50  # constant names are usually capitalized snake case
KM_PER_POINT = 5

speed = 140

points = (speed - MAX_SPEED) // KM_PER_POINT
if points <= 0:
    print('OK')
elif points <= 12:
    print(f'Points: {points}')
else:
    print('License suspended')


# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz". If the number 30 is encountered, break the loop.

for i in range(1, 50):
    if i == 30:
        break
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
