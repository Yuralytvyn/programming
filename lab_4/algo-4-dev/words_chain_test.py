from main import main
from write_read_helper.read_file import read_csv


def main_test():
    """
    main function to run algorithm
    :return:max chain from our words
    >>> main(read_csv("input.csv"))
    6
    >>> main(read_csv("input2.csv"))
    4
    >>> main(read_csv("input3.csv"))
    1
    >>> main(read_csv("input4.csv"))
    0
    >>> main(read_csv("input5.csv"))
    3
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
