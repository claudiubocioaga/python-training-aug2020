x = 46546112
sum_of_digits = 0

while x:
    sum_of_digits += x % 10
    x //= 10

print(sum_of_digits)

greeting = "Hello world"
for char in "sjfoahrv":
    print(char, greeting.find(char))

for i in range(len(greeting)):
    char = greeting[i]
    print(char)

for i in range(1, 50):
    if i % 3 == 0:
        print("fizz")
    else:
        print(i)
