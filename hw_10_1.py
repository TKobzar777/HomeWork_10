from collections import UserDict


class Field:
    def __init__(self, value:str)-> None:
        self.value = value
        #self.fl = None
        
    def __str__(self) -> str:
        return self.value
        
    
class Name(Field):
    ...


class Phone(Field):
    def __eq__(self, value: object) -> bool:
        return self.value == value.value
    
    # def __eq__(self, __value: object) -> bool:
    #     return self.value == __value.value
    ...


class Record:
    def __init__(self, name:Name, phone: Phone | None = None)->None:
        self.name = name 
        self.list_phones = [phone] if phone else []

    def __str__(self):
        return f'Name {self.name} - list phones: {" ,".join([str(pn) for pn in self.list_phones]) if self.list_phones else "no phone"}'
            
    def add_phone(self, phone:Phone)->str:
        if phone not in self.list_phones:
            self.list_phones.append(phone)
            return f'Phone number {phone}  added to the sonnact {self.name}'
        return f'Phone number {phone} already exists' 
    
    def find_phone(self, phone:Phone)->str:
        for pn in self.list_phones:
            if pn == phone:
                return f'Phone number {phone} is in contact {self.name}'
        return f'Phone number {phone} isn\'t in contact {self.name}'
    
    def edit_phone(self, phone: Phone, new_phone: Phone) -> str:
        if all((phone in self.list_phones, phone != new_phone)):
            self.list_phones[self.list_phones.index(phone)] = new_phone
            return f"Phone number {phone} change to {new_phone} for contact {self.name}"
        return f"Phone {phone} not in phones or {phone} = {new_phone}" 

    def delete_phone(self, phone:Phone):
        list_temp=[]
        for pn in self.list_phones:
            if pn == phone:
                str_result = 'Phone number {phone} delete'
            list_temp.append(pn) 
        self.list_phones = list_temp     
        return str_result


class AddressBook(UserDict):
    def add_record(self, record:Record)->str:
        self.data[record.name.value] = record
        return f'Add new record {record} to Address Book'
 
    def delete_record(self, record:Record)->str:
        self.pop(record.name.value)
        return f'Delete {record} to Address Book'
    
    # def find(self, record:Record) -> str:
    #     return self.get(record.name.value)

    def find(self, name:str) -> Record|None:
        record = self.get(name)
        return record if record else None   
    
if __name__ == "__main__":

    '''Checking Class Description'''
    book = AddressBook()

    john_record = Record(Name("John"))
    john_record.add_phone(Phone("1234567890"))
    john_record.add_phone(Phone("1234567890"))
    john_record.add_phone(Phone("5555555555"))   

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record(Name("Jane"))
    jane_record.add_phone(Phone("9876543210"))
    print(jane_record)
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(john)

    print(john.edit_phone(Phone("1234567890"), Phone("1112223333")))

    for name, record in book.data.items():
        print(record)
    
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone(Phone("5555555555"))
    print(found_phone)
    print(book.delete_record(book.find("Jane")))



