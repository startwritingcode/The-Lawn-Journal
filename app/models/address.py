class Address:
    def __init__(self, address1 = '', address2 = '', city = '', state = '', zip = '', country = ''):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
    
    def deserialize(address_dict):
        return Address(address_dict['address1'], address_dict['address2'], address_dict['city'], address_dict['state'], address_dict['zip'], address_dict['country'])