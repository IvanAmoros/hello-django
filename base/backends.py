# backends.py
from social_core.backends.oauth import BaseOAuth2
import requests  # Add this import

class Slug42OAuth2(BaseOAuth2):
	name = 'oauth2-42'
	AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
	ACCESS_TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
	ACCESS_TOKEN_METHOD = 'POST'
	REDIRECT_STATE = False
	ID_KEY = 'id'  # Update this to the correct field in the 42 API response

	def get_user_id(self, details, response):
		return response.get('id')  # Update this to the correct field in the 42 API response

	def get_user_details(self, response):
		return {
			'username': response.get('login', ''),
			'email': response.get('email', ''),
			'first_name': response.get('first_name', ''),
			'last_name': response.get('last_name', ''),
		}

	def user_data(self, access_token, *args, **kwargs):
		url = 'https://api.intra.42.fr/v2/me'
		headers = {'Authorization': f'Bearer {access_token}'}

		# Make the request to fetch user data
		response = requests.get(url, headers=headers)
		response.raise_for_status()

		# Parse and return the user data
		return response.json()
