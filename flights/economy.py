from flights.abs_flight import AbsFlight


class Economy(AbsFlight):
    @property
    def cost(self):
        return 150

    @property
    def description(self):
        return "Economy class. Our best offer"

    @property
    def in_flight_amenities(self):
        return 'A selection of movies and limited drinks and snacks'