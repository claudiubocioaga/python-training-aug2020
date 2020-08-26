# import functions_module
#
# result = functions_module.filter_longer_words('ana', 'are', 'mere', n=3)
# print(result)
#
# result = functions_module.filter_longer_words('ana', 'are', 'mere')
# print(result)
#
#
# from functions_module import filter_longer_words
#
# print(filter_longer_words('ana', 'are', 'mere', n=3))

from functions_module import filter_longer_words as filter_words
# from pypackage.pymodule import diff, sum_nr
import pypackage
# from pypackage import pymodule


if __name__ == '__main__':
    print([word.capitalize() for word in filter_words('ana', 'are', 'mere', n=3)])

    # print(diff(10, 2))
    # print(sum_nr(10, 2, 15, 1))

    print(pypackage.PACKAGE_VAR)
    print(pypackage.pymodule.diff(10, 20))
