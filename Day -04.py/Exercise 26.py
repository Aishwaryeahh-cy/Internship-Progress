# Employee Attendance Management System

class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, days_present):

        # Encapsulation (Private Variables)
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
        self.__days_present = days_present


    # Calculate Attendance Percentage
    def calculate_percentage(self):

        working_days = 30

        percentage = (self.__days_present / working_days) * 100

        return percentage


    # Attendance Status
    def attendance_status(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "Excellent"

        elif percentage >= 75:
            return "Good"

        else:
            return "Needs Improvement"


    # Display Report
    def display_report(self):

        print("\n------ EMPLOYEE REPORT ------")

        print("Employee ID :", self.__emp_id)
        print("Employee Name :", self.__name)
        print("Department :", self.__department)
        print("Days Present :", self.__days_present)
        print("Attendance Percentage :", round(self.calculate_percentage(),2),"%")
        print("Status :", self.attendance_status())


# Main Function
def main():

    emp_id = int(input("Enter Employee ID : "))
    name = input("Enter Employee Name : ")
    department = input("Enter Department : ")
    days = int(input("Enter Days Present : "))

    emp = Employee(emp_id, name, department, days)

    emp.display_report()


main()