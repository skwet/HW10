from classes_bot import Field,AddressBook,Record,Name,Phone

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough data'
        except KeyError:
            return 'Are you sure that you added this contact?.Try again'
        except ValueError:
            return 'Impossible to add or change this number'
    return wrapper

adress_book = AddressBook()

def hello(*args):
    return 'What`s up?How can I help you?'

@input_error
def add(*args):
    input_split = args[0].split()
    name = Name(input_split[0])
    phone = Phone(input_split[1])
    rec = Record(name,phone)
    adress_book.add_record(rec)
    return f'U added {name} with phone {phone}'

@input_error
def change(*args):
    input_split = args[0].split()
    name = Name(input_split[0])
    old_phone = Phone(input_split[1])
    new_phone= Phone(input_split[2])
    rec = Record(name,old_phone)
    rec.edit_phone(old_phone,new_phone)
    adress_book.add_record(rec)
    if new_phone in rec.phones:
        return 'Phone has been changed'
    raise ValueError

@input_error
def delete_phone(*args):
    input_split = args[0].split()
    name = input_split[0]
    phone = input_split[1]
    rec = Record(name,phone)
    rec.delete_phone(phone)
    if phone not in rec.phones:
        return 'Phone has been removed'   
    raise ValueError
    
@input_error
def phones(*args):
    input_split = args[0].split()
    name = input_split[0]
    phone_number = adress_book[name]
    if not name:
        raise KeyError
    return f'{phone_number}'

def show_all(*args):
    print(adress_book)

def bb(*args):
    return 'Good bye'

commands = {hello:'hello',
            add:'add',
            change:'change',  
            phones:'phone',
            show_all:'show all',
            delete_phone:'delete',
            bb:'bye'}

def handler(text):
    for command,kword in commands.items():
        if text.startswith(kword):
            return command,text.replace(kword,'').strip()
    return None

def main():
    while True:
        user_input = input('>>>')
        command,data =handler(user_input)
        print(command(data))
        if command == bb:
            break

if __name__ == '__main__':
    main()