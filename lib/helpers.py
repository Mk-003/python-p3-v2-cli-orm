from models import department
from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments=Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name=input("Enter the department's name:")
    departments=Department.find_by_name()
    print(department) if department else print(
        f'Department {name} not found')
    


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department(name,location):
    department = Department.create(name, location)
    (f"Department '{name}' created successfully in '{location}'")


def update_department():
    for employee in employee_list:
        if employee['id'] == employee_id:
            # Update the department of the employee
            employee['department'] = new_department
            print("Department updated successfully.")
            return
    
    # If the employee with the given ID is not found
    print("Employee not found.")


def delete_department():
    pass


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
   name = input("Enter the name of the employee you want to find: ")
    for employee in employee_list:
        if employee['name'] == name:
            return employee
    return None

if found_employee:
    print("Employee found:")
    print(found_employee)
else:
    print("Employee not found.")


def find_employee_by_id():
    for employee in employee_list:
        if employee['id'] == employee_id:
            return employee
    return None


def create_employee():
    if not employee_list:
        new_id = 1
    else:
        new_id = max(employee['id'] for employee in employee_list) + 1

    # Create a dictionary for the new employee
    new_employee = {'id': new_id, 'name': name, 'age': age, 'department': department}
    
    # Add the new employee to the list
    employee_list.append(new_employee)
    
    print("Employee created successfully.")


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass