sentence_simple_quotes = 'That\'s not "true"'  # "\" used as escape character
sentence_double_quotes = "That's not \"true\""
print(sentence_simple_quotes)
print(sentence_double_quotes)

print('Special characters containing "\\": \n \t \r')
print('Escaping characters: \\; Newline character: \\n')

# Slicing
# string[start:stop]
# string[start:stop:step]

# f-strings
x = 123
greeting = 'hello world'.replace('l', '*')
print(f'Last digit in number {x}: {x % 10}. {greeting.replace("*", "l")}! {dir} is a built-in function')
