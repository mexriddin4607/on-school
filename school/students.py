def register_student(student : dict[str, dict[str, str]]) -> None:
    
    student['name'] = input("Enter your name: ")

    student['course'] = []

    student_email = input("Enter your email: ")
    student_password = input("Enter your password: ")
    
    
    student['pas_log'] = {}
    student['pas_log']['log'] = student_email
   
    return student

def login_student(students_data: list) -> str | None:
   
    
    login = input("Enter your email: ")
    passwod = input("Enter your password: ")

    student_dict = {}
    student_dict['log'] = login
    student_dict['pass'] = passwod
    
    
    for user in students_data:
        if(user['pas_log']) == student_dict:
            print("Login successful! Welcome back, {}.".format(user['name']))
            return user
    return None


def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:

    courses_number = int(input("Select a course number to enroll: "))

    if courses_number - 1 > len(courses_data) or courses_number - 1 < 0:
        print("\nSiz tanlagan nommirda kurs yo`q iltimos tikshirib qaytadan tanlang!\n")
        return None
    else:
        print("Successfully enrolled in {}!\n".format(courses_data[courses_number - 1]["course_name"]))
        return courses_data[courses_number - 1]
   