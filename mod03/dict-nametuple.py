from collections import namedtuple
from pprint import pprint

Dev_info = namedtuple('Dev_info',['name', 'os', 'ip', 'user', 'password'])

devices = {}

file = open('devices','r')
for line in file:
    device_info = Dev_info(*(line.strip().split(',')))
    print 'Device Information: ', device_info
    devices[device_info.name] = device_info

pprint(devices)
