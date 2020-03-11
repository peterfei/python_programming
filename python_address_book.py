#coding utf-8
import os,pickle
class AddressBook(object):
    def __init__(self,name=None,address=None,email=None,tell=None):
        self.name = name
        self.address = address
        self.email = email
        self.tell = tell
        self.contacts = {}
        self.filename = "addressbook.vbs"

    def  add(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename)>0:
                myAddressBook = open(self.filename,'rb')
                data = pickle.load(myAddressBook)
                myAddressBook.close()
            else:
                myAddressBook = open(self.filename,'wb')
                data={}
            contact = self.getDetailsFromUser()
            data[contact['Name']] = contact
            myAddressBook = open(self.filename, 'wb')
            pickle.dump(data, myAddressBook)
            myAddressBook.close()
            print('Contact Added Successfully!')

        except:
            print('There was an error! Contact was not added.')
        finally:
            myAddressBook.close()

    def getDetailsFromUser(self):
        try:
            self.contacts['Name'] = raw_input('Enter  Name: ')
            self.contacts['Address'] = raw_input('Enter  Address: ')
            self.contacts['Email'] = raw_input('Enter Email: ')
            self.contacts['Tell'] = raw_input('Enter Tell: ')
            return self.contacts
        except KeyboardInterrupt as error:
            raise  error

    def displayContacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'rb')
            data = pickle.load(myAddressBook)
            myAddressBook.close()
            if data:
                for records in data.values():
                    print(records)
            myAddressBook.close()
        else:
            print('No Record in database.')
if __name__ ==  "__main__":
    myBook = AddressBook()
    print('Plz type your chiose:')
    while True:
        choise =  int(input("your choise:"))
        if choise == 1:
            myBook.add()
        elif choise==2:
            myBook.displayContacts()
