# WAY2SMS Free Python API
> Now also verify mobile number as email, do cool stuff with it.


## Features
	- Free sms api
	- 100% delivery guarantee

## Limitations
	- you can write 140 characters in single message

## Installation
	``` pip install messanger ```


All you need to write is,

```
import messanger

# Mobile number registered in way2sms website.
phone = '+919409567000'

# Password in way2sms website.
password = ''

# Receiver mobile number.
receiver = '+14529959578'

# Text message that you want to send
message = """Hey Donald Trump,
Can write a python program which can send free text messages
"""

messanger.send(phone, password, receiver, message)
```

# Note
	- Don't try that number, Donald Trump doesn't owns it.
