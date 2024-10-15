import pytermgui as ptg
import mysql.connector

# MySQL connection 
db = mysql.connector.connect(
    host="localhost",
    user="python",
    password="Password@123",
    database="heal_id"
)
cursor = db.cursor()

def main_menu():
    with ptg.WindowManager() as manager:
        window = (
            ptg.Window("HEAL-ID System", box="DOUBLE")
            .set_title("Main Menu")
            .center()
        )

        window.add(
            ptg.Button("Sign in as User", lambda *_: user_menu()),
            ptg.Button("Sign in as Doctor", lambda *_: doctor_menu()),
            ptg.Button("Exit", lambda *_: manager.stop()),
        )

        manager.add(window)
        manager.run()

def user_menu():
    pass

def doctor_menu():
    pass

def view_patient_history(aadhar_number):
    pass

def doctor_form():
    with ptg.WindowManager() as manager:
        window = (
            ptg.Window("Doctor's Form", box="DOUBLE")
            .set_title("Patient Visit")
            .center()
        )

        aadhar_input = ptg.InputField("Aadhar Number: ")
        reason_input = ptg.InputField("Reason for Visit: ")
        diagnosis_input = ptg.InputField("Diagnosis: ")
        treatment_input = ptg.InputField("Treatment Plan: ")

        def submit_form():
            pass

        window.add(
            aadhar_input,
            reason_input,
            diagnosis_input,
            treatment_input,
            ptg.Button("Submit", lambda *_: submit_form()),
            ptg.Button("Back", lambda *_: manager.stop()),
        )

        manager.add(window)
        manager.run()

if __name__ == "__main__":
    main_menu()
