
"""
        get all words from file input№?.csv and enter to array
        :param first_param,second_param: current and possible max count of chain
        :return: max element after compare
"""

def find_max(first_param, second_param):
    if first_param > second_param:
        return first_param
    elif first_param<second_param:
        return second_param
    else:
        return first_param

def search_possible_word(word, iterator):
    result = word[:iterator] + word[iterator + 1:]
    return result
