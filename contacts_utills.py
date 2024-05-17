from error_decorator import input_error
from adress_book_class import AddressBook
from record_class import Record


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return f"Contact does not exist." 
    record.edit_phone(old_phone, new_phone)
    
    return "Contact changed."

@input_error
def show_phone(args: list[str], book: AddressBook)->str:
    name,  = args
    record = book.find(name)
    if record is None:
        return f"Contact does not exist."
    if not record.phones:
        return "Contact has no phone numbers."
    
    return "; ".join(str(phone) for phone in record.phones)

@input_error
def all_contacts(book: AddressBook):
    if not book.data:
        return "There are no contacts."
    str_s = 'All contacts: \n'
    for record in book.data.values():
        str_s += f"{record}\n"
            
    return str_s[:len(str_s)-1]

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args  
    record = book.find(name)
    if record is None:
        return f"Contact does not exist."
    record.add_birthday(birthday)

    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook)->str:
    name,  = args
    record = book.find(name)
    if record is None:
        return f"Contact does not exist."
    if not record.birthday:
        return "Birthday is not added"
    
    return record.birthday

def birthdays(book: AddressBook)->list:
    if not book.data:
        return "There are no contacts."
    birth_info = book.get_upcoming_birthdays()
    if not birth_info:
        return 'There are no birthdays this week'
        
    str_s = 'This week birthdays: \n'
    for birth_dict in birth_info:
        str_s += f"{birth_dict}\n"
            
    return str_s[:len(str_s)-1]