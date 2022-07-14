from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

# from event import event_body
from request_body.event import event_body

class Calendar:

    def __init__(self, credentials_file, token_file):
        self.credentials_file = credentials_file
        self.token_file = token_file

    def connect(self):

        #==================creating or refreshing token file=============#
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
       
        with open(self.token_file, 'w') as token:
            token.write(creds.to_json())

        #========================creating service==========================#
        try:
            self.calendar = build('calendar', 'v3', credentials=creds)

        except HttpError as error:
            print(error)


    def create_event(self, name, start_time, end_time, description, location):

        #I have to create a function to manipulate event_body fields

        event = self.calendar.events().insert(calendarId='primary', body=event_body).execute()
        print ('Event created: %s' % (event.get('htmlLink')))


    def list_events(self):
        
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Listing the upcoming 10 events')
        events_result = self.calendar.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])