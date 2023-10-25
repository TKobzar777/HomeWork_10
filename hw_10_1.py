from collections import UserDict


class Field:
    def __init__(self, value:str)-> None:
        self.value = value
        self.fl = None
        
    def __str__(self) -> str:
        return self.value
        
    
class Name(Field):
    fl = True

class Phone(Field):
    fl = False


class Record:
    def __init__(self, name:Name)->None:
        self.name = name 
        self.list_phones = []

    def __str__(self):
        return f'{self.name} - list phones = {[str(pn) for pn in self.list_phones]}'
            
    def add_phone(self, phone:Phone):
        self.list_phones.append(phone)
        return self
        #return f'Номер телефона добавлен {self.name} -- {self.list_phones}' 
    
    def search_phone_in_record(self, phone:str)->bool:

        for pn in self.list_phones:
            if str(phone) == str(pn.value):
                return True
        return False
    
    def edit_phone(self, phone:str, new_phone:str)-> str:
        temp_list_phone = []
        str_result =''
        for ph in self.list_phones:
            print(ph.value)
            print(phone)
            if ph.value != phone:
                temp_list_phone.append(ph)
            else:
                print(temp_list_phone.append(Phone(new_phone)))
                str_result += f'Замена {phone} --> {new_phone}\n'
        self.list_phones = temp_list_phone
        if not str_result:
            return f'{phone} не найден'
        return str_result
    

    def delete_phone(self, phone:Phone):
        temp_list_phone = []
        str_result =''
        for ph in self.list_phones:
            if ph.value != phone:
                temp_list_phone.append(ph)
            else: 
                str_result += f'{phone} is delete'
        self.list_phones = temp_list_phone

        if not str_result:
            return f'{phone} телефон не найден'
        return str_result



class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record
        

    def delete_record(self, record:Record):
        return(self.pop(record.name.value))

