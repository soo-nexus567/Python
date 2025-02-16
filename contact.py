# Jonathan Soo
# Date: 02/06/25
# Purpose: Program that performs as a Employee Contact List for the first lab of python programming
def print_list(contacts):
    # Print a table of the contact list
    print("================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
def add_contact(contact_list, /, *,first_name, last_name):
    #Add a contact to a contact list
    contact_list.append([first_name, last_name])
def modify_contact(contact_list, /, *, first_name, last_name, index):
    # Modify a certain index in the contact list
    if (index < len(contact_list)):
        contact_list[index] = [first_name, last_name]
        return True
    else:
        return False
def delete_contact(contact_list, /, *, index):
    # Delete a element in contact list
    if  (index < len(contact_list)):
        contact_list.pop(index)
        return True
    else:
        return False
def sort_contacts(contact_list, /, *, column):
    # Sort the contact list, by the first or last name

    if (column == 0):
        contact_list.sort(key=lambda x: x[0].lower())
    elif(column == 1):
        contact_list.sort(key=lambda x: x[1].lower())
    
    