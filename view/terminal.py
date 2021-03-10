def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"{title}:")

    for i in range(1,len(list_options)):
        print(f"({i}) {list_options[i]}")

    print(f"(0) {list_options[0]}\n")    


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int:
        print(f"{label}: {result}")
    elif type(result) == float:
        result_formatted = '{:.2f}'.format(result)
        print(f"{label}: {result_formatted}")
    elif type(result) == list or type(result) == tuple:
        print(f"{label}:")
        print('; '.join(f'{e}' for e in result))
    elif type(result) == dict:
        print(f"{label}:")
        print('; '.join(f'{k}: {v}' for k,v in result.items()))
    print('')


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table, headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    cell_sizes = [16, 16, 32, 16, 16]

    print('-'*(sum(cell_sizes) + (3*len(headers)+1)))
    print('| ',end='')
    for ind, element in enumerate(headers): 
        print(element + ' '*(cell_sizes[ind]-len(element)), end =' | ')
    print('')
    print('-'*(sum(cell_sizes) + (3*len(headers)+1)))

    for row in table:
        
        print('| ',end='')
        for ind, element in enumerate(row): 
            print(element + ' '*(cell_sizes[ind]-len(element)), end =' | ')
        print('')
        print('-'*(sum(cell_sizes) + (3*len(row)+1)))

        
def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"{label}: ") 


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    input_list = []
    for label in labels:
        input_list.append(get_input(f"{label}")) 

    return input_list
        

def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error: {message}")