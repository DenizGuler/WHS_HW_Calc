
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Python Data'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# Gets a range of values using 'Sheet1!(range)' range is in the format of 'A1:B2'
def get(range):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1Dnt8QajzCWO8bIW8dzkm-4UJy6Tve9cwuhCC8Ijc_RQ'
    # Range: B column is class names, D column is class data
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=range).execute()

    values = result.get('values', [])
    return values

# Converts two ranges into one dict(key, value)
def toDict(key, val):
    keys = []
    vals = []
    values = get(key)
    for row in values:
        keys.append(row[0])
        #print(row[0])
    values = get(val)
    for row in values:
        vals.append(row[0])
        #print(vals)
    return dict(zip(keys, vals))

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    values = get('Sheet1!B8:D10')

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        print(toDict('Sheet1!B8:B10','Sheet1!D8:D10'))
        for row in values:
            # Print to console. Row 0 is column B; 2 is D
            print('%s, %s' % (row[0], row[2]))


if __name__ == '__main__':
    main()
