from decorators.abs_decorator import AbsDecorator


class EarlyBoarding(AbsDecorator):
    @property
    def cost(self):
        return self.trip.cost + 25

    @property
    def description(self):
        return self.trip.description + ' . Includes fast track boarding'