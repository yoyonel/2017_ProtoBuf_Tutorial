#! /usr/bin/python

import addressbook_pb2
import sys

# Manual Reflexivity
phone_number_types = {
    addressbook_pb2.Person.MOBILE: "Mobile",
    addressbook_pb2.Person.HOME: "Home",
    addressbook_pb2.Person.WORK: "Work",
}


# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book):
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        if person.HasField('email'):
            print("  E-mail address:", person.email)

        for phone_number in person.phones:
            print("  {PHONE_NUMBER_TYPE} phone #: {PHONE_NUMBER}".format(
                PHONE_NUMBER_TYPE=phone_number_types.get(phone_number.type, "<UNKNOW_TYPE>"),
                PHONE_NUMBER=phone_number.number
            ))


# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)
