current_year = 2023 #you can also get the current age using the datetime module

def is_student_adult():
    name = input("input your name: ")
    date_of_birth = int(input("input year of birth: "))
    age = current_year  -  date_of_birth
    if age >= 18:
        print(True)
        
    else:
        print(False)



is_student_adult()