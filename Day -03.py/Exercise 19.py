# Hospital Appointment System


class Patient:


    # Constructor

    def __init__(self, patient_id, name, age, appointment_time):

        self.patient_id = patient_id

        self.name = name

        self.age = age

        self.appointment_time = appointment_time



    # Display Details

    def display_details(self):

        print("\nPatient Details")

        print("Patient ID :", self.patient_id)

        print("Name :", self.name)

        print("Age :", self.age)

        print("Appointment Time :", self.appointment_time, ":00")



    # Check Patient Category

    def check_patient_type(self):

        if self.age >= 60:

            print("Senior Citizen")

        elif self.age >= 18:

            print("Adult")

        else:

            print("Child")



    # Check Appointment Time

    def check_appointment(self):

        if 6 <= self.appointment_time < 12:

            print("Morning Appointment")

        elif 12 <= self.appointment_time < 18:

            print("Afternoon Appointment")

        else:

            print("Evening Appointment")



# Objects

patient1 = Patient(201, "Anusha", 23, 10)

patient2 = Patient(202, "Ramesh", 65, 15)

patient3 = Patient(203, "Arya", 12, 19)



patient1.display_details()

patient1.check_patient_type()

patient1.check_appointment()


patient2.display_details()

patient2.check_patient_type()

patient2.check_appointment()


patient3.display_details()

patient3.check_patient_type()

patient3.check_appointment()