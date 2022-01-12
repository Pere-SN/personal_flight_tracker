from twilio.rest import Client
import os
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phonenumber = os.environ['TWILIO_PN']
my_phonenumber = os.environ['VERIFIED_TWILIO_PN']


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def notification(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_phonenumber,
            to=my_phonenumber
        )
        print(message.sid)
