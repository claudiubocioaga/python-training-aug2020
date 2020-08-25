greeting = "Bună"

try:
    #fifth_element = greeting[4]
    h_index = greeting.index('u')
except (IndexError, KeyError):
    print('element not found!')
except ValueError as ex:
    print(ex)
    print('Exception occured at line:', ex.__traceback__.tb_lineno)
else:
    print('No exception')
finally:
    print('Executes every time')

name = input("What's your name? ")
print(f'Hi, {name}')
