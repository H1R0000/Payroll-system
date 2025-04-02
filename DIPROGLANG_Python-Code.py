# Python: Basic Payroll System for a Call Center
#DIPROGLANG & IMAN Project
#Group Members:
# Kumaarr, Kkshitij
# Limpin, Miguel
# Rodriguez, Angelle Joshe
# Hero, Park
# Bongon, Joshwell

from datetime import datetime

#Lists
employees = []  # List to store employee records
probationary_employees = []
permanent_employees = []
contractual_employees = []

def generate_employee_id():
    """Generate a unique employee ID starting from 0001."""
    return f"{len(employees) + 1:04d}"

def is_name_unique(new_name, current_name=None):
    """Check if the new name is unique, allowing the same name if unchanged."""
    return all(emp["Name"] != new_name for emp in employees if emp["Name"] != current_name)

def validator_date():
    while True:
        try:
            date_str = input("Enter Date Hired (YYYY-MM-DD): ").strip()
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
            return valid_date.strftime("%Y-%m-%d")  # Return in correct format
        except ValueError as e:
            print(f"Invalid date format: {e}. Please enter a valid date in YYYY-MM-DD format.")

def validator_name():
    while True:
        try:
            name = input("Enter Employee Complete Name (Firstname, Middle Name, Lastname): ").strip()
            if not all(char.isalpha() or char.isspace() for char in name) or not name:
                raise ValueError("Name should only contain letters and spaces.")
            return name
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def add_employee():
    print("\n--- Add Employee ---")
    emp_id = generate_employee_id()
    print(f"Employee ID: {emp_id}")
    name = validator_name()    
    date_hired = validator_date()    
    department = input("Enter Department: ")
    position = input("Enter Position: ")
    print("Employment status: \n ~Probationary \n ~Permanent \n ~Contractual")
    
     # Shortened employment status input
    while True:
        status_input = input("Enter Employment Status (PRB/P/C): ").upper()
        
        if status_input == "PRB":
            status = "Probationary"
            break
        elif status_input == "P":
            status = "Permanent"
            break
        elif status_input == "C":
            status = "Contractual"
            break
        else:
            print("Invalid status! Use PRB for Probationary, P for Permanent, C for Contractual.")

    rate_per_hour = float(input("Enter Rate per Hour: "))
    hours_worked = float(input("Enter Hours Worked: "))

    # Compute salary
    overtime_hours = max(0, hours_worked - 40)
    overtime_pay = overtime_hours * (rate_per_hour * 1.5)
    basic_salary = (hours_worked * rate_per_hour) + overtime_pay

    employee = {
        "ID": emp_id,
        "Name": name,
        "Date Hired": date_hired,
        "Department": department,
        "Position": position,
        "Status": status,
        "Rate per Hour": rate_per_hour,
        "Hours Worked": hours_worked,
        "Overtime Pay": overtime_pay,
        "Total Salary": basic_salary
    }

    employees.append(employee)
    
    # Add employee to the respective category list
    if status == "Probationary":
        probationary_employees.append(employee)
    elif status == "Permanent":
        permanent_employees.append(employee)
    elif status == "Contractual":
        contractual_employees.append(employee)
        
    print("Employee added successfully!\n")

def display_employees():
    print("\n--- Employee Records ---")
    if not employees:
        print("No records found.\n")
        return

    emp_id = input("Enter Employee ID to view details (or press Enter to view all): ")
    
    if emp_id:
        for emp in employees:
            if emp["ID"] == emp_id:
                print("\n" + "-" * 40)
                for key, value in emp.items():
                    print(f"{key}: {value}")
                print("-" * 40)
                return
        print("Employee ID not found.\n")
    else:
        if probationary_employees:
            print("\n--- Probationary Employees ---\n")
            for emp in probationary_employees:
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Overtime Pay: ${emp['Overtime Pay']:.2f}, Total Salary: ${emp['Total Salary']:.2f}")

        if permanent_employees:
            print("\n--- Permanent Employees ---\n")
            for emp in permanent_employees:
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Overtime Pay: ${emp['Overtime Pay']:.2f}, Total Salary: ${emp['Total Salary']:.2f}")

        if contractual_employees:
            print("\n--- Contractual Employees ---\n")
            for emp in contractual_employees:
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Overtime Pay: ${emp['Overtime Pay']:.2f}, Total Salary: ${emp['Total Salary']:.2f}")

def edit_employee():
    print("\n--- Edit Employee ---")
    emp_id = input("Enter Employee ID to edit: ")
    
    for emp in employees:
        if emp["ID"] == emp_id:
            while True:
                print("\nSelect the field to edit:")
                print("1. Employee Name")
                print("2. Date Hired")
                print("3. Department")
                print("4. Position")
                print("5. Status")
                print("6. Rate per Hour")
                print("7. Hours Worked")
                print("8. Exit Editing")

                choice = input("Enter choice: ")
                
                if choice == "1":
                    new_name = input("Type new name: ")
                    if new_name and is_name_unique(new_name, emp["Name"]):
                        emp["Name"] = new_name
                        print("Name updated successfully!\n")
                    else:
                        print("Invalid! Name must be unique and different from the current name.\n")
                elif choice == "2":
                    emp["Date Hired"] = input("Enter New Date Hired: ") or emp["Date Hired"]
                elif choice == "3":
                    emp["Department"] = input("Enter New Department: ") or emp["Department"]
                elif choice == "4":
                    emp["Position"] = input("Enter New Position: ") or emp["Position"]
                elif choice == "5":
                    emp["Status"] = input("Enter New Status: ") or emp["Status"]
                elif choice == "6":
                    emp["Rate per Hour"] = float(input("Enter New Rate per Hour: ") or emp["Rate per Hour"])
                elif choice == "7":
                    emp["Hours Worked"] = float(input("Enter New Hours Worked: ") or emp["Hours Worked"])
                    overtime_hours = max(0, emp["Hours Worked"] - 40)
                    emp["Overtime Pay"] = overtime_hours * (emp["Rate per Hour"] * 1.5)
                    emp["Total Salary"] = (emp["Hours Worked"] * emp["Rate per Hour"]) + emp["Overtime Pay"]
                elif choice == "8":
                    print("Exiting editing mode.\n")
                    return
                else:
                    print("Invalid choice, please try again.\n")

def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input("Enter Employee ID to delete: ")
    
    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!\n")
            
            if emp in probationary_employees:
                probationary_employees.remove(emp)
            elif emp in permanent_employees:
                permanent_employees.remove(emp)
            elif emp in contractual_employees:
                contractual_employees.remove(emp)
                
            return
    print("Employee ID not found.\n")

# Main menu loop
while True:
    print("--- Call Center Payroll System ---")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Delete Employee")
    print("4. Display Employees")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        edit_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")
