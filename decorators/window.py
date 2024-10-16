from decorators.abs_decorator import AbsDecorator


class Window(AbsDecorator):
    @property
    def cost(self):
        return self.trip.cost + 50

    @property
    def description(self):
        return self.trip.description + ' and a window seat'
