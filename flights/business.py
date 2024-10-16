from flights.abs_flight import AbsFlight


class Business(AbsFlight):
    @property
    def cost(self):
        return 1025

    @property
    def description(self):
        return "Business class. Mid-way spoils"

    @property
    def in_flight_amenities(self):
        return 'Chapagne before depature and a selection of movies'