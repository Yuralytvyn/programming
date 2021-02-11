from write_read_helper.helper import find_max
from write_read_helper.helper import search_possible_word


def find_max_chain(word_list, words_dictinary):
    largest_chain = 0
    for word in word_list:
        current_max = 1
        iterator = 0
        while iterator < len(word):
            possible_word = search_possible_word(word, iterator)

            if possible_word in words_dictinary:
                current_max = find_max(current_max, words_dictinary[possible_word])

            iterator += 1
        words_dictinary[word] = current_max+1
        largest_chain = find_max(largest_chain, current_max)

    return largest_chain
