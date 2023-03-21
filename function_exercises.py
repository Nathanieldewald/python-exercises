
def is_two(input_var):
    check_string = isinstance(input_var,str)
    check_number = int(input_var)
    if input_var == check_number:
        return True
    if check_string == True:
        return True
    else:
        return False

is_two(12.1)

def is_vowel(input_var):
    vowel_list = ['a','e','i','o','u']
    if input_var.lower() in vowel_list:
        return True
    else:
        return False
is_vowel('f')

def is_consonant(input_var):
    vowel_list = ['a','e','i','o','u']
    if input_var.lower() in vowel_list:
        return False
    else:
        return True
is_vowel('f') 

def word_check(input_var):
    vowel_list = ['a','e','i','o','u']
    first_char = input_var[0]
    if first_char.lower() in vowel_list:
        input_var = "Now a word"
    else:
        input_var = input_var.capitalize()
        return input_var
word_check("helLo")

def calculate_tip(input_var_a,input_var_b):
    bill_total = input_var_b
    tip_percentage = input_var_a
    tip_amount = input_var_a * input_var_b
    return tip_amount
calculate_tip(0.1, 100)   

def apply_discount(input_var_a, input_var_b):
    price = input_var_a
    discounted_amount = input_var_b * price
    discounted_price = price - discounted_amount
    return discounted_price
apply_discount(10,.1)

def handle_commas(input_var):
    input_var = input_var.replace(",", "")
    return input_var
handle_commas("1,000,000")

def get_letter_grade(input_var):
    input_var = int(input_var)
    if input_var >= 90:
        return "A"
    if input_var >= 80:
        return "B"
    if input_var >= 70:
        return "C"
    if input_var >= 60:
        return "D"
    else:
        return "F"
get_letter_grade(79)     

def remove_vowels(input_var):
    vowel_list = ['a','e','i','o','u']
    input_var = input_var.lower()
    input_var = input_var.replace('a', "") 
    input_var = input_var.replace('e', "") 
    input_var = input_var.replace('i', "") 
    input_var = input_var.replace('o', "")
    input_var = input_var.replace('u', "") 
    return input_var
remove_vowels("helaelo")

def normalize_name(input_var):
    input_var = input_var.lower()
    input_var = ''.join(i for i in input_var if i.isalnum() or i == ' ')
    input_var = input_var.strip()
    input_var = input_var.replace(" ","_")
    return input_var
normalize_name("First ?name sdkjal  ")

from itertools import accumulate
def cumulative_sum(input_list):
    return list(accumulate(input_list))
cumulative_sum([1, 3, 6, 10])   