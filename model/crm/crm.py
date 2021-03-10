""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

CUSTOMER_ID_INDEX = 0
CUSTOMER_NAME_INDEX = 1
EMAIL_INDEX = 2
SUBSCRIBED_INDEX = 3

# function that returns list of all customers from database
def get_customers_list():
    customers = data_manager.read_table_from_file(DATAFILE)
    return customers

# function that create a new customer account and generate a new id form him/her
def create_new_account(lista):
    customers = get_customers_list()
    customers_id_list = [position[CUSTOMER_ID_INDEX] for position in customers]

    id = util.generate_unique_id(customers_id_list)

    new_customer = [id]
    
    for i in range(len(lista)):
        new_customer.append(lista[i])
    
    customers.append(new_customer)
    data_manager.write_table_to_file(DATAFILE, customers)

    return new_customer

# function that update the customer account
def update_customer_account(id, index, value):
    updated_customer = []

    customers = get_customers_list()

    for i in range(len(customers)):
        if customers[i][CUSTOMER_ID_INDEX] == id:
            customers[i][index] = value
            updated_customer = customers[i]
    
    data_manager.write_table_to_file(DATAFILE, customers)

    return updated_customer

#function that delete customer depends on chosen data
def delete_customer_account(id, name, email):
    customers = get_customers_list()

    for i in range(len(customers)):
        if customers[i][CUSTOMER_ID_INDEX] == id:
            customers.pop(i)
        elif customers[i][CUSTOMER_NAME_INDEX] == name:
            customers.pop(i)
        elif customers[i][EMAIL_INDEX] == email:
            customers.pop(i)

    
    data_manager.write_table_to_file(DATAFILE, customers)

# # function to get the list of emails of subscribed customers
def get_emails_of_subscribed_customers():
    list_of_emails_of_subs_cust = []
    customers = get_customers_list()
    
    for i in range(len(customers)):
        if customers[i][SUBSCRIBED_INDEX] == 1:
            list_of_emails_of_subs_cust = customers[EMAIL_INDEX]

    return list_of_emails_of_subs_cust
    

# function to return customer name if a given string is a part of this name 
def find_customer_names(part_of_name):
    customers = get_customers_list()
    list_of_cust_with_string = []

    try:
        for i in range(len(customers)):
            # if customers[i][CUSTOMER_NAME_INDEX] == part_of_name:
            if part_of_name.lower() in customers[i][CUSTOMER_NAME_INDEX].lower():
                # list_of_cust_with_string = customers[i]
                list_of_cust_with_string.append(customers[i][CUSTOMER_NAME_INDEX])
        
        return list_of_cust_with_string 

    except ValueError:
        return []

# function that searchs for customer name and return his/her id
def find_customer_id(customer_name):
    customers = get_customers_list()

    for i in range(len(customers)):
        if customers[i][CUSTOMER_NAME_INDEX] == customer_name:
            return customers[i][CUSTOMER_ID_INDEX]


