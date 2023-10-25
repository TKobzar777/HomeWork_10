from hw_10_1 import Name, Phone, Record, AddressBook 

import string

class PhoneAlreadyExistsError(Exception):
    pass

class RecordError(Exception):
    pass

class ChoiceError(Exception):
    pass

global address_book 
address_book = AddressBook()

# dict_phone = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Try again'
        except ValueError:
            return 'Phon nomber is not correct. Try again'
        except KeyError:
            return 'There is no entry in the phone book that contains that parameter.'
        except PhoneAlreadyExistsError:
            return 'Phone already exists'
        except RecordError:
            return r'There is no corresponding entry in the phone book!'
        except ChoiceError:
            return 'Wrong choice.Try again'
        
    return inner

def search_record_name(name:str)-> Record|None:
    if address_book.get(name):
        return address_book.get(name)
    return None
    
def search_record_phone(phone:str)-> Record|None:
    for _, record in address_book.items():
        if record.search_phone_in_record(phone):
            return record
    return None

def serch_on_param(str_param:str)-> Record|bool:
    record = search_record_name(str_param)
    #print(record)
    if record:
        return record
    record = search_record_phone(str_param)
    if record:
        return record
    return False



@input_error
def add_contact(*args)->str:
    name = Name(str(args[1]))
    phone = Phone(str(args[2]))

    if address_book.get(args[1]):    
        record = address_book.get(args[1])
        if not record.search_phone_in_record(args[2]):
            record = address_book.get(args[1])
        else:
            #return "phone already exists"
            raise PhoneAlreadyExistsError          
    else:
        record = Record(name)  

    if int(args[2]):
        record.add_phone(phone)
        address_book.add_record(record)
        return address_book[name.value]
    


def search_oll_param(*args) ->Record|None:
    #print(len(args))

    if (len(args))==0:
        return None
    i=1
    while i < len(args):
        record = serch_on_param(args[i])
        i+=1
        #print(record)
        if record:
            return record
        
    return None




@input_error
def edit_contact(*args) -> str:

    record = search_oll_param(*args)
    if not record:
        return 'There is no entry in the phone book that contains that parameter'
    print(record)
    print('Select a command from the list:\n'\
            '\tedit phone - 1\n'\
            '\tdelete phone -2\n'\
            '\tchange name- 3\n')
    while True:
        user_input= int(input('<<<< '))
        if user_input == 1:
            phone = input('<<<< input phone ')
            new_phone = input('<<<< input new phone ')
            return record.edit_phone(phone, new_phone)
        elif user_input == 2:
            phone = input('<<<< input phone ')
            return record.delete_phone(phone)
        elif user_input == 3:
            new_name = input('<<<< input new name ')
            record_temp = record
            address_book.delete_record(record)
            record_temp.name.value = new_name
            print(address_book.add_record(record_temp))
            return 'Name is changed'
        else:
            raise ChoiceError
 

        
def delete_contact(*args) ->str:
    record = search_oll_param(*args)
    if record:
        txt_result = f'{record} - DELETE!'
        address_book.delete_record(record)
        return f'{txt_result}'
    else: 
        return 'There is no entry in the phone book that contains that parameter'
    
 

# @input_error
def search_record(*args):
    record = search_oll_param(*args)
    if record:
        return sorted(record)
    else:
        return 'No record was found on these parameters!'




@input_error
def print_phone(*args):

    if search_record_phone(args[1]):
        return search_record_phone(args[1])
    else:
        return f'{args[1]} - this phone was not found in the phone book '
  

@input_error
def change_phon(*args)->str:
    record = search_oll_param(args[1],args[2])
    if record:
        return record.edit_phone(args[2], args[3])
    return 'There is no entry in the phone book that contains that parameter'
  
        
def show_all()->str: 

    if address_book:   
        for _, record in address_book.items():
            print(record)        
        return 'The address book is printed out!'
    return 'The address book is empty'    

def help_cla():
    return 'Command Line Interface\n'\
        'I will help you with your phone book\n'\
        'List of commands you can use:\n'\
        '\tHELLO - greeting\n'\
        '\tADD (name and phone number separated by space) - add a phonebook entry\n'\
        '\tDELETE (name or phone) - delete a contact\n'\
        '\tSEARCH (name or phone) - contact search by name or name\n'\
        '\tCHANGE (name or phone) -change contact\n'\
        '\tSHOW ALL -displays all saved contacts with phone numbers in the console\n'\
        '\tGOOD BYE, CLOSE, EXIT - shutdown\n'\
        '\tHELP - Displays this alarm in the console\n'\
        'The bot is not sensitive to the register of commands entered\n'\
        'Success in your work!'
        
def command_parser(stp_user_input)->str:
    list_user_input=stp_user_input.split()
        
    if list_user_input[0].lower() == 'hello':
        return 'How can I help you?'
    
    if list_user_input[0].lower() == 'help':
        return help_cla()
    
    if list_user_input[0].lower() == 'show'and list_user_input[1].lower() == 'all':
        return show_all()
        
    if list_user_input[0].lower() == 'add':
        return add_contact(*list_user_input)
    
                
    if list_user_input[0].lower() == 'search':
        return search_record(*list_user_input)       
        
 
    if list_user_input[0].lower() == 'delete':
        return delete_contact(*list_user_input)
        
       
        
    if list_user_input[0].lower() == 'change':
        return edit_contact(*list_user_input)
        
    if list_user_input[0].lower() == 'close' or list_user_input[0].lower() == 'exit'or (list_user_input[0].lower() == 'good' and list_user_input[1].lower() == 'bye'):
        return'Good bye!'
    return 'The command is not correct'    




def create_dict():
    
    add_contact('add', 'tttttt', '1111111111')
    add_contact('add', 'aaaaaaa', '222222222')
    add_contact( 'add', 'bbbbbb', '3333333')
    add_contact('add', 'ccccccc', '44444444')
    add_contact( 'add', 'ddddddd', '555555555')
    add_contact('add', 'tttttt', '67676767')


def main():
    create_dict()
    print(help_cla())
    show_all()
    
    #print(delete_phone("3333334"))

    while True:
        stp_user_input= input('<<<< ')
        result_str = command_parser(stp_user_input)
        print(result_str)
        #show_all()
        if result_str == 'Good bye!':
            break



if __name__ == "__main__":
     main()