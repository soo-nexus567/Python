# Jonathan Soo
# Date: 02/06/25
# Purpose: Program that performs as a Employee Contact List for the first lab of python programming
def print_list(contacts):
    # Print a table of the contact list
    print("================== CONTACT LIST ======================")
    print("Last Name             First Name            Phone")
    print("====================  ====================  ==========")
    for key, value in contacts.items():
        print(f'{value[1]:22}{value[0]:22}{str(key)}')
def add_contact(contact_list, /, *, id, first_name, last_name):
    #Add a contact to a contact list
    if (id not in contact_list):
        contact_list[int(id)] = [first_name, last_name]
    else:
        return "ID not found"
def modify_contact(contact_list, /, *, id, first_name, last_name):
    # Modify a certain index in the contact list
    # if (id in contact_list):
    contact_list[int(id)] = [first_name, last_name]
    # else:   
    #     return "ID not found"
    return contact_list[int(id)]
def delete_contact(contact_list, /, *, id):
    # Delete a element in contact list
    if  (int(id) in contact_list):
        contact_list.pop(id)
    else:
        return "ID not Found"
    return contact_list[id]
def sort_contacts(contact_list):
    # Sort the contact list, by the first or last name
    sorted(contact_list, key= lambda x: (contact_list[x][1], contact_list[x][0]))
    return contact_list
def find_contact(contact_list, /, *, find):
    empty = {}
    if (isinstance(find, int)):
        print("==================  FOUND CONTACT(S) ======================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key, value in contact_list.items():
            empty[key] = value
            if (key == int(find)):
                print(f'{value[0]:22}{value[1]:22}{str(key)}')
    else:
        print("==================  FOUND CONTACT(S) ======================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key, value in contact_list.items():
            empty[key] = value
            if (find in value[0] or find in value[1]):
                print(f'{value[1]:22}{value[0]:22}{str(key)}')
    return_value = sort_contacts(empty)
    return return_value
    