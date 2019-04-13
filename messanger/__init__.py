import requests
from lxml import html

def send(phone, password, receiver, message):
	with requests.Session() as s:
		headers = {
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest',
			'Origin': 'https://www.way2sms.com',
			'Referer': 'https://www.way2sms.com/'
		}

		response = s.post('http://www.way2sms.com/re-login',
			data=dict(
				mobileNo=phone,
				password=password,
				CatType='',
				redirectPage='',
				pid=''
			),
			headers=headers,
		)

		response = s.get('http://www.way2sms.com/send-sms', headers=headers)

		selector = html.fromstring(response.content)
		token = selector.xpath('//input[@id="Token"]/@value')

		if not token:
			return send(phone, password, receiver, message)

		response = s.post('http://www.way2sms.com/smstoss', headers=headers, data=dict(
			Token=token[0],
			message=message,
			toMobile=receiver,
			ssaction='undefined',
			senderId='WAYSMS'
		))

		return response.content
