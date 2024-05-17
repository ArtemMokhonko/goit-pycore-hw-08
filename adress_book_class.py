from collections import UserDict
from record_class import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        

    def find(self, name) -> Record:
        
        return self.data.get(name)


    def delete(self, name) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for record in self.data.values():
            birthday = record.birthday.value
            
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:  # якщо минув
                birthday_this_year = birthday.replace(year=today.year + 1) 
            
            delta = birthday_this_year - today
            
            if 0 <= delta.days <= 7:
                if birthday_this_year.weekday() > 4:  
                    
                    days_till_monday = 7 - birthday_this_year.weekday()
                    congratulation_date = birthday_this_year + timedelta(days=days_till_monday)
                else:
                    congratulation_date = birthday_this_year
                
                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })
        return upcoming_birthdays