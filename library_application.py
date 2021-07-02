
# Book properties and their explanation
'''
book_id which will act as an identifier
book_name which is name of book
book_owned_by will hold the owner name of book
book_status will hold value whether it is assigned or not
duration_of_book will hold how long user is going to own the book
'''

# duration_of_book
'''duration_of_book should be integer value
If duration_of_book set to -1 means book is not reserved
Any positive integer value will be appropriate for duration_of_book
By default maximum assign time will be 14, irrespective of requested duration
'''

# Operation available in this application
'''
CURD Operations are available in the library application
C -> Create
U -> Update
r -> Read
D -> Delete
'''

# Methods and their functions
'''
Librray
Method add_book -> Adds book to the library
Method delete_book -> Deletes existing book from the library
Method view_all_books -> Displays all book from the library
Method view_book -> Displays requested book based on book id
Method assign_book -> Assigns the book to the requested user if it is not assigned to any one
Method un_assign_book ->Un-assigns the book from the user if it is assigned
Method display_book_list -> Displays the library content 
'''
import logging
import sys

log = logging.getLogger()
log.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stdout_handler)

book_dict = {"books": {"book_list": []}}


class Book:

    def __init__(self, book_id=None, book_name=None, book_owned_by=None, book_status='Not Assigned',
                 duration_of_book=-1):
        self.book_id = book_id
        self.book_name = book_name
        self.book_owned_by = book_owned_by
        self.book_status = book_status
        self.duration_of_book = duration_of_book


class LibraryOperation:

    def add_book(self):
        try:
            self.display_book_list()
            log.info(f'Available books in the library: \n {book_dict} \n')
            book_id = int(input("Enter the book id to be added: "))
            book_name = input("Enter the book name to be added: ")
            exist_flag = 0
            for iterator in range(len(book_dict['books']['book_list'])):
                if book_dict['books']['book_list'][iterator]['Book_id'] != book_id:
                    continue
                elif book_dict['books']['book_list'][iterator]['Book_id'] == book_id:
                    log.info(f'Book id already exists, kindly give different id while adding book')
                    exist_flag = 1
                    break
            if exist_flag == 0:
                val = Book(book_id=book_id, book_name=book_name)
                book_dict['books']['book_list'].append({"Book_id": val.book_id, "Book_Name": val.book_name, "Book_Status": val.book_status,
                             "Book_Owned_by": val.book_owned_by,
                             "Booked_Duration": val.duration_of_book})
                log.info(f'Book Added Successfully \n \n {book_dict}')


        except Exception as e:
            log.exception(e)

    def delete_book(self):
        try:
            self.display_book_list()
            log.info(f'Available books in the library: \n {book_dict} \n')
            if len(book_dict['books']['book_list']) > 0:
                book_id = int(input("Enter the book id to be deleted: "))
                for iterator in range(len(book_dict['books']['book_list'])):
                    requested_book = book_dict['books']['book_list'][iterator]
                    if requested_book['Book_id'] == book_id:
                        book_dict['books']['book_list'].pop(iterator)
                        log.info(f'Successfully deleted \n Available Book List \n {book_dict}')
                        break
                else:
                    log.warning("Unable to deleted requested book as it doesn't exist")

        except Exception as e:
            log.exception(e)

    def view_all_books(self):
        try:
            self.display_book_list()
            if len(book_dict['books']['book_list']) > 0:
                log.info(f'Available books are: \n{book_dict} \n')
            else:
                log.warning("No books are found in library")

        except Exception as e:
            log.exception(e)

    def view_book(self):
        try:
            self.display_book_list()
            log.info(f'Available books in the library: \n {book_dict} \n')
            if len(book_dict['books']['book_list']) > 0:
                book_id = int(input("Enter the book id to be viewed: "))
                for iterator in range(len(book_dict['books']['book_list'])):
                    requested_book = book_dict['books']['book_list'][iterator]
                    if requested_book['Book_id'] == book_id:
                        log.info(f'Request Book Is: \n {requested_book}')
                        break
                else:
                    log.warning("Requested book is not found in library")
            else:
                log.warning("No books are available in library")

        except Exception as e:
            log.exception(e)

    def assign_book(self):
        try:
            self.display_book_list()
            log.info(f'Available books in the library: \n {book_dict} \n')
            if len(book_dict['books']['book_list']) > 0:
                book_id = int(input("Enter the book id to be assigned: "))
                book_owned_by = input("Enter requester name of book: ")
                duration_of_book = int(input("Enter the duration to own book (With valid integer number): "))

                for iterator in range(len(book_dict['books']['book_list'])):
                    requested_book = book_dict['books']['book_list'][iterator]
                    if requested_book['Book_id'] == book_id:
                        if requested_book['Book_Status'] == 'Assigned':
                            log.info("Requested book is already assigned")
                            break
                        if duration_of_book > 14 or duration_of_book <= 0:
                            log.info("Given duration doesn't suite expectation, hence assigning default duration as "
                                     "14 \n")
                            duration_of_book = 14
                        requested_book['Book_Owned_by'] = book_owned_by
                        requested_book['Booked_Duration'] = duration_of_book
                        requested_book['Book_Status'] = 'Assigned'
                        log.info(f'Successfully assigned book to {book_owned_by} as per request \n{requested_book}')
                        break
                else:
                    log.warning("Requested book is not available")
            else:
                log.warning("No books are available in library")

        except Exception as e:
            log.exception(e)

    def un_assign_book(self):
        try:
            self.display_book_list()
            log.info(f'Available books in the library: \n {book_dict} \n')
            if len(book_dict['books']['book_list']) > 0:
                book_id = int(input("Enter the book id to be un assigned: "))
                for iterator in range(len(book_dict['books']['book_list'])):
                    requested_book = book_dict['books']['book_list'][iterator]
                    if requested_book['Book_id'] == book_id:
                        if requested_book['Book_Status'] == 'Not Assigned' or requested_book['Booked_Duration'] == -1 or\
                                requested_book['Book_Owned_by'] == None:
                            log.info(f'Requestd book is already unassigned')
                            break
                        requested_book['Book_Owned_by'] = None
                        requested_book['Booked_Duration'] = -1
                        requested_book['Book_Status'] = 'Not Assigned'
                        log.info(f'Successfully un assigned book {book_id} as per request \n {requested_book}')
                        break
                else:
                    log.warning("Requested book is not available in library")
            else:
                log.warning("No books are available in library")

        except Exception as e:
            log.exception(e)

    def display_book_list(self):
        try:
            book_dict['books']['book_list'].append({'Book_id': 1, 'Book_Name': 'Book1', 'Book_Status': 'Not Assigned', 'Book_Owned_by': None, 'Booked_Duration': -1})
            book_dict['books']['book_list'].append(
                {'Book_id': 2, 'Book_Name': 'Book2', 'Book_Status': 'Assigned', 'Book_Owned_by': 'Pavan',
                 'Booked_Duration': 14})
        except Exception as e:
            log.exception(e)


def available_action():
    obj = LibraryOperation()
    log.info("Welcome to library\n")
    log.info("For better user experience I have added two books by default in library\n")
    log.info("Here are the available options: ")
    log.info("""
    To View books enter 1
    To assign a book enter 2
    To un assign a book Enter 3
    To add a book enter 4
    To delete a book enter 5
    To view a particular book 6
    """)
    try:
        user_input = int(input("What do you want to do?: "))
        if type(user_input) is int:
            if user_input == 1:
                obj.view_all_books()
            elif user_input == 2:
                obj.assign_book()
            elif user_input == 3:
                obj.un_assign_book()
            elif user_input == 4:
                obj.add_book()
            elif user_input == 5:
                obj.delete_book()
            elif user_input == 6:
                obj.view_book()
            else:
                log.error('Please enter valid action')
        else:
            log.error('Given input is not valid action, please provide valid action')
    except Exception as e:
        log.exception(e)


available_action()

