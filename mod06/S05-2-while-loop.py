from pprint import pprint

devices_list = [] # Create the outer list for all devices

file = open('devices','r')
line = file.readline()
while line:

    device_info_list = line.split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]

    # Now append our device and its info onto our 'devices' list
    devices_list.append(device_info)

    line = file.readline()

file.close() # Close the file since we are done with it

# Use while loop to print the results
print ''
print 'Name     OS-type  IP address           Software         '
print '------   -------  ------------------   ------------------'

index = 0
while index < len(devices_list):

    device = devices_list[index]

    print '{0:8} {1:8} {2:20} {3:20}'.format(device['name'],
                                             device['os-type'],
                                             device['ip'],
                                             device['version'])

    index += 1

print ''


