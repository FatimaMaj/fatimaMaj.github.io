from __future__ import print_function
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle
import datetime

# find the directory that the Python script is located in
current_dir = os.path.dirname(__file__)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def find_conflicts(events):
    conflictsList = []
    for idx1, eventA in enumerate(events['items']):
        for idx2, eventB in enumerate(events['items']):
            # this condition is to avoid comparing the same pair
            if idx1 >= idx2:
                continue
            # condition to check is there conflict between two events
            if eventA['start']['date'] <= eventB['end']['date'] and eventB['start']['date'] <= eventA['end']['date']:
                if (eventA['summary'] not in conflictsList):
                    conflictsList.append(eventA['summary'])
                if (eventB['summary'] not in conflictsList):
                    conflictsList.append(eventB['summary'])
    return conflictsList


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(current_dir + '/token.pickle'):
        with open(current_dir + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                current_dir + '/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(current_dir + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    conflicts = find_conflicts(events_result)  # events_result
    print('conflicts', conflicts)

    return conflicts

if __name__ == '__main__':
    main()
