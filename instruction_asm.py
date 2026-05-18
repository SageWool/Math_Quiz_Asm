# checks users enter yes (y) or no (n)

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y /
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

every round you will get some questions related to math,
 it will contain multiplication, division, subtraction, and addition, answer correctly!!

    """)


# Main routine
print()
print("✖️➕➖Welcome to the math quiz game➖➕✖️")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to see the instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


#Display the instructions if the user wants to see them...

print()
print("Program continues")


