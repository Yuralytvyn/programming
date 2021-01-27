
def kmp_search(pattern, text):
    length_of_pattern = len(pattern)
    length_of_text = len(text)

    array_of_0 = [0] * length_of_pattern
    j = 0
    i = 0
    compute_array(pattern, length_of_pattern, array_of_0)

    if length_of_pattern == 0:
        return str(0)
    while i < length_of_text:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        elif i < length_of_text and pattern[j] != text[i]:
            if j != 0:
                j = array_of_0[j - 1]
            else:
                i += 1
        if j == length_of_pattern:


            j=length_of_pattern
            return str(i - j)


def compute_array(pattern, length_of_pattern, array_of_0):
    length = 0
    i = 1

    while i < length_of_pattern:

        if pattern[i] == pattern[length]:
            length += 1
            array_of_0[i] = length
            i += 1
        else:
            if length != 0:
                length = array_of_0[length - 1]
            else:
                array_of_0[i] = 0
                i += 1

    return array_of_0


text = "cdfgocdac"
pattern = "cdac"

print("Pattern begins at " + kmp_search(pattern, text) + " letter")
