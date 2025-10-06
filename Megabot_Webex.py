import requests

bot_token = 'NTM1N2JkYjMtZmQ0Zi00NDVkLTk1MTEtMWRmODFkODlhN2Y0MTQ3YTFiYjUtNDA0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
room_id = 'b35f7fc0-8d91-11f0-82c5-731be99413a5'
message = 'Hello from my Webex bot!'

headers = {
    'Authorization': f'Bearer {bot_token}',
    'Content-Type': 'application/json'
}

data = {
    'roomId': room_id,
    'text': message
}

response = requests.post('https://webexapis.com/v1/messages', headers=headers, json=data)

if response.status_code == 200:
    print('Message sent successfully')
else:
    print(f'Failed to send message: {response.status_code} {response.text}')