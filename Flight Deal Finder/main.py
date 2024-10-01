
import time
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

### Adding the IATA Codes for each Row
for row in sheet_data:
    if row["iataCode"] == "" or row["iataCode"] == "Not Found":
        row["iataCode"] = flight_search.get_IATA_code(row["city"])

# print(sheet_data)

#### Adding the new rows to the Google Sheet
# data_manager.add_IATA_codes()


### Searching for Flights
ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for row in sheet_data: # Each row represents one destination
    print(f"\nFor {row["city"]}: ")
    # 'flights' stores all the information regarding every flight going from origin to 
    # destination in the next 6 months
    flights = flight_search.find_flights(
        origin_city_iata = ORIGIN_CITY_IATA,
        destination_city_iata =row["iataCode"],
        from_time = tomorrow,
        to_time = six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{ORIGIN_CITY_IATA} to {row['city']} Round Trip: ${cheapest_flight.price}")
    time.sleep(2)

    ### Send Whatsapp Message if a cheaper flight was found
    if cheapest_flight.price != "N/A" and cheapest_flight.price < row["lowestPrice"]:

        print(f"Lower price flight found to {row['city']}!")

        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
            f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )





