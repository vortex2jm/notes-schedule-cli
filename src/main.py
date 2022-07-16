#! usr/local/bin/python3

from g_calendar import Calendar
from db import DataBase
from dotenv import load_dotenv
from pprint import pprint
import os

DOTENV = "./token/.env"
TOKEN = "./token/token.json"
CREDENTIALS = "./token/credentials.json" 

def main():
    
    load_dotenv(DOTENV)

    # Google calendar connection
    calendar = Calendar(CREDENTIALS, TOKEN)
    calendar.connect()

    # database connection
    db = DataBase(os.getenv("username"), os.getenv("password"))
    db.connect()

    # client
    print('==========My Notes==========\n')
    while(True):

        operation = int(input('Choose one operation\n-> 0 - exit\n-> 1 - notes\n-> 2 - calendar\n-> 3 - to do list\n\n> '))
        os.system('clear')

        # Exit
        if not operation:
            break
        
        # notes
        elif operation == 1:
            
            while (True):

                option = int(input('Choose an option:\n0 - back\n1 - view all notes\n2 - create new note\n3 - delete a note\n\n> '))

                if not option:
                    os.system('clear')
                    break
                
                elif option == 1:
                    db.show_table(1)

                    action = int(input('\n0 - back\n1 - delete'))
                    
                    if action == 1:
                            print('delete')

                    os.system('clear')

                #waiting for functions
        

        # google calendar
        elif operation == 2:

            while (True):

                option = int(input('Choose an option:\n0 - back\n1 - list events\n2 - create event\n\n> '))    
                os.system('clear')

                # back to previous menu
                if not option:
                    break
                
                # list events
                elif option == 1:
                    
                    events = calendar.list_events()
                    action = int(input('\n0 - back\n1 - delete an event\n\n> '))

                    # delete an event
                    if action == 1:
                        if events:
                            y = int(input('\nChoose which event do you want to delete: '))
                            calendar.delete_event(events[y-1]['id'])
                            input('\npress ENTER to continue')
                        else:
                            print('You have no events to delete')
                            input('\npress ENTER to continue')

                    os.system('clear')
                
                # create an event
                elif option == 2:
                    
                    # getting and manipulating data
                    name = str(input('event name -> '))
                    start_date = str(input('start date -> '))
                    start_time = str(input('start time (hh:mm) -> '))
                    end_date = str(input('end date -> '))
                    end_time = str(input('end time (hh:mm) -> '))
                    description = str(input('description -> '))
                    location = str(input('location -> '))

                    start_date = start_date.split('/')
                    start_date = f'{start_date[2]}-{start_date[1]}-{start_date[0]}'

                    end_date = end_date.split('/')
                    end_date = f'{end_date[2]}-{end_date[1]}-{end_date[0]}'

                    # creating
                    calendar.create_event(name, start_date, end_date, start_time, end_time, description, location)

                    i = input('press ENTER to continue')
                    os.system('clear')

                # if operation do not exists
                else:
                    print('Invalid operation, choose another one!\n')

        # to do list
        elif operation == 3:
            print('to do list tab')
        
        # if operation do not exists
        else:
            print('Invalid operation. Choose another one!\n')
    

if __name__ == '__main__':
    main()