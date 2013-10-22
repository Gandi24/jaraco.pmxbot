import re

import twilio
import pmxbot
from pmxbot.core import command

@command('send_text')
def send_text(conn, event, channel, nick, rest):
	account = pmxbot.config.twilio_account
	token = pmxbot.config.twilio_token
	number, _, msg = rest.partition(' ')
	number = parse_number(number)
	if not msg: return
	msg = msg.encode('ascii')[:160]
	client = twilio.rest.TwilioRestClient(account=account, token=token)
	client.messages.create(to=number, from_="+15712573984", body=msg)
	return "Sent {count} chars to {number}".format(count=len(msg),
		number=number)

def parse_number(str):
	"""
	Strip everything but digits and + sign; ensure it begins with a country
	code.
	"""
	clean = ''.join(re.findall('[\d+]*'))
	if not clean.startswith('+'):
		clean = clean.lstrip('1')
		clean = '+1' + clean
	return clean