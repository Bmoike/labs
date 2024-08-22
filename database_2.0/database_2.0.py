
student_directory = [
    {"name": "Sandy Cheeks",
     "hometown": "Dallas",
     "favorite_food": "Walnuts"},
    {"name": "Squidward Tennisball",
     "hometown": "Easter Island",
     "favorite_food": "Kelp"},
    {"name": "Patrick Star",
     "hometown": "Rock City",
     "favorite_food": "Krabby Patties"},
    {"name": "Sheldon Plankton",
     "hometown": "Chum Bucket",
     "favorite_food": "Holograms"}
]


# gets to know more about a student
def know_more():
    while True:
        # gets to choose to find a student with their name or with their number
        name_v_num = input("Would you like to search for a student with their name or their number? If not"
                           " then please type quit\n"
                           "(name/number/quit): ").lower()
        # search by name then prints the info of the student
        if name_v_num == "name":
            stu_name = input("Please enter the name of the student: ").title()
            for i in range(len(student_directory)):
                if stu_name in student_directory[i]["name"]:
                    home_v_food = input("Would you like to see this students favorite food or their hometown?(f/h)").lower()
                    if home_v_food == "f":

                        print(f"{student_directory[i]["name"]} likes {student_directory[i]["favorite_food"]}.")

                    elif home_v_food == "h":
                        print(f"{student_directory[i]["name"]} is from {student_directory[i]["hometown"]} ")

                    else:
                        print("Since that wasn't a valid entry I will tell you everything about this student")
                        print(f"{student_directory[i]["name"]} likes {student_directory[i]["favorite_food"]} and "
                              f"they're from {student_directory[i]["hometown"]}.")
                    break
                print("That student doesn't seem to be on record. Please try again.")

        # search by the student number to print the info of the student
        elif name_v_num == "number":
            stu_num = input(f"Please choose a student number. (1-{len(student_directory)}): ")
            try:
                stu_num = int(stu_num)
                if 0 < stu_num < len(student_directory) + 1:
                    home_v_food = input(
                        "Would you like to see this students favorite food or their hometown?(f/h)").lower()
                    if home_v_food == "f":

                        print(f"{student_directory[stu_num-1]["name"]} likes {student_directory[stu_num-1]["favorite_food"]}.")

                    elif home_v_food == "h":
                        print(f"{student_directory[stu_num-1]["name"]} is from {student_directory[stu_num-1]["hometown"]} ")

                    else:
                        print("Since that wasn't a valid entry I will tell you everything about this student")
                        print(f"{student_directory[stu_num-1]["name"]} likes {student_directory[stu_num-1]["favorite_food"]} and"
                              f" they're from {student_directory[stu_num-1]["hometown"]}.")

                else:
                    print(f"Please choose an integer from 1-{len(student_directory)} only.\n")
                    continue
            except ValueError:
                print(f"Please choose an integer from 1-{len(student_directory)} only.\n")
        # breaks the loop
        elif name_v_num == "quit":
            print()
            break

        # lets the user that they chose an invalid entry
        else:
            print("Please choose a valid entry from the options given.\n")


def break_new_student():
    while True:
        end_loop = input("Would you like to add another student?(yes/no): ").lower()
        if end_loop == "no":
            return True
        elif end_loop == "yes":
            break
        else:
            print("Please enter either yes or no only")


# adds new student
def get_new_student():
    new_dict = []
    while True:
        new_name = input("Please enter the name of the new student: ").title()
        new_home = input("Please enter the hometown of the new student: ").title()
        new_food = input("Please enter the favorite food of the new student: ").title()

        new_dict.extend([{"name": new_name, "hometown": new_home, "favorite_food": new_food}])

        break_loop = break_new_student()
        if break_loop:
            for i in range(len(new_dict)):
                print(f"You added {new_dict[i]["name"]} to the student directory")
            return new_dict


# views list
def list_names(students):
    for i, name in enumerate(students, start=1):
        print(f"{i}. {students[i - 1]["name"]}")
    while True:
        more_info = input("Would you like to know more about a certain student?(yes/no): ").lower()
        match more_info:
            case "yes":
                know_more()

            case "no":
                break
            case _:
                print("Please choose either yes or no.")


while True:
    # call to add new students to the list
    print("Would you like to add a new student, view existing students, or quit the program?")
    option = input("(add/view/quit): ").lower()
    match option:
        case "add":
            # adds new student to list of current student names
            newbies = get_new_student()
            student_directory += newbies
        case "view":
            # prints list of current student names
            list_names(student_directory)

        case "quit":
            print("Have a nice day!")
            break
        case _:
            print("Please enter a valid input as directed in the instructions.\n")
