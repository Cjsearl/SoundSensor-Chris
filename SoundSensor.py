
#!/usr/bin/env python
#code edited from sunfounder.com
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import socket

SERVERIP = '10.0.0.22'

voiceValue = 0

n = 0

GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)

def loop():
	global voiceValue
	count = 0
	while True:
		voiceValue = ADC.read(0)
		if voiceValue:
			print 'Value:', voiceValue
			if voiceValue > 100:
				print "Voice detected! ", count
				count += 1
			time.sleep(0.5)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass


while True:
	global voiceValue
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((SERVERIP, 8881))
	print '%d : Connected to server' % n,
	data = "Chris, %d , " % voiceValue
	sock.sendall(data)
	print " Sent:", data
	sock.close()
	n += 1
	time.sleep(30)
