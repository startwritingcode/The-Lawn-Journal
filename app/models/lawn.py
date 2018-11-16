class Lawn:
    def __init__(self, name, address, total_area, unit_of_measurement):
        self.name = name
        self.address = address
        self.total_area = total_area
        self.unit_of_measurement = unit_of_measurement
    
    def serialize(self):
        return {
            'name': self.name,
            'address': self.address.__dict__,
            'total_area': self.total_area,
            'unit_of_measure': self.unit_of_measurement
        }