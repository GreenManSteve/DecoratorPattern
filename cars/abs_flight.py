import abc

class AbsFlight(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def cost(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass