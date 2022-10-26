from urllib.request import  urlopen


import  json
import  time


READ_API_KEY='E3F844Q8H2YL6TPB7'
CHANNEL_ID='1771037'

while True:
    TS=urlopen("https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2".format(CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    data=json.loads(response.decode('utf-8'))

    print(data)

    print(data["feeds"][1]["field1"])
    a=data["feeds"][1]["field1"]
    print(a)


    TS.close()