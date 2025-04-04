
from  data_manager import DataManager
from flight_search import FlightSearch

data_manager =  DataManager()
sheet_data = data_manager.get_destination_data()

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet data: \n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

