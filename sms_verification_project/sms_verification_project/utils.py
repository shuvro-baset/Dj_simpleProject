import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body=f'Hi your user and verification code is : {user_code}!',
        from_='+16783746416',
        to=f'{phone_number}'
    )

    print(message.sid)