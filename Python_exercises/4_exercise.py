class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    def play_music(self):
        print("Music playing")


class ElectricMixin:
    def start(self):
        print("Battery OK")
        super().start()


class AutopilotMixin:
    def start(self):
        print("Sensors calibrated")
        super().start()


class Tesla(AutopilotMixin, ElectricMixin, Car):
    pass


t = Tesla()
t.start()
t.play_music()