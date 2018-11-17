from app.models.lawn import Lawn
from app.models.address import Address

def buildLawn(lawn_dict):
    lawn_name = lawn_measure = address1 = address2 = city = state = zip = country = ''
    lawn_area = 0

    if 'name' in lawn_dict:
        lawn_name = lawn_dict['name']
    if 'total_area' in lawn_dict:
        lawn_area = lawn_dict['total_area']
    if 'unit_of_measure' in lawn_dict:
        lawn_measure = lawn_dict['unit_of_measure']
    if 'address1' in lawn_dict['address']:
        address1 = lawn_dict['address']['address1']
    if 'address2' in lawn_dict['address']:
        address2 = lawn_dict['address']['address2']
    if 'city' in lawn_dict['address']:
        city = lawn_dict['address']['city']
    if 'state' in lawn_dict['address']:
        state = lawn_dict['address']['state']
    if 'zip' in lawn_dict['address']:
        zip = lawn_dict['address']['zip']
    if 'country' in lawn_dict['address']:
        country = lawn_dict['address']['country']
    
    address = Address(address1, address2, city, state, zip, country)
    lawn = Lawn(lawn_name, address, lawn_area, lawn_measure)

    return lawn