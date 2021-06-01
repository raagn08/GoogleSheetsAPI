import pickle
from googleapiclient import discovery
from googleapiclient.errors import HttpError

class GoogleSheets():

    def __init__(self, spreadsheetId, GAUTH=None, cache_discovery=False):
        if GAUTH is None:
            #Attempt to read Google OAuth Credentials Pickle file // will raise FileNotFoundError if no token file is available
            with open('token.pickle', 'rb') as token:
                GAUTH = pickle.load(token)
        self.spreadsheetId = spreadsheetId
        self.service = discovery.build('sheets', 'v4', credentials=GAUTH, cache_discovery=cache_discovery)

    def append(self, range, data, majorDimension="ROWS", valueInputOption="USER_ENTERED"):
        """
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
        ------------------------
        ranges: str
            "Example!A1:Z1"
        data: list
            [["0"], ["1"]...]
        majorDimensions: str
            "ROWS" (default) / "COLUMNS"
        valueInputOption: str
            "USER_ENTERED"(default) / "RAW"
        """
        try:
            response = self.service.spreadsheets().values().append(
                spreadsheetId = self.spreadsheetId,
                range = range,
                body = {
                    "majorDimension": majorDimension,
                    "values": data
                },
                valueInputOption = valueInputOption
            ).execute()
        
        except HttpError as e:
            print(e)
            


    def batchGet(self, ranges, valueRenderOption="UNFORMATTED_VALUE"):
        """
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet
        ------------------------
        ranges: list
            ["Example!A1:Z1", ...]
        valueRenderOption: str
            "FORMATTED_VALUE"(default) / "UNFORMATTED_VALUE" / "FORMULA"
        """
        try:
            response = self.service.spreadsheets().values().batchGet(
                spreadsheetId = self.spreadsheetId,
                ranges = ranges,
                valueRenderOption = valueRenderOption
            ).execute()

            return response.get('valueRanges', [])
        except HttpError as e:
            self.retries=0
            print(e)
            

    def batchUpdate(self, data):
        """
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
        ------------------------
        requestBody: dict
            requestBody
        """
        try:
            response = self.service.spreadsheets().values().batchUpdate(
                spreadsheetId = self.spreadsheetId,
                body = data
            ).execute()
        except HttpError as e:
            print(e)
            

    def batchSheetUpdate(self, data):
        """
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
        ------------------------
        requestBody: dict
            requestBody
        """
        try:
            response = self.service.spreadsheets().batchUpdate(
                spreadsheetId = self.spreadsheetId,
                body = data
            ).execute()
        
        except HttpError as e:
            print(e)

    def batchClear(self, range):
        """
        https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchClear
        ------------------------
        range: list
            ["Example!A1:Z1", ...]
        """
        try:
            response = self.service.spreadsheets().values().batchClear(
                spreadsheetId = self.spreadsheetId,
                body = {
                    'ranges': range
                }
            ).execute()
        except HttpError as e:
            self.retries=0
            print(e)
