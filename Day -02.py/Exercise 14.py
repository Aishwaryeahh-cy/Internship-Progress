from abc import ABC, abstractmethod


# ---------------- ABSTRACT CLASS ----------------

class Employee(ABC):

    def __init__(self, emp_id, name):

        self.emp_id = emp_id
        self.name = name


    @abstractmethod
    def calculate_salary(self):
        pass


    def calculate_tax(self, salary):

        if salary <= 30000:
            tax = salary * 0.05

        elif salary <= 70000:
            tax = salary * 0.10

        else:
            tax = salary * 0.20


        return tax



    def generate_salary_slip(self):

        salary = self.calculate_salary()

        tax = self.calculate_tax(salary)

        net_salary = salary - tax


        print("\n------ SALARY SLIP ------")

        print("Employee ID :", self.emp_id)
        print("Name :", self.name)

        print("Gross Salary :", salary)
        print("Tax Deduction :", tax)
        print("Net Salary :", net_salary)



# ---------------- FULL TIME EMPLOYEE ----------------

class FullTimeEmployee(Employee):


    def __init__(
        self,
        emp_id,
        name,
        monthly_salary
    ):

        super().__init__(
            emp_id,
            name
        )

        self.monthly_salary = monthly_salary



    # Method overriding
    def calculate_salary(self):

        bonus = self.monthly_salary * 0.10

        return self.monthly_salary + bonus



# ---------------- PART TIME EMPLOYEE ----------------

class PartTimeEmployee(Employee):


    def __init__(
        self,
        emp_id,
        name,
        hours_worked,
        hourly_rate
    ):

        super().__init__(
            emp_id,
            name
        )

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate



    # Method overriding
    def calculate_salary(self):

        return (
            self.hours_worked *
            self.hourly_rate
        )



# ---------------- INTERN CLASS ----------------

class Intern(Employee):


    def __init__(
        self,
        emp_id,
        name,
        stipend
    ):

        super().__init__(
            emp_id,
            name
        )

        self.stipend = stipend



    # Method overriding
    def calculate_salary(self):

        return self.stipend



# ---------------- PAYROLL CLASS ----------------

class Payroll:


    def __init__(self):

        self.employees = []



    def add_employee(self, employee):

        self.employees.append(employee)

        print(
            "Employee added successfully"
        )



    def process_payroll(self):

        for employee in self.employees:

            employee.generate_salary_slip()



# ---------------- MAIN PROGRAM ----------------


payroll = Payroll()



# Creating employees

emp1 = FullTimeEmployee(
    101,
    "Anusha",
    50000
)


emp2 = PartTimeEmployee(
    102,
    "Rahul",
    80,
    300
)


emp3 = Intern(
    103,
    "Priya",
    15000
)



# Adding employees

payroll.add_employee(emp1)

payroll.add_employee(emp2)

payroll.add_employee(emp3)



# Generate salary slips

payroll.process_payroll()