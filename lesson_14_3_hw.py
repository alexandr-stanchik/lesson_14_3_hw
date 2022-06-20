class Building:
    def __init__(self, floor, windows, doors):
        self.floor = floor
        self.windows = windows
        self.doors = doors

    def build(self):
        print(f'The house was built')

    def populate(self):
        print(f'The house was populated')

    def demolish(self):
        print(f'The house was demolished')


class BeautySalonMixin:
    min_price = 100 
    
    @classmethod
    def manic(cls):
        return cls.min_price + cls.min_price * 0.20
	
    @classmethod
    def haircut(cls, value):
        if value < 30:
        	return cls.min_price + cls.min_price * 0.20
        elif 30 <= value <= 50:
        	return cls.min_price + cls.min_price * 0.50
        elif value > 50:
        	return cls.min_price + cls.min_price * 0.80

    def salon_opening_hours(self, time):
        if self.open_time < time < self.close_time:
            return "салон открыт"
        return "салон закрыт"

    def set_timework(self, timeopen, timeclose):
        self.open_time = timeopen
        self.close_time = timeclose


class HouseWithSalon(Building, BeautySalonMixin):
    def __init__(self, floor, windows, doors):
        super().__init__(floor, windows, doors)
        self.open_time = None
        self.close_time = None


if __name__ == "__main__":
    hws = HouseWithSalon(2, 2, 2)
    hws.set_timework(10, 22)
    print(f'{hws.manic() = }')
    print(f'{hws.haircut(20) = }')
    print(f'{hws.haircut(40) = }')
    print(f'{hws.haircut(60) = }')