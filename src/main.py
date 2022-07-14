#! usr/local/bin/python3

from g_calendar import Calendar
import os

def main():

    calendar = Calendar('./token/credentials.json', './token/token.json')
    calendar.connect()

    print('==========My Notes==========\n')

    while(True):

        operation = int(input('Choose one operation\n-> 0 - exit\n-> 1 - notes\n-> 2 - calendar\n-> 3 - to do list\n\n> '))
        os.system('clear')

        if not operation:
            break


        elif operation == 1:
            print('note tab')
        

        elif operation == 2:

            while (True):
                
                option = int(input('Choose an option:\n0 - back\n1 - list events\n2 - create event\n\n> '))    
                os.system('clear')

                if not option:
                    break

                elif option == 1:
                    calendar.list_events()
                    i = input('\npress ENTER to continue')
                    os.system('clear')

                elif option == 2:
                    
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

                    calendar.create_event(name, start_date, end_date, start_time, end_time, description, location)

                    i = input('press ENTER to continue')
                    os.system('clear')

                else:
                    print('Invalid operation, choose another one!\n')


        elif operation == 3:
            print('to do list tab')
        
        else:
            print('Invalid operation. Choose another one!\n')
    

if __name__ == '__main__':
    main()