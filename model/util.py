import random
import string

# function that create id and check if it is unique 
def generate_unique_id(forbidden_id_list,number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    
    is_accessible = False

    while not is_accessible:
        id = generate_id(number_of_small_letters,
                number_of_capital_letters,
                number_of_digits,
                number_of_special_chars,
                allowed_special_chars)
        if check_is_id_accessible(id,forbidden_id_list):
            is_accessible = True   

    return id 


# functions that generates id
def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    # small_letters = list(string.ascii_lowercase)
    # capital_letters = list(string.ascii_uppercase)
    # digits = list(string.digits)
    # digits = [random.randint(0,9) for i in range(number_of_digits)]
    
    
    id_list = random.choices(string.ascii_lowercase,k=number_of_small_letters)
    id_list += random.choices(string.ascii_uppercase,k=number_of_capital_letters)
    id_list += [random.randint(0,9) for i in range(number_of_digits)]
    id_list += random.choices(allowed_special_chars,k= number_of_special_chars)

    random.shuffle(id_list)

    id = ""
    for i in range(len(id_list)):
        id += str(id_list[i])

    return id  
    
# function that checks if a given id has been used before
def check_is_id_accessible(id,id_list):
    if any(position == id for position in id_list):
        return False
    else:
        return True
