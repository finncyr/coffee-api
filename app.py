import requests
import falcon

class TestGetFunction:
	def on_get(self, req, resp):
		"""Handles GET Request"""
		resp.status = falcon.HTTP_200
		
		answer = {
			'message': (
				"I was GETted!" 
				),
			'origin': 'finncyr'
			}

		resp.media = answer

app = falcon.API()
test = TestGetFunction()
app.add_route('/test', test)
