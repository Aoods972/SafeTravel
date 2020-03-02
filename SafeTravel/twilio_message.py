from twilio.rest import Client


def sendMessage(asid, atoken, toNumber, text):

    # Both asid and atoken are on the group chat

    # Your Account SID from twilio.com/console
    account_sid = asid
    # Your Auth Token from twilio.com/console
    auth_token = atoken

    client = Client(account_sid, auth_token)

    # toNumber needs to be registered on twilio first

    message = client.messages.create(
        to=toNumber,
        from_="+441618508564",
        body=text)

# print(message.sid)
