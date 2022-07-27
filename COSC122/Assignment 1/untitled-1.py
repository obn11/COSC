def load_file(file_name):
    """ Reads integers from a file.
    The file should have one integer per line """
    with open(file_name) as infile:
        integers = [int(line) for line in infile.read().splitlines()]
    return integers

a = load_file("list0.txt")