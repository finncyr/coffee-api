import falcon
import subprocess
import json

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

		resp.status = falcon.HTTP_201
		resp.media = 'Coffee for User is brewing!'
app = falcon.API()
app.add_route('/info', SystemInfoRessource())
app.add_route('/brew', brewMeCoffee())
