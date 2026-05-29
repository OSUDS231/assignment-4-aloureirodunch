import copy

# ── Global variables — do not modify ─────────────────────────────────────────

employee_list = []
employee_set  = set()
employee_records  = {}
employee_benefits = {}

VALID_LEVELS      = {'employee', 'manager', 'executive'}
VALID_DEPARTMENTS = {'engineering', 'marketing', 'hr', 'finance', 'operations'}
VALID_PAY_TYPES   = {'hourly', 'salary'}

BENEFITS = {
    'healthcare': ('Health Insurance',        150.0),
    'childcare':  ('Child Care Support',      100.0),
    'transport':  ('Public Transport Benefit', 50.0),
}

change_log = []

# ── Your implementations go below ────────────────────────────────────────────


# Part 1 — Employee Registration

def add_employee(input_str):
    """
    Input: input_str (str)
    Return: the newly created record dictionary for the employee (dict)
    Raises: ValueError for any invalid or missing field, or a duplicate name
    """

    split_string = input_str.split(' ')
    if len(split_string) != 5:
        raise ValueError(f"Expected 5 fields, got {len(split_string)}")
    if split_string[0] in employee_set:
        raise ValueError(f"Name already exists: {split_string[0]}")
    if split_string[1] not in VALID_LEVELS:
        raise ValueError(f"Invalid level: {split_string[1]}")
    if split_string[2] not in VALID_DEPARTMENTS:
        raise ValueError(f"Invalid department: {split_string[2]}")
    if split_string[3] not in VALID_PAY_TYPES:
       raise ValueError(f"Invalid pay type: {split_string[3]}")
    try:
        pay_amount_converted = float(split_string[4])
    except:
       raise ValueError(f"Invalid pay amount: {split_string[4]}")
    employee_list.append(split_string[0])
    employee_set.add(split_string[0])
    employee_records[split_string[0]] = {"level": split_string[1], "dept": split_string[2], "pay_type": split_string[3], "pay_amount": pay_amount_converted}
    employee_benefits[split_string[0]] = set()


def run_registration():
   while True:
       counter = 0
       new_employee = input("Enter employee info (or 'quit' to stop): ")
       if new_employee == 'quit':
           break
       try:
           add_employee(new_employee)
           print(f"Employee {new_employee.split()[0]} added successfully.")
           counter += 1
       except ValueError as err:
           print(str(err))

run_registration()

# Part 2 — Accessors

def get_employee(name):
    pass


def get_employees_by_department(dept):
    pass


def get_employees_by_level(level):
    pass


# Part 3 — Benefit Assignment

def assign_benefit(name, benefit_code):
    pass


# Part 4 — Change Log and Modifiers

def save_to_change_log(name):
    pass


def update_employee_pay(name, new_amount):
    pass


def update_employee_level(name, new_level):
    pass


def remove_employee(name):
    pass

