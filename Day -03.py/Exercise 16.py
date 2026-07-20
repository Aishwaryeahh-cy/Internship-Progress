class Employee:

    # Constructor
    def __init__(self, employee_id, employee_name, days_present):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.days_present = days_present


    # Display employee details
    def display_details(self):

        print("\nEmployee Details")
        print("Employee ID :", self.employee_id)
        print("Employee Name :", self.employee_name)
        print("Days Present :", self.days_present)


    # Calculate attendance percentage
    def check_attendance(self):

        working_days = 5

        percentage = (self.days_present / working_days) * 100


        print("Attendance Percentage :", percentage, "%")


        # if-else condition

        if percentage >= 90:
            print("Excellent Attendance")

        elif percentage >= 75:
            print("Good Attendance")

        else:
            print("Needs Improvement")



# Creating Objects

emp1 = Employee(101, "Aliya", 5)

emp2 = Employee(102, "Rahul", 3)



# Calling methods

emp1.display_details()
emp1.check_attendance()


emp2.display_details()
emp2.check_attendance()