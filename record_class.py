from name_phone_birthday_class import Birthday, Phone, Name
from custom_errors import BirthdayError, PhoneError 

class Record:
    
    def __init__(self, name):
        
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def add_phone(self, phone):
        
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        

    def remove_phone(self, phone):
        if not self.find_phone(phone):
            raise PhoneError("This phone number does not exist.")
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not self.find_phone(old_phone):
            raise PhoneError("This old phone number does not exist.")
        if self.find_phone(new_phone):
            raise PhoneError("This new phone number already exists.")
        
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone) 
                        
        
    def find_phone(self, phone):
        
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise BirthdayError ("This birthday is allredy added!")

    
        

    def __str__(self):
        
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, Birthday: {self.birthday}"