"""
User Input Assignment
Gathers an employee's ID, name, email address, and (optional) address.
If any value is entered incorrectly, the program prints an error message
and terminates immediately without asking for any more information.
"""

import sys   # sys.exit() lets us stop the program as soon as an input is invalid

# ---------------------------------------------------------
# Characters that are NOT allowed in each field (from the rules)
# ---------------------------------------------------------
name_bad_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
email_bad_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
address_bad_chars = '!"\'@$%^&*_=+<>?;:[]{}'

# ---------------------------------------------------------
# Employee ID (required)
# Rules: must be a number and 7 or fewer digits long
# ---------------------------------------------------------
employee_id = input("Please enter your Employee ID: ").strip()

# .isdigit() is only True when every character is a digit (and the string
# is not empty), so this covers both "required" and "must be a number"
if not employee_id.isdigit():
    print("Invalid Employee ID. It is required and must be a number.")
    sys.exit()

# Check the length: 7 digits or fewer
if len(employee_id) > 7:
    print("Invalid Employee ID. It must be 7 digits or fewer.")
    sys.exit()

# ---------------------------------------------------------
# Employee Name (required)
# Rules: primarily letters, and none of the forbidden characters
# ---------------------------------------------------------
employee_name = input("Please enter your Employee Name: ").strip()

# Required: an empty name is not allowed
if not employee_name:
    print("Invalid Employee Name. It is required.")
    sys.exit()

# Look for any forbidden character in the name
for character in employee_name:
    if character in name_bad_chars:
        print("Invalid Employee Name. It contains a character that is not allowed.")
        sys.exit()

# "Primarily letters": count the letters (ignoring spaces) and make sure
# they make up more than half of the characters entered
letter_count = 0
non_space_count = 0
for character in employee_name:
    if character != " ":
        non_space_count += 1
        if character.isalpha():
            letter_count += 1

if non_space_count == 0 or letter_count <= non_space_count / 2:
    print("Invalid Employee Name. It must be primarily letters.")
    sys.exit()

# ---------------------------------------------------------
# Employee Email Address (required)
# Rules: primarily alphanumeric, and none of the forbidden characters
# ---------------------------------------------------------
employee_email = input("Please enter your Employee Email Address: ").strip()

# Required: an empty email is not allowed
if not employee_email:
    print("Invalid Email Address. It is required.")
    sys.exit()

# Look for any forbidden character in the email
for character in employee_email:
    if character in email_bad_chars:
        print("Invalid Email Address. It contains a character that is not allowed.")
        sys.exit()

# An email address cannot contain spaces and needs an "@" symbol
if " " in employee_email or "@" not in employee_email:
    print("Invalid Email Address. It must contain an @ symbol and no spaces.")
    sys.exit()

# "Primarily alphanumeric": more than half of the characters must be
# letters or numbers
alnum_count = 0
for character in employee_email:
    if character.isalnum():
        alnum_count += 1

if alnum_count <= len(employee_email) / 2:
    print("Invalid Email Address. It must be primarily alphanumeric characters.")
    sys.exit()

# ---------------------------------------------------------
# Employee Address (NOT required)
# Rules: if provided, primarily alphanumeric and none of the
# forbidden characters
# ---------------------------------------------------------
employee_address = input("Please enter your Employee Address (optional): ").strip()

# Only validate the address if the user actually typed something
if employee_address:
    # Look for any forbidden character in the address
    for character in employee_address:
        if character in address_bad_chars:
            print("Invalid Address. It contains a character that is not allowed.")
            sys.exit()

    # "Primarily alphanumeric": count letters/numbers (ignoring spaces)
    # and make sure they make up more than half of the characters entered
    alnum_count = 0
    non_space_count = 0
    for character in employee_address:
        if character != " ":
            non_space_count += 1
            if character.isalnum():
                alnum_count += 1

    if non_space_count == 0 or alnum_count <= non_space_count / 2:
        print("Invalid Address. It must be primarily alphanumeric characters.")
        sys.exit()

# ---------------------------------------------------------
# Everything was valid, so print the final message
# ---------------------------------------------------------
message = ("Hello, " + employee_name + ". Your Employee ID is " + employee_id +
           ", and your email address is " + employee_email + ". ")

if employee_address:
    # An address was provided
    message += "Your address is " + employee_address + "."
else:
    # No address was provided
    message += "You did not provide an address."

print(message)
