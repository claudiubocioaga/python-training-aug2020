# Write a function that takes a number as a parameter and prints its square.
def print_square(x):
    print(x ** 2)


# Write another function that takes a number as a parameter and returns the
# square. Are the results of the two functions different?
def return_square(x):
    return x ** 2


ex_1_result = print_square(5)
ex_2_result = return_square(5)
print(f'Ex 1 result: {ex_1_result}\nEx 2 result: {ex_2_result}\n'
      f'Results are equal: {ex_1_result == ex_2_result}')


# Write a function that takes any number of strings and an integer n as
# parameters. n should be an optional parameter. Return the list of strings
# longer than n. By default, it should return a list containing all words
def filter_long_words(*words, min_length=0):
    # long_words = [word for word in words if len(word) > min_length]
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


print(filter_long_words('hello', 'hi', 'bye', min_length=2))
print(filter_long_words('hello', 'hi'))
print(filter_long_words())
print(filter_long_words(min_length=10))


# Write a function that builds html tags. Apply html escaping for html special
# chars. The function will receive 2 parameters – tag type and tag content and
# will return the generated html as a string.
#
# E.g.: f('b', 'Ham&Eggs') returns "<b>Ham&amp;Eggs</b>"
#
# HTML char escaping:
#
# < becomes &lt;
# > becomes &gt;
# " becomes &quot;
# & becomes &amp;
def build_html(tag_type, tag_content):
    tag_content = (
        tag_content
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
    )
    return f'<{tag_type}>{tag_content}</{tag_type}>'


print(build_html('b', 'Ham & Eggs'))
print(build_html('p', '"a < b" comparison'))
