import falcon
import subprocess
import json
import brew

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
	@falcon.before(max_body(64 * 1024))
	def on_post(self, req, resp):
		try:
			user = req.media.get('user')
			key  = req.media.get('key')

		except AttributeError:
			raise falcon.HTTPBadRequest('Missing thing', 'You need to submit something xD')

		with open("secret.json", "r") as read_file:
			userdata = json.load(read_file)

		if not(key = userdata["secret"]):
			raise falcon.HTTPBadRequest('Bro you are not allowed to use dem coffee maschine!')
		else:
			"""START BREWING BOI"""

		resp.status = falcon.HTTP_201
		resp.media = 'Coffee for User {} is brewing!'.format(user)

app = falcon.API()
app.add_route('/info', SystemInfoRessource())
