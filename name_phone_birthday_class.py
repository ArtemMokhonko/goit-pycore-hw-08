import re
from field_class import Field
from datetime import datetime
from custom_errors import BirthdayError, PhoneError, NameError



class Name(Field):
    
    def __init__(self, name: str)-> None:
        
        if not name[0].isupper():
            raise NameError("Name must start with a capital letter")
        if len(name) <= 2:
            raise NameError("Name must be longer than 2 letters")
        super().__init__(name)
        

class Phone(Field):
    
    def __init__(self, phone):
        
        if not re.fullmatch(r'\d{10}', phone):
            raise PhoneError("Phone number must be 10 digits")
        super().__init__(phone)


class Birthday(Field):
    def __init__(self, birthday):
        try:
            
            birthday_day = datetime.strptime(birthday, "%d.%m.%Y").date()
            today = datetime.today().date()
            if birthday_day > today:
                raise BirthdayError ("Invalid date, after today!")
            super().__init__(birthday_day)
        except ValueError:
            raise BirthdayError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        
        return datetime.strftime(self.value, "%d.%m.%Y")