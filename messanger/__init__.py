import requests
from lxml import html

def send(phone, password, receiver, message):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}

	response = requests.post('http://www.way2sms.com/re-login',
		data=dict(
			mobileNo=phone,
			password=password,
			CatType='',
		),
		headers=headers,
	)

	cookies = response.cookies.get_dict()

	headers['Cookie'] = '; '.join([f'{key}={value}' for key, value in cookies.items()])

	response = requests.get('http://www.way2sms.com/send-sms', headers=headers)

	selector = html.fromstring(response.content)
	token = selector.xpath('//input[@id="Token"]/@value')
	token = token[0] if token else ''

	if not token:
		return send(phone, password, receiver, message)

	response = requests.post('http://www.way2sms.com/smstoss', headers=headers, data=dict(
		Token=token,
		message=message,
		toMobile=receiver,
		ssaction='undefined',
	))

	return response.content
