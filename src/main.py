#! usr/local/bin/python3

from g_calendar import Calendar

def main():

    calendar = Calendar('./token/credentials.json', './token/token.json')
    calendar.connect()

    print('==========My Notes==========\n\n')

    while(True):

        operation = int(input('Choose one operation\n-> 0 - exit\n-> 1 - notes\n-> 2 - calendar\n-> 3 - to do list\n\n>'))

        if not operation:
            break


        elif operation == 1:
            print('note tab')
        

        elif operation == 2:
            calendar.list_events()
            print('\ncalendar tab')
        

        elif operation == 3:
            print('to do list tab')
        

        else:
            ('Invalid operation. Choose another one!')
    
        
if __name__ == '__main__':
    main()