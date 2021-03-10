from model.sales import sales
from model.crm import crm
from view import terminal as view


MENU = ["Back to main menu","Try again"]

def list_transactions():
    # view.print_error_message("Not implemented yet.")
    transactions = sales.get_transactions_list()
    view.print_table(transactions,sales.HEADERS)


def insert_exit_option(menu):
    menu.insert(0,"Back to main menu")
    return menu

def short_menu():
    view.print_menu("Menu", MENU)
    operation = view.get_input("What would you like to do")
    return int(operation)

def get_matching_names(partial_customer_name):

    # funkcja która zwraca listę nazw klientów, w których pojawia się podana częściowa nazwa klienta (string),
    # jeśli nie ma, to zwraca error value
    matching_names = crm.find_customer_names(partial_customer_name)
    if matching_names == []:
        view.print_error_message("Any customer matches")
        operation = short_menu()
        if operation == 0:
            return None
    
    return matching_names


def add_transaction():
    # view.print_error_message("Not implemented yet.")
    '''cześć potrzebna gdy już bedzie działał crm'''
    matching_customers_names_list = []
    while matching_customers_names_list == []:
        partial_customer_name = view.get_input("Enter name or part of customer's name")
        matching_customers_names_list = get_matching_names(partial_customer_name)
        if matching_customers_names_list == None:
            return
    
    insert_exit_option(matching_customers_names_list)
    view.print_menu("Matching customers names", matching_customers_names_list)
    customer_number = int(view.get_input("Choose the customer to add transaction on it"))
    if customer_number == 0:
        return
    customer_name = matching_customers_names_list[customer_number]
    # # funkcja która dostaje nazwę klienta i zwraca jego id
    customer_id = crm.find_customer_id(customer_name)

    new_transaction_data = view.get_inputs(sales.HEADERS[sales.PRODUCT_INDEX:]) 
    new_transaction_data.insert(0,customer_id)
    
        
    new_transaction = sales.create_new_transaction(new_transaction_data)
    # print(new_transaction)
    view.print_message("New transaction has been added")
    view.print_table([new_transaction],sales.HEADERS)



def update_transaction():
    # view.print_error_message("Not implemented yet.")
    transaction_id = view.get_input(f"Specify the transaction {sales.HEADERS[sales.ID_TRANSACTION_INDEX]}")
    # view.print_message("Specify what do you want to change.")
    headers_menu = sales.HEADERS.copy()[sales.ID_CUSTOMER_INDEX:]
    insert_exit_option(headers_menu)
    view.print_menu("Possible positions to update", headers_menu)
    index = view.get_input("Specify which position would you like to update")
    index_in_headers_menu = int(index)
    if index_in_headers_menu == 0:
        return
    new_value = view.get_input("Enter new value")
    updated_transaction = sales.update_transaction(transaction_id,index_in_headers_menu,new_value)
    view.print_message("The updated transaction: ")
    view.print_table(updated_transaction,sales.HEADERS)
    


def delete_transaction():
    # view.print_error_message("Not implemented yet.")
    transaction_id = view.get_input("Specify id of transaction you want to delete")
    sales.delete_transaction(transaction_id)
    view.print_message(f"Transaction {transaction_id} has been deleted")


def get_biggest_revenue_transaction():
    # view.print_error_message("Not implemented yet.")
    biggest_revenue_transaction = sales.get_biggest_revenue_sale()
    view.print_message("Biggest revenue transaction: ")
    view.print_table([biggest_revenue_transaction],sales.HEADERS)
    # co jeśli sa dwie z takim samym revenue


def get_biggest_revenue_product():
    # view.print_error_message("Not implemented yet.")
    biggest_revenue_product = sales.get_biggest_revenue_product()
    view.print_general_results(biggest_revenue_product,"The product that has brought the biggest revenue")


ASKING_DATES = ["Enter the beginning date of period",
                      "Enter the end date of period"]

def count_transactions_between():
    # view.print_error_message("Not implemented yet.")

    period = view.get_inputs(ASKING_DATES)
    transactions_number = sales.count_transactions_between_dates(period)
    view.print_general_results(transactions_number,f"The number of transactions between {period[0]} and {period[1]} is")


def sum_transactions_between():
    # view.print_error_message("Not implemented yet.")
    period = view.get_inputs(ASKING_DATES)
    total_revenue = sales.get_sum_transactions_between_dates(period)
    view.print_general_results(total_revenue,f"Total revenue of transactions between {period[0]} and {period[1]} is")



def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
