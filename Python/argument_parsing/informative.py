"""
    > python script_name.py [arg1] [arg2] [arg_n]
"""


def arg_parsing(*args, **kwargs):   # Example function to argument parsing
    print(f'Arguments: {args[0], args[1]}')
    print(f"Keyword Arguments: {kwargs['KW1'], kwargs['KW2']}")


arg_parsing(True, 11, KW1='Hello', KW2='World')

