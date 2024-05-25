import requests

channelID = input("[REQUIRED] Please Enter The ChannelID You Want To Send It Too: ")
content = input("[REQUIRED] Please Enter The Message You Want To Send: ")
token = input("[REQUIRED] Please Input Your Token: ")
Times = input("[REQUIRED] Times You Want To Send The Message: ")

url = "https://discord.com/api/v9/channels/%s/messages" % channelID

payload = {
    "content": content
}

headers = { 
    "Authorization": token
}

for i in range(Times):
    res = requests.post(url, payload, headers=headers)
    print(res)
