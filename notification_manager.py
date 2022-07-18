from twilio.rest import Client

TWILIO_SID = "AC953fad4d1f04f40890f9d71f2a675c31"
TWILIO_AUTH_TOKEN = "df640e10aa18522dcba8975b7ecbc4bf"
TWILIO_VIRTUAL_NUMBER = "+18647327884"
TWILIO_VERIFIED_NUMBER = MY NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
