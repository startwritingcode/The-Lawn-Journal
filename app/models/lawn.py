from app.models.address import Address

class Lawn:
    def __init__(self, name, address = Address(), total_area = 0, unit_of_measurement = ''):
        self.id = ''
        self.address = address
        self.name = name
        self.total_area = total_area
        self.unit_of_measurement = unit_of_measurement
    
    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'address': {
                'address1': self.address.address1,
                'address2': self.address.address2,
                'city': self.address.city,
                'state': self.address.state,
                'zip': self.address.zip,
                'country': self.address.country
            },
            'total_area': self.total_area,
            'unit_of_measure': self.unit_of_measurement
        }