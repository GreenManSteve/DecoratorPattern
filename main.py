from flights.business import Business
from flights.economy import Economy
from flights.first import First
from decorators.early_boarding import EarlyBoarding
from decorators.window import Window


def main():
    # set trip = Business(), Economy() or First()
    trip = Economy()
    showflight(trip)
    trip = Window(trip)
    showflight(trip)
    trip = EarlyBoarding(trip)
    showflight(trip)

    trip = Business()
    showflight(trip)
    trip = Window(trip)
    showflight(trip)
    trip = EarlyBoarding(trip)
    showflight(trip)

    trip = First()
    showflight(trip)
    trip = Window(trip)
    showflight(trip)
    trip = EarlyBoarding(trip)
    showflight(trip)


def showflight(trip):
    print('Flight details: {} | Cost: £{}'.format(trip.description, trip.cost))


if __name__ == '__main__':
    main()