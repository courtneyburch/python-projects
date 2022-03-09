# CIT 244 Program 1 Courtney Burch
from tabulate import tabulate  # package to display tabular data
import pickle


class Contact:  # define Contact class
    contact_list = []  # list of class instances

    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def get_contact_data(self):  # class method to return contact data
        return [self.f_name, self.l_name, self.email]


# read data from pickle file
def read_data():
    try: # if save_contacts file exist, import the data
        with open('save_contacts.pkl', 'rb') as file:
            saved_contacts = pickle.load(file)
        file.close()
    except: # if save_contacts file does not exist, return and empty list
        saved_contacts = []
    return saved_contacts


# display program options
def display_options():
    print("\nWhat would you like to do?")

    selection = str(input(  # accept user input for program options
        "    Press 1 to display all contacts\n    Press 2 to create a new contact\n    Press 3 to exit\n"))

    while selection not in ('1', '2', '3'):  # reject invalid input
        selection = input(
            "Sorry ,that is not a valid selection.\n     Press 1 to display all contacts\n     Press 2 to create a new contact\n     Press 3 to exit \n")

    return selection  # return program option to main program

 # function to create a contact
def create_contact():

    # get first name, last name, email from user input
    first_name = input("What is the first name of the new contact? ")
    last_name = input("What is the last name of the new contact? ")
    email_address = input("What is the email address of the new contact? ")

    # valid email address must inlcude @ and .
    while "@" not in email_address or "." not in email_address:
        print(f"Please enter a valid email address.")
        email_address = input("What is the email address of the new contact? ")

    # create a new instance of Contact Class
    new_contact = Contact(first_name, last_name, email_address)
    contact_data = Contact.get_contact_data(new_contact)  # get instance data

    # append instance data to list of class instances
    Contact.contact_list.append(contact_data)
    print("Contact has been added!")


# display list of class instances in table format

def display_contacts():
    print(tabulate(Contact.contact_list, headers=[
          "First Name", 'Last Name', "Email Address"]))

# main program
def main():
    while True:
        option = display_options()  # get user selection from program options
    
        if option == "3":  # quit program
            with open('save_contacts.pkl', 'wb') as file:  # open pickle file for writing
                # write contact list to file
                pickle.dump(Contact.contact_list, file)
                file.close()
                print('Goodbye!')
                break

        if option == "2":  # create contact, restart program options from beginning
            create_contact()
            continue
        

        if option == '1':  # display all contacts, restart program options from beginning
            display_contacts()
            continue


# display welcome only once
print("Welcome to the Contact List!")
# add return value of read_data function to the Contace class instance list
Contact.contact_list.extend(read_data())
main()  # run main program
