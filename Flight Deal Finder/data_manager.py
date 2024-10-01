import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


# Loading Environment Variables
load_dotenv()


SHEETY_ENDPOINT = "https://api.sheety.co/d1b8f138f22cb09e4c23bee45b1efa79/flightDeals/prices"
                        
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        # Authentication
        self._username = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._username, self._password)

        # Stores Sheet Data
        self.destinations_data = {}
    
    def get_data(self):
        """
        This gets the data from the Google Sheet and returns it (GET Request)
        """
        response = requests.get(SHEETY_ENDPOINT)
        # response.raise_for_status()
        data = response.json()
        self.destinations_data = data["prices"]
        return self.destinations_data
    

    def add_IATA_codes(self):
        """
        This adds the IATA Codes onto the Google Sheet (PUT Request)
        """
        for row in self.destinations_data:
            add_data = {
                "price":{
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}", json=add_data)
            # print(response.text)
