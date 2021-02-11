
"""
        get result of our algorithm
        :param result: result of algorithm longest chain
        :return: file output.out with result
"""
def create_write_to_file(result):
    f = open("output.out", "w+")
    f.write(str(result))
    f.close()