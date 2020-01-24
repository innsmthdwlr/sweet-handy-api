import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Auth:

    def __init__(self, this_directory, SCOPES):
        self.this_directory = this_directory
        self.SCOPES = SCOPES

    def get_credentials(self):
        creds = None
        # token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time
        secrets_path = os.path.join(self.this_directory, '.credentials')
        token_path = os.path.join(secrets_path, 'token.pickle')
        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)

        # if there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                secrets_file = os.path.join(secrets_path, 'googledrive.json')
                flow = InstalledAppFlow.from_client_secrets_file(
                    secrets_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # save the credentials for the next run
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)
        return creds
