import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
HEADERS = {"apikey": os.environ['KIWI_TOKEN']}


class FlightSearch:
    @staticmethod
    def get_iata_code(city_name: str):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        code_search = requests.get(url=location_endpoint, params=query, headers=HEADERS).json()
        return code_search['locations'][0]['code']

    @staticmethod
    def get_cheap_price(o_city_code, d_city_code, from_time, to_time):
        query = {
            "fly_from": o_city_code,
            "fly_to": d_city_code,
            "date_from ": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR",
        }

        flight_search = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=HEADERS)

        try:
            data = flight_search.json()['data'][0]
        except IndexError:
            print(f"No flights found for {d_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            website=''
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data
