from collections import UserDict

class Field:
    def __init__(self, value):
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
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = ''

    def edit_phone(self,old_phone: Phone, new_phone:Phone):
        for i, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[i] = new_phone
                return f'Phone {old_phone} change on {new_phone}'
        return f'Record dont have phone {old_phone}'
                
    
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

if __name__ == '__main__':
    address_book = AddressBook()
    name = Name('Bob')
    phone1 = Phone('+0987654321')
    rec1 = Record(name,phone1)

    phone2 = Phone('+1234567890')
    rec1.edit_phone(phone1,phone2)
    
    address_book.add_record(rec1)
    print(address_book)

    # rec1.delete_phone(phone2)
    # print(rec1)

    address_book.find_phone(name)
    