from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name: Name, phone: Phone):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def add(self, phone: Phone):
        self.phones.append(phone)
    
    def delete_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, name: Name, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone == old_phone:
                self.delete_phone(phone)
                self.add(new_phone)
    
    def __str__(self) -> str:
        return str(f'{self.name}: {", ".join(str(p) for p in self.phones)}')

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def __str__(self):
        return '\n'.join([str(rec) for rec in self.data.values()])
    
    def find_phone(self, name:Name):
        if name in self.data:
            return self.data[name]
        else:
            return f'There is no contact with name {name}'