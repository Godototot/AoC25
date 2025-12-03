from operator import methodcaller

def read_input_lines(file_name):
    """takes file and returns list of strings for each line, removing the 'new line'"""
    lines = open(file_name, 'r').readlines()
    return list(map(methodcaller('replace', '\n', ''), lines))

def read_single_line_list(file_name):
    """takes file and returns list of all strings in the first line devided by commas"""
    line = open(file_name, 'r').readline()
    return list(line.split(','))