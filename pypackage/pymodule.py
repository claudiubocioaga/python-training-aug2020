# from pypackage import PACKAGE_VAR  # absolute import
from .pymodule2 import GLOBAL_VAR # relative import


def diff(a, b):
    return a - b


def sum_nr(*args):
    from . import PACKAGE_VAR  # local relative import
    final_args = []
    for arg in args:
        if arg in PACKAGE_VAR or arg == GLOBAL_VAR:
            continue
        final_args.append(arg)
    return sum(final_args)
