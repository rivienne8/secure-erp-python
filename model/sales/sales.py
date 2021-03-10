""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
ID_TRANSACTION_INDEX = 0
ID_CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4

# function that returns list of lists /  all transactions
def get_transactions_list():
    transactions = data_manager.read_table_from_file(DATAFILE)
    return transactions


# function that creates new transaction with new id
def create_new_transaction(lista):
    transactions = get_transactions_list()
    transactions_id_list = [position[ID_TRANSACTION_INDEX] for position in transactions]

    id = util.generate_unique_id(transactions_id_list)
    
    new_transaction = [id]
    for item in lista:
    # for i in range(len(lista)):
        # if i == ID_CUSTOMER_INDEX: !! zrobic w SC zapytanie do modela CRM, jakie id klienta jest dla nazwy klienta
        new_transaction.append(item)

    transactions.append(new_transaction)
    data_manager.write_table_to_file(DATAFILE,transactions)

    return new_transaction


# function that updates data in a given transaction
def update_transaction(id,index,value):
    updated_transaction = []
    transactions = data_manager.read_table_from_file(DATAFILE)
    for i in range(len(transactions)):
        if transactions[i][ID_TRANSACTION_INDEX] == id:
            transactions[i][index] = value
            updated_transaction.append(transactions[i])

    data_manager.write_table_to_file(DATAFILE,transactions)

    return updated_transaction

# function that deletes transaction with a given id
def delete_transaction(id):
    transactions = get_transactions_list()
    for i in range(len(transactions)):
        if transactions[i][ID_TRANSACTION_INDEX] == id:
            transactions.pop(i)
            break
    
    data_manager.write_table_to_file(DATAFILE,transactions)
    
    return transactions # czy potrzebne?

# function that finds the biggest revenue transaction
def get_biggest_revenue_sale():
    transactions = get_transactions_list()
    # for i in range(len(transactions)):

    sorted_desc_by_price_transactions = sorted(
                        transactions, 
                        key= lambda x: float(x[PRICE_INDEX]),
                        reverse=True
                        )
    
    biggest_revenue_transaction = sorted_desc_by_price_transactions[0]

    return biggest_revenue_transaction

# function that finds product that brought the biggest revenue
def get_biggest_revenue_product():
    transactions = get_transactions_list()
    products = list(set([transactions[i][PRODUCT_INDEX] for i in range(len(transactions))]))
    
    products_revenues = []
    for product in products:
        revenue = 0
        for i in range(len(transactions)):
            if transactions[i][PRODUCT_INDEX] == product:
                revenue += float(transactions[i][PRICE_INDEX])
        products_revenues.append((product,revenue))

    # product_index = 0
    sorted_desc_biggest_revenue_products = sorted(
                                products_revenues,
                                key= lambda x:x[1],
                                reverse=True
                                )
    
    biggest_revenue_product = sorted_desc_biggest_revenue_products[0]

    return biggest_revenue_product

# function that counts transactions between 2 different dates
def count_transactions_between_dates(period):
    transactions = get_transactions_list()

    start_date_index = 0
    end_date_index = 1
    transactions_count = 0
    for i in range(len(transactions)):
        if (transactions[i][DATE_INDEX] >= period[start_date_index] and
            transactions[i][DATE_INDEX] <= period[end_date_index]):
            transactions_count += 1
    
    return transactions_count


def get_sum_transactions_between_dates(period):
    transactions = get_transactions_list()

    start_date_index = 0
    end_date_index = 1
    total_revenue_transactions = 0
    for i in range(len(transactions)):
        if (transactions[i][DATE_INDEX] >= period[start_date_index] and
            transactions[i][DATE_INDEX] <= period[end_date_index]):
            total_revenue_transactions += float(transactions[i][PRICE_INDEX])
    
    return total_revenue_transactions
















 
