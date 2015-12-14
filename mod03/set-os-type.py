from collections import namedtuple
from pprint import pprint

Dev_info = namedtuple('Dev_info',['name', 'os_type', 'ip', 'user', 'password'])

os_types = set()

file = open('devices','r')
for line in file:

    device_info = Dev_info(*(line.strip().split(',')))
    print 'Device Information: ', device_info

    if device_info.os_type not in os_types:
        os_types.add(device_info.os_type)

pprint(os_types)
