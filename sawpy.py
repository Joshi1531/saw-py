import requests
import requests.auth


#basicAuth = requests.auth.HTTPBasicAuth('user', 'pass')
#requests.get(
#    url='',
#    auth = basicAuth
#)

class setup:
    def __init__(self, username : str, password : str):
        self.user = username
        self.password = password
    
    def test(self):
        return "Success"
    
    def kurs_waehlen(self, name : str):
        #res = requests.get()
        print('\033[95m' + "- - - - - - - - - - - STATUS - - - - - - - - - - -")
        print('\033[93m' + "Status - Request ... - PENDING")
        print('\033[92m' + "Status - Request ... - SUCCESS")
        print('\033[91m' + "Status - Request ... - ERROR")
        return True