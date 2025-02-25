from contact import *
contactList = []
while True:
    print("\n      *** EMPLOYEE CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program\n")
    try:
        menuChoice = int(input("Enter menu choice: "))
        print()
        if (menuChoice == 1):
            print_list(contactList)
        if (menuChoice == 2):
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            add_contact(contactList, first_name = firstName, last_name=lastName)
        elif(menuChoice == 3):
            try:
                indexNumber = int(input("Enter the index number: "))
                firstName = input("Enter first name: ")
                lastName = input("Enter last name: ") 
                state = modify_contact(contactList, first_name = firstName, last_name=lastName, index = indexNumber)
                if (state == False):
                    print("Invalid index number.")
            except:
                print("Invalid index number.")
        elif(menuChoice == 4):
            try:
                indexNumber = int(input("Enter the index number: "))
                state = delete_contact(contactList, index=indexNumber)
                if (state == False):
                    print("Invalid index number.")
            except:
                print("Invalid index number.")
        elif (menuChoice == 5):
            sort_contacts(contactList, column=0)
        elif (menuChoice == 6):
            sort_contacts(contactList, column=1)
        elif(menuChoice ==7):
            break
    except:
        print("Invalid index number.")