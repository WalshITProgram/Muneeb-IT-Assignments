"""
Employee Data Assignment
Sorting mixed employee data into separate lists, calculating
total hourly rate (with benefits), identifying underpaid employees,
and calculating raises. Final step: combine all of the lists into a
list of dictionaries (a database-like structure) and print it.
"""

# ---------------------------------------------------------
# Requirement 1: Single list containing the raw employee data
# exactly in the order provided.
# ---------------------------------------------------------
employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# ---------------------------------------------------------
# Requirement 2 & 3: Programmatically sort the data into three
# lists based on data type (employee numbers, names, salary
# information), with no duplicate values in each new list.
#
# Note: bool is technically a subclass of int in Python, so
# `type(value) is int` is used instead of `isinstance(value, int)`
# to keep True/False out of the employee number list.
# ---------------------------------------------------------
employee_numbers = []
employee_names = []
hourly_wages = []

for value in employee_data:
    if type(value) is int:
        if value not in employee_numbers:
            employee_numbers.append(value)
    elif type(value) is str:
        if value not in employee_names:
            employee_names.append(value)
    elif type(value) is float:
        if value not in hourly_wages:
            hourly_wages.append(value)
    # Boolean values are the mystery column mentioned in the
    # instructions and are intentionally not sorted into any
    # of the three required lists.

print("Employee numbers:", employee_numbers)
print("Employee names:", employee_names)
print("Hourly wages:", hourly_wages)

# ---------------------------------------------------------
# Requirement 4: Multiply each hourly wage by 1.3 to account
# for benefits, store the results in total_hourly_rate, then
# find the maximum value and warn if it exceeds 37.30.
# ---------------------------------------------------------
total_hourly_rate = []

for wage in hourly_wages:
    total_hourly_rate.append(wage * 1.3)

print("\nTotal hourly rate (with benefits):", total_hourly_rate)

max_total_rate = max(total_hourly_rate)

# Styling: comparison on its own clear if statement, descriptive variable name
if max_total_rate > 37.30:
    print(f"Warning: a total hourly rate of {max_total_rate:.2f} "
          f"may be a budget concern.")

# ---------------------------------------------------------
# Requirement 5: Identify any total hourly rate that falls
# between 28.15 and 30.65 and add it to underpaid_salaries.
# ---------------------------------------------------------
underpaid_salaries = []

for rate in total_hourly_rate:
    if 28.15 <= rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid salaries:", underpaid_salaries)

# ---------------------------------------------------------
# Requirement 6: Calculate a raise for each unmodified hourly
# wage based on the tiered rules below and store the new rates
# in company_raises.
# ---------------------------------------------------------
company_raises = []

for wage in hourly_wages:
    if 22 <= wage < 24:
        new_rate = wage * 1.05
    elif 24 <= wage < 26:
        new_rate = wage * 1.04
    elif 26 <= wage < 28:
        new_rate = wage * 1.03
    else:
        new_rate = wage * 1.02

    company_raises.append(round(new_rate, 2))

print("\nCompany raises:", company_raises)

# ---------------------------------------------------------
# Requirement 7: A custom complex condition with at least four
# truth tests combined on a single line.
#
# Behavior being implemented: check whether there is at least
# one employee name on file, at least one employee number on
# file, at least one underpaid salary identified, and that the
# highest total hourly rate (with benefits) still stays at or
# under $45.00. If all four of those are true at the same time,
# print a short status message summarizing the company data.
# ---------------------------------------------------------
if len(employee_names) > 0 and len(employee_numbers) > 0 and len(underpaid_salaries) > 0 and max_total_rate <= 45.00:
    print("\nStatus: employee data loaded, at least one underpaid "
          "employee was flagged, and total hourly rates remain "
          "within an acceptable range.")

# ---------------------------------------------------------
# Requirement 8 (Week 8): Combine the final lists into a list
# of dictionary items that looks like a database table.
#
# Structure: each dictionary is one "row" (one employee) and
# every dictionary uses the exact same keys, which act like the
# "column names". The list holds all of the rows together.
#
# The lists were all built in the same order, so the item at
# index 0 of every list belongs to the same employee, index 1
# belongs to the next employee, and so on. That lets one index
# pull the matching value out of each list.
# ---------------------------------------------------------
employee_database = []

# Loop once per employee (one pass for each index position)
for index in range(len(employee_numbers)):
    # Build one dictionary ("row") using the value at this index
    # from each of the five lists
    employee_record = {
        'employee_number': employee_numbers[index],
        'employee_name': employee_names[index],
        'hourly_wage': hourly_wages[index],
        'total_hourly_rate': round(total_hourly_rate[index], 2),
        'company_raise': company_raises[index],
    }

    # Add the finished row to the list that acts as our table
    employee_database.append(employee_record)

# Print the final list of dictionaries
print("\nFinal employee database:")
print(employee_database)

# Also print each record on its own line so it is easier to read
print("\nFinal employee database (one record per line):")
for employee_record in employee_database:
    print(employee_record)
