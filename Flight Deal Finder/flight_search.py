import os
import requests
from dotenv import load_dotenv

# Loading Environment Variables
load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()
    
    def _get_new_token(self):
        """
        To authenticate access requests in Amadeus
        """

        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_IATA_code(self,city):
        
        # For Authorization
        headers = {"Authorization": f"Bearer {self._token}"}

        # Parameters
        query = {
        "keyword": city,
        "max": "5",
        "include": "AIRPORTS",
        }

        response = requests.get(url=IATA_ENDPOINT,headers=headers,params=query)
        # print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return code
    
    def find_flights(self,origin_city_iata,destination_city_iata, from_time, to_time):
        
        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_iata,
            "destinationLocationCode": destination_city_iata,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "20",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            # print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n")
            # print("Response body:", response.text)
            return None
        else:
            # print ("Successful")
            return (response.json())