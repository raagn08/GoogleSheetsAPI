# GoogleSheetsAPI

### Use this snippet to generate a pickle file associated with the mentioned SCOPE(s)

```
#Define your scopes here
SCOPE  = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds  =  None
if os.path.exists('token.pickle'):
with  open('token.pickle', 'rb') as  token:
	creds  = pickle.load(token)
	
# If there are no (valid) credentials available, let the user log in.
if  not  creds  or  not  creds.valid:
	if  creds  and  creds.expired and  creds.refresh_token:
		creds.refresh(Request())
	else:
		flow  = InstalledAppFlow.from_client_secrets_file( 'credentials.json', SCOPE)
		creds  =  flow.run_local_server(port=0)
		# Save the credentials for the next run
		with  open('token.pickle', 'wb') as  token:
			pickle.dump(creds, token)