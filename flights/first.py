from flights.abs_flight import AbsFlight


class First(AbsFlight):
    @property
    def cost(self):
        return 2500

    @property
    def description(self):
        return "First class. All the spoils"

    @property
    def in_flight_amenities(self):
        return 'Unlimited everything'