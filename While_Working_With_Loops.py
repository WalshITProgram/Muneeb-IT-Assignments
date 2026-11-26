"""
While Working With Loops Assignment
Gathers information for up to 5 employees (ID, name, email, and an
optional address). If the user enters improper data, the program asks
them to re-enter it before moving on. Each employee is stored as a
dictionary, and all of the dictionaries are kept in one list that is
printed at the end.
"""

# ---------------------------------------------------------
# Characters that are NOT allowed in each field (from the rules)
# ---------------------------------------------------------
name_bad_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
email_bad_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
address_bad_chars = '!"\'@$%^&*_=+<>?;:[]{}'

# ---------------------------------------------------------
# The list that will act like our database table. Each employee
# will be added to it as a dictionary ("row"), and every dictionary
# uses the exact same keys.
# ---------------------------------------------------------
employees = []
max_employees = 5

# ---------------------------------------------------------
# MAIN LOOP: runs once per employee, up to a maximum of 5.
# The user can also stop early by answering "N" at the end of a pass.
# ---------------------------------------------------------
while len(employees) < max_employees:
    print("\n--- Employee " + str(len(employees) + 1) + " of " + str(max_employees) + " ---")

    # -----------------------------------------------------
    # Employee ID (required)
    # Rules: must be a number and 7 or fewer digits long
    # The loop keeps asking until the ID is valid.
    # -----------------------------------------------------
    while True:
        employee_id = input("Please enter the Employee ID: ").strip()

        # .isdigit() is only True when every character is a digit (and the
        # string is not empty), so this covers "required" and "a number"
        if not employee_id.isdigit():
            print("Invalid Employee ID. It is required and must be a number. Please try again.")
        elif len(employee_id) > 7:
            print("Invalid Employee ID. It must be 7 digits or fewer. Please try again.")
        else:
            break   # valid, so leave the loop

    # -----------------------------------------------------
    # Employee Name (required)
    # Rules: primarily letters, and none of the forbidden characters
    # -----------------------------------------------------
    while True:
        employee_name = input("Please enter the Employee Name: ").strip()
        name_ok = True

        # Required: an empty name is not allowed
        if not employee_name:
            print("Invalid Employee Name. It is required. Please try again.")
            name_ok = False
        else:
            # Look for any forbidden character in the name
            for character in employee_name:
                if character in name_bad_chars:
                    name_ok = False
            if not name_ok:
                print("Invalid Employee Name. It contains a character that is not allowed. Please try again.")
            else:
                # "Primarily letters": count the letters (ignoring spaces) and
                # make sure they are more than half of the characters entered
                letter_count = 0
                non_space_count = 0
                for character in employee_name:
                    if character != " ":
                        non_space_count += 1
                        if character.isalpha():
                            letter_count += 1
                if non_space_count == 0 or letter_count <= non_space_count / 2:
                    print("Invalid Employee Name. It must be primarily letters. Please try again.")
                    name_ok = False

        if name_ok:
            break   # valid, so leave the loop

    # -----------------------------------------------------
    # Employee Email Address (required)
    # Rules: primarily alphanumeric, and none of the forbidden characters
    # -----------------------------------------------------
    while True:
        employee_email = input("Please enter the Employee Email Address: ").strip()
        email_ok = True

        # Required: an empty email is not allowed
        if not employee_email:
            print("Invalid Email Address. It is required. Please try again.")
            email_ok = False
        else:
            # Look for any forbidden character in the email
            for character in employee_email:
                if character in email_bad_chars:
                    email_ok = False
            if not email_ok:
                print("Invalid Email Address. It contains a character that is not allowed. Please try again.")
            elif " " in employee_email or "@" not in employee_email:
                # An email address cannot contain spaces and needs an "@"
                print("Invalid Email Address. It must contain an @ symbol and no spaces. Please try again.")
                email_ok = False
            else:
                # "Primarily alphanumeric": more than half of the characters
                # must be letters or numbers
                alnum_count = 0
                for character in employee_email:
                    if character.isalnum():
                        alnum_count += 1
                if alnum_count <= len(employee_email) / 2:
                    print("Invalid Email Address. It must be primarily alphanumeric characters. Please try again.")
                    email_ok = False

        if email_ok:
            break   # valid, so leave the loop

    # -----------------------------------------------------
    # Employee Address (NOT required)
    # Rules: if provided, primarily alphanumeric and none of the
    # forbidden characters. Leaving it blank is allowed.
    # -----------------------------------------------------
    while True:
        employee_address = input("Please enter the Employee Address (optional, press Enter to skip): ").strip()
        address_ok = True

        # Only validate the address if the user actually typed something
        if employee_address:
            # Look for any forbidden character in the address
            for character in employee_address:
                if character in address_bad_chars:
                    address_ok = False
            if not address_ok:
                print("Invalid Address. It contains a character that is not allowed. Please try again.")
            else:
                # "Primarily alphanumeric": count letters/numbers (ignoring
                # spaces) and make sure they are more than half of the characters
                alnum_count = 0
                non_space_count = 0
                for character in employee_address:
                    if character != " ":
                        non_space_count += 1
                        if character.isalnum():
                            alnum_count += 1
                if non_space_count == 0 or alnum_count <= non_space_count / 2:
                    print("Invalid Address. It must be primarily alphanumeric characters. Please try again.")
                    address_ok = False

        if address_ok:
            break   # valid (or blank), so leave the loop

    # -----------------------------------------------------
    # All four values are valid, so build this employee's dictionary
    # (one "row") and add it to the list. A blank address is stored
    # as an empty string.
    # -----------------------------------------------------
    employee_record = {
        'employee_id': employee_id,
        'employee_name': employee_name,
        'employee_email': employee_email,
        'employee_address': employee_address,
    }
    employees.append(employee_record)

    # -----------------------------------------------------
    # Ask whether to add another employee (only if we haven't hit 5 yet)
    # -----------------------------------------------------
    if len(employees) < max_employees:
        while True:
            add_another = input("Do you wish to add another employee (Y or N)? ").strip().upper()
            if add_another == "Y" or add_another == "N":
                break
            print("Please enter Y or N.")

        if add_another == "N":
            break   # the user is done, so exit the main loop
    else:
        print("\nThe maximum of " + str(max_employees) + " employees has been reached.")

# ---------------------------------------------------------
# Print out the final list of dictionaries
# ---------------------------------------------------------
print("\nFinal employee list:")
print(employees)

# Also print each record on its own line so it is easier to read
print("\nFinal employee list (one record per line):")
for employee_record in employees:
    print(employee_record)
