from datetime import date


class Person:
    count = 0  # class variable
    MIN_YEAR_OF_BIRTH = 1900

    # Type annotations (argument: type) are suggestions for expected type
    def __init__(self, name: str, date_of_birth: date):
        self.name = name  # instance variable
        self.date_of_birth = date_of_birth

    def get_age(self):  # instance method
        diff = date.today() - self.date_of_birth
        return int(diff.days / 365.25)

    def __str__(self):
        return (
            f'name={self.name}, date_of_birth={self.date_of_birth}, '
            f'age={self.get_age()}'
        )

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __eq__(self, other):
        return self.date_of_birth == other.date_of_birth


# Set attribute: object.attribute = value
# Get attribute: object.attribute
# Delete attribute: del object.attribute
if __name__ == '__main__':
    p1 = Person('Ana', date(1999, 10, 2))
    d = date(1985, 4, 23)
    p2 = Person('Andrei', d)
    print(Person.count, p1.count, p2.count)
    print(f'p1: {p1}')
    print(f'p2: {p2}')

    if p1 < p2:
        print(f'{p1.name} is younger than {p2.name}')
    else:
        print(f'{p1.name} is older than {p2.name}')
