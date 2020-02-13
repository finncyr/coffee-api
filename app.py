import falcon
import subprocess
import json
from os import uname
import time
#import RPi.GPIO as GPIO
class SystemInfoRessource:
	def on_get(self, req, resp):
		"""Handles GET Request"""
		resp.status = falcon.HTTP_200

		uptime = subprocess.Popen('uptime', stdout=subprocess.PIPE)
		uptime_out, uptime_err = uptime.communicate()
		
		answer = {
			'uptime': uptime_out, 
			'creator': 'finncyr',
			'code': 'https://github.com/finncyr/coffee-api'
			}

		resp.media = answer

class brewMeCoffee:
	def on_post(self, req, resp):
		try:
			key  = req.media.get('key')

		except AttributeError:
			raise falcon.HTTPBadRequest('Missing thing', 'You need to submit something xD')

		with open("secret.json", "r") as read_file:
			userdata = json.load(read_file)

		if not(key == userdata["secret"]):
			raise falcon.HTTPBadRequest('Bro you are not allowed to use dem coffee maschine!')
		else:
			print("BOB, BREW SOMETHING!")
			brewCoffee()


		resp.status = falcon.HTTP_201
		resp.media = 'Coffee for User is brewing!'
app = falcon.API()
app.add_route('/info', SystemInfoRessource())
app.add_route('/brew', brewMeCoffee())


def brewCoffee():

    if(uname()[4][:3] == 'arm'):
      #  GPIO.setmode(GPIO.BCM)
      print("This is ARM")
      #  GPIO.setup(23, GPIO.OUT)
      #  GPIO.output(23, GPIO.HIGH)
      #  time.sleep(0.325)
      #  GPIO.output(23. GPIO.LOW) 
    else:
        print("SIMULATED GPIO 23: On")
        time.sleep(0.325)
        print("SIMULATED GPIO 23: Off")