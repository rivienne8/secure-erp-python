""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import date, timedelta
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_employees_list():
    employees = data_manager.read_table_from_file(DATAFILE)
    return employees

def create_new_employee(new_employee):
    employees_list = get_employees_list()
    new_id = util.generate_id()
    new_employee.insert(0, new_id)
    employees_list.append(new_employee)    
    data_manager.write_table_to_file(DATAFILE, employees_list)

def update_employee(given_id, index, value):
    employees_list = get_employees_list()
    for employee in employees_list:
        if employee[0] == given_id:
            employee[int(index)] = value
    data_manager.write_table_to_file(DATAFILE, employees_list)

def delete_employee(given_id):
    employees_list = get_employees_list()
    for employee in employees_list:
        if employee[0] == given_id:
            employees_list.remove(employee)
    data_manager.write_table_to_file(DATAFILE, employees_list)

def find_names_oldest_youngest():
    employees_list = get_employees_list()
    oldest_emp = min(employees_list, key=lambda employee: employee[2])
    youngest_emp = max(employees_list, key=lambda employee: employee[2])
    return (oldest_emp[1], youngest_emp[1])

def calculate_age(bday_date):
    year, month, day = [int(f) for f in bday_date.split('-')]
    bday_date = date(year, month, day)
    today = date.today()
    years = today.year - bday_date.year
    if today.month < bday_date.month or (today.month == bday_date.month and today.day < bday_date.day):
        years -= 1
    return years

def average_age():
    employees_list = get_employees_list()
    avg_employee_age = sum(calculate_age(employee[2]) for employee in employees_list)/len(employees_list)
    return avg_employee_age

def coming_bdays(input_date):
    employees_list = get_employees_list()

    year, month, day = [int(f) for f in input_date.split('-')]
    input_date = date(year, month, day)
    
    fortnite_to_bday = input_date + timedelta(days = 14)
    results = []
    for employee in employees_list:
        _, bday_month, bday_day = [int(f) for f in employee[2].split('-')]
        bday_date = date(year, bday_month, bday_day)
        next_bday_date = date(year+1, bday_month, bday_day) 
        if (bday_date >= input_date and bday_date <= fortnite_to_bday) or (next_bday_date >= input_date and next_bday_date <= fortnite_to_bday):
            results.append(employee[1])
    return results

def num_of_employees_clr_lvl(given_clr_lvl):
    employees_list = get_employees_list()
    results = 0
    for employee in employees_list:
        if int(employee[4]) >= int(given_clr_lvl):
            results += 1
    return results

def num_of_employees_per_dpt():
    employees_list = get_employees_list()
    results = {}
    for employee in employees_list:
        if employee[3] in results:
            results[employee[3]] += 1
        else:
            results[employee[3]] = 1
    return results
