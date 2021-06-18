from os import PRIO_PROCESS


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, price, from_city, from_airport, to_city, to_airport, leave_date, return_date):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.leave_date = leave_date
        self.return_date = return_date
