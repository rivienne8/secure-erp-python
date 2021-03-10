from model.hr import hr
from view import terminal as view


def list_employees():
    employees_list = hr.get_employees_list()
    view.print_table(employees_list, hr.HEADERS)

def add_employee():
    new_employee = view.get_inputs([
        "Enter new employee's name",
        "Enter new employee's birth date",
        "Specify new employee's department",
        "Specify new employee's clearance level"
    ])
    hr.create_new_employee(new_employee)

def update_employee(): 
    given_id = view.get_input("Provide a valid employee's id to update his/her profile")
    index = view.get_input("Specify which value you are attempting to change:\n1 for name, 2 for b.day, 3 for dept, 4 for clr lvl")
    value = view.get_input("Provide a new value for the selected category")
    hr.update_employee(given_id, index, value) 

def delete_employee():
    given_id = view.get_input("Provide a valid employee's id to delete his/her profile")
    hr.delete_employee(given_id)

def get_oldest_and_youngest():
    age_extremum_names = hr.find_names_oldest_youngest()
    view.print_general_results(age_extremum_names, 'The oldest and youngest employees are')

def get_average_age():
    avg_age = hr.average_age()
    view.print_general_results(avg_age, "Employees' average age equals")

def next_birthdays():
    input_date = view.get_input('Select the date to be checked since')    
    view.print_general_results(hr.coming_bdays(input_date), 'Employees having their birthday within 2 weeks since the date provided are')

def count_employees_with_clearance():
    given_clr_lvl = view.get_input('Specify the minimum clearance level')
    qty = hr.num_of_employees_clr_lvl(given_clr_lvl)
    view.print_general_results(qty, 'Number of employees above or equal to this criteria is')

def count_employees_per_department():
    num_per_dpt = hr.num_of_employees_per_dpt()
    view.print_general_results(num_per_dpt, 'Departments with their inner employees quantities')

def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")

def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)

def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
