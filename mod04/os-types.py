from pprint import pprint
import re

# Print heading
print ''
print 'Counts of different OS-types for all devices'
print '============================================'

os_types = { 'Cisco IOS':    {'count':0, 'devs':[] },
             'Cisco Nexus':  {'count':0, 'devs':[] },
             'Cisco IOS-XR': {'count':0, 'devs':[] },
             'Cisco IOS-XE': {'count':0, 'devs':[] } }

# Read all lines of device information from file
file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create a dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]

    name = device_info['name'] # get the device name 
    os = device_info['os-type'] # get the OS-type for comparisons

    # Based on the OS-type, increment the count and add name to list
    if os == 'ios':
        os_types['Cisco IOS']['count'] += 1
        os_types['Cisco IOS']['devs'].append(name)

    elif os == 'nx-os':
        os_types['Cisco Nexus']['count'] += 1
        os_types['Cisco Nexus']['devs'].append(name)

    elif os == 'ios-xr':
        os_types['Cisco IOS-XR']['count'] += 1
        os_types['Cisco IOS-XR']['devs'].append(name)
 
    elif os == 'ios-xe':
        os_types['Cisco IOS-XE']['count'] += 1
        os_types['Cisco IOS-XE']['devs'].append(name)

    else:
        print "   Warning: unknown device type:", os

pprint(os_types)
print '' # Print final blank line

file.close() # Close the file since we are done with it
