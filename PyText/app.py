from twilio.rest import Client
import config

client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

call = client.messages.create(
    to="8801943029170",
    from_="+17175029894",
    body="This is a test message"
)

print(call)
