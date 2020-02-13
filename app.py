import requests
import falcon
import subprocess

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



app = falcon.API()
app.add_route('/info', SystemInfoRessource())
