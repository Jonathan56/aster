import spacecraft as sc


class Factory(object):
    def __init__(self, colony, name):
        self.sim = colony.sim
        self.colony = colony

        # Initialize factory parameters
        self.production = colony.set_initial(name, 'production')
        self.rate = colony.set_initial(name, 'rate')


class Propellant(Factory):
    def __init__(self, colony):
        super(Propellant, self).__init__(colony, 'propellant_factory')

        # Start factory
        self.sim.env.process(self.start())

    def start(self):
        while True:
            yield self.sim.env.timeout(self.rate)
            yield self.colony.propelant_container.put(self.rate)


class Booster(Factory):
    def __init__(self, colony):
        super(Booster, self).__init__(colony, 'booster_factory')

        # Start factory
        self.sim.env.process(self.start())

    def start(self):
        while True:
            yield self.sim.env.timeout(self.rate)
            for index in range(0, self.production):
                yield self.colony.booster_storage.put(sc.Booster(self.sim))


class Tank(Factory):
    def __init__(self, colony):
        super(Tank, self).__init__(colony, 'tank_factory')

        # Start factory
        self.sim.env.process(self.start())

    def start(self):
        while True:
            yield self.sim.env.timeout(self.rate)
            for index in range(0, self.production):
                yield self.colony.tank_storage.put(sc.Tank(self.sim))


class Heartofgold(Factory):
    def __init__(self, colony):
        super(Heartofgold, self).__init__(colony, 'heartofgold_factory')

        # Start factory
        self.sim.env.process(self.start())

    def start(self):
        while True:
            yield self.sim.env.timeout(self.rate)
            for index in range(0, self.production):
                yield self.colony.heartofgold_storage.put(sc.Heartofgold(self.sim))