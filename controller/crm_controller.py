from model.crm import crm
from view import terminal as view


def list_customers():
    #view.print_error_message("Not implemented yet.")
    list_of_customers = crm.get_customers_list()
    view.print_general_results(list_of_customers, "Customers")

def add_customer():
    add_new_customer = crm.create_new_account()
    view.print_general_results(add_new_customer, "A new customer has been added")
    #view.print_error_message("Not implemented yet.")


def update_customer():
    update_customer_list = crm.update_customer_account()
    view.print_general_results(update_customer_list, "The list of customers has been updated")
    #view.print_error_message("Not implemented yet.")


def delete_customer():
    deletion_of_customer = crm.delete_customer_account()
    view.print_general_results(deletion_of_customer, "The customer has been deleted from the list")
    #view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    subscribed_emails = crm.get_emails_of_subscribed_customers()
    view.print_general_results(subscribed_emails, "The list of subscribed emails")
    #view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
