from app.models.lawn import Lawn
from app.models.address import Address

ADDRESSES = [
    Address('123 Main St.', '', 'Chicago', 'IL', '12345', 'USA'),
    Address('555 Fifth St.', 'Apt 2', 'New York', 'NY', '12345', 'USA'),
    Address('20445 Royal Road', '', 'LONDON', 'WIP', '6HQ', 'ENGLAND'),
    Address('4545 Continental Cir', '', '', 'St Paul', '06570', 'France')
]

LAWNS = [
    Lawn('Home', ADDRESSES[0], 5000, 'sq. ft'),
    Lawn('Parents', ADDRESSES[1], 1200, 'sq. ft'),
    Lawn('Summer Home', ADDRESSES[2], 500, 'sq m'),
    Lawn('Somewhere else', ADDRESSES[3], 1000, 'sq m')
]