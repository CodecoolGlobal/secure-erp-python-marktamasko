def print_menu(title, list_options):
    bold = "\033[1m"
    yellow = '\033[93m'
    end = '\033[0m'
    title = bold + title.upper() + end
    print("\n\n")
    print(yellow + title.center(95) + end)
    print()
    counter = 0
    for option in list_options:
        print(str(counter).rjust(50), option)
        counter += 1
    '''Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)'''


def print_message(message):
    '''Args:
        message: str - the message'''
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    # floatType = isinstance(result, (float))
    listType = isinstance(result(list, tuple))
    # dictType = isinstance(result, (dict))
    # if floatType:
    #     pass
    if listType:
        print(f"{result}\n customer is subscribed")
    # elif dictType:
    #     pass
    # else:
    #     errormsg - validálás

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def print_table(table):
    length_list = [len(element) for row in table for element in row]
    column_width = max(length_list)
    printTableRow = (len(table[0])*(column_width + 5)) * '-'
    for row in table:
        print(printTableRow.rjust(100))
        row = " | ".join(element.center(column_width + 2) for element in row)
        print(row.rjust(100))
    print(printTableRow.rjust(100))


"""Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    nl = '\n\n'
    inp = input(f"{nl}Please {label} : ")
    return inp


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inps = input(f"Please {labels} :\n")
    return inps


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error:{ message}")
