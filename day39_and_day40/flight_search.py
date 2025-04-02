import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR_API_KEY_HERE"


class FlightSearch:

    def get_destination_code(self, city_name):
       loaction_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
       headers = {
           "apikey": TEQUILA_API_KEY
       }
       query = {
           "term": city_name,
           "location_types": "city"
       }
       response = requests.get(url=loaction_endpoint, headers=headers, params=query)
       results = response.json()["locations"]
       iata_code = results[0]["code"]
       return iata_code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=search_endpoint, headers=headers, params=query)

        try:
            data = response.json()["data"][0]
            return data
        except IndexError:
            print(f"No flights found for {origin_city_code} to {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
