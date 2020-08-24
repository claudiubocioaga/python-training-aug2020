# Implicit line joining (line breaking inside parentheses is allowed)

# Long string separated in two shorter strings - automatic concatenation
print('Hello world world world world world world world world world world world'
      ' world world world world world world world world world!')
# Function called with multiple arguments, each argument on a new line
print('Hello',
      'Anna',
      'how',
      'are',
      'you?')
# Multiline string
multiline_str = """Somnoroase păsărele
Pe la cuiburi se adună,
Se ascund în rămurele
Noapte bună!"""
print(multiline_str)
# Arithmetic operation split on multiple lines - parentheses used instead of "\"
sum_nr = (
    10 +
    20 +
    30 +
    15
)

# Explicit line joining (using "\" - continuation character)
my_sentence = \
    "A very long sentence ..."
print(my_sentence)

s = 10 + \
    20 + \
    30 + \
    15

grade = 4  # inline comment
# TODO refactor later pls
if grade >= 5:
    print('Congrats! You have passed the exam!')
    print('Inside if-block')

print('Outside if-block!')

if grade is None:  # comparison to None is always done with `is` operator
    print()
