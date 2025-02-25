from contacts import *
contactList = {}
while True:
    print("\n      *** EMPLOYEE CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort contact")
    print("6. Find contact")
    print("7. Exit the program\n")
    menuChoice = int(input("Enter menu choice: "))
    print()
    if (menuChoice == 1):
        print_list(contactList)
    if (menuChoice == 2):
        id = input("Enter phone number: ")
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        add_contact(contactList, id = id, first_name = firstName, last_name=lastName)
    elif(menuChoice == 3):
        id = input("Enter phone number: ")
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        modify_contact(contactList, id = id, first_name = firstName, last_name=lastName)
    elif(menuChoice == 4):       
        id = input("Enter phone number: ")
        state = delete_contact(contactList, id=id)
    elif (menuChoice == 5):
        sort_contacts(contactList)
    elif (menuChoice == 6):
        find = input("Enter find value: ")
        find_contact(contactList, find=find)
    elif(menuChoice ==7):
        break