from cars.business import Business
from cars.economy import Economy
from cars.first import First
from decorators.early_boarding import EarlyBoarding
from decorators.window import Window


def main():
    # set trip = Business(), Economy() or First()
    trip = Business()
    showflight(trip)
    trip = Window(trip)
    showflight(trip)
    trip = EarlyBoarding(trip)
    showflight(trip)


def showflight(car):
    print(car.description, car.cost)


if __name__ == '__main__':
    main()