import requests

i = 0

def send():
    global i 
    i += 1
    URL = "http://www.google.com"

    headers = {"Accept": "application/json; indent=4"}
    print("Sending Done For Request:" + str(i))
    response = requests.get(URL)
    send()

send()
