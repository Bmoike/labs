# how can I make this code neater? Are there too many functions?

# list of student info
names = ["sandy cheeks", "Squidward tennisball", "patrick Star", "sheldon plankton"]
hometown = ["dallas", "Easter Island", "Rock city", "Chum Bucket"]
favorite_food = ["walnuts", "kelp", "krabby patties", "holograms"]


# asks user if they would like to see the list of students
def see_list():
    while True:
        total = input("Would you like to see the list of students?(yes/no): ")
        if total.lower() == "yes":
            for i, value in enumerate(names, start=1):
                print(f"{i}){value.title()}", end="  ")
            print()
            break
        elif total.lower() == "no":
            print("Going in blind is even more fun!\n")
            break
        else:
            print("Please choose a valid input")


# validation of users student choice
def validate_student():
    while True:
        # gets to choose to find a student with their name or with their number
        name_v_num = input("Would you like to search for a student with their name or their number?"
                           "Type in either name or number for your choice: ")
        name_v_num = name_v_num.lower()
        # search by name then returns the index of the student
        if name_v_num == "name":
            stu_name = input("Please enter the name of the student: ")
            stu_name = stu_name.lower()
            for i in names:
                if stu_name in i.lower():
                    place = names.index(i)
                    return place
        # search by the student number and returns the index by subtracting 1 from the option chosen
        elif name_v_num == "number":
            stu_num = input("Please choose a student number. (1-4): ")
            try:
                stu_num = int(stu_num)
                if 0 < stu_num < len(names) + 1:
                    return stu_num - 1
                else:
                    print("Please choose an integer from 1-4 only.\n")
                    continue
            except ValueError:
                print("Please choose an integer from 1-4 only.\n")
        # lets the user that they chose an invalid entry
        else:
            print("Please choose a valid entry from the options given.\n")


# validation of user choice to see favorite food, hometown of student, or neither
def validate_choice(student_num):
    while True:
        choice = input("Please choose either to see the students favorite food, hometown, or neither if you would "
                       "like to move on: ")
        choice = choice.lower()
        if choice in "favorite food":
            print(f"{names[student_num].title()} favorite food is {favorite_food[student_num].title()}")
            break
        elif choice in "hometown":
            print(f"{names[student_num].title()} hometown is {hometown[student_num].title()}")
            break
        elif choice == "neither":
            print("Less is more these days I guess.")
            break
        else:
            print("Please choose a valid entry as directed.")


# validation to break out of main loop
def loop_break():
    while True:
        loop = input("Would you like to see information on another student?(yes/no): ")
        if loop.title() == "Yes":
            return True
        elif loop.title() == "No":
            return False
        else:
            print("Please choose a valid input as directed.\n")


while True:
    # sees if user would like a list of all students
    see_list()

    # gets the user to choose a student from the list
    choose_student = validate_student()
    print(names[choose_student].title())

    # gets the user to choose if they want to see favorite food or hometown of the student
    validate_choice(choose_student)

    # breaks out of loop to end program
    loop_again = loop_break()
    print()
    if not loop_again:
        break
