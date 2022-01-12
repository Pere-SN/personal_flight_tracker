import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'BCN'
sheet_data = DataManager().get_sheet_data()

n = 2

for city in sheet_data["prices"]:

    # Fill the IATA code in the sheet if it's empty
    if city["iataCode"] == "":
        DataManager().edit_row(n, FlightSearch().get_iata_code(city['city']))

    # Get data of flights for every row in the sheet
    flight = FlightSearch().get_cheap_price(o_city_code=ORIGIN_CITY_IATA,
                                            d_city_code=city['iataCode'],
                                            from_time=dt.datetime.now(),
                                            to_time=dt.datetime.now() + dt.timedelta(days=30*6))

    # Check if the price is lower than the one in the sheet and send a notification

    if flight is not None and flight.price < city['lowestPrice']:
        NotificationManager().notification(
            message=f"Only {flight.price}€ to fly from {flight.origin_city}-{flight.origin_airport} to "
            f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            f"{flight.website}"
        )

