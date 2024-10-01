
class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Will be responsible for containing the cheapest flight up to that point
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(all_flights):
    
    # If no data is present then can return N/A
    if all_flights is None or not all_flights['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    ### Information regarding the FIRST Flight
    first_flight = all_flights['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    
    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in all_flights["data"]:
        price = float(flight["price"]["grandTotal"])

        if price < lowest_price: # Meaning we found a cheaper flight
            lowest_price = price

            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
    
    return cheapest_flight
