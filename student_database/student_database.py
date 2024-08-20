# how can I make this code neater?

# list of student info
names = ["sandy cheeks", "Squidward tennisball", "patrick Star", "sheldon plankton"]
hometown = ["dallas", "Easter Island", "Rock city", "Chum Bucket"]
favorite_food = ["walnuts", "kelp", "krabby patties", "holograms"]


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
        student = input("Please choose a student number. (1-4): ")
        try:
            student = int(student)
            if student.is_integer() and 0 < student < len(names) + 1:
                return student
            else:
                print("Please choose an integer from 1-4 only.")
                continue
        except ValueError:
            print("Please choose an integer from 1-4 only.")


# validation of user choice to see favorite food, hometown of student, or neither
def validate_choice(student_num):

    while True:
        choice = input("Please choose either to see the students favorite food, hometown, or neither if you would "
                       "like to move on: ")
        if choice.lower() in "favorite food":
            print(f"{names[student_num - 1].title()} favorite food is {favorite_food[student_num - 1].title()}")
            break
        elif choice.lower() in "hometown":
            print(f"{names[student_num - 1].title()} hometown is {hometown[student_num - 1].title()}")
            break
        elif choice.lower() == "neither":
            print("Less is more these days I guess.")
            break
        else:
            print("Please choose a valid entry as directed.")

        # try:
        #     choice = int(choice)
        #     if choice.is_integer() and 0 < choice < 4:
        #         return choice
        #     else:
        #         print("Please choose an integer from 1-3 only.")
        # except ValueError:
        #     print("Please choose an integer from 1-3 only.")


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
    print(names[choose_student - 1].title())

    # gets the user to choose if they want to see favorite food or hometown of the student
    validate_choice(choose_student)

    # breaks out of loop to end program
    loop_again = loop_break()
    print()
    if not loop_again:
        break
