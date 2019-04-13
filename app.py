import messanger

# Mobile number registered in way2sms website.
phone = '9409567085'

# Password in way2sms website.
password = '9409567085'

# Receiver mobile number.
receiver = '9099330013'

# Text message that you want to send
message = """Hey Donald Trump,
Can write a python program which can send free text messages
"""

messanger.send(phone, password, receiver, message)
