from flights.abs_flight import AbsFlight


class AbsDecorator(AbsFlight):
    def __init__(self, trip):
        self._trip = trip

    @property
    def trip(self):
        return self._trip