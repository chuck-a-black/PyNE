devices_list = [] # Create the outer list for all devices

# Read in the devices from the file
file = open('devices','r')
for line in file:

    device_info_list = line.split(',') # Get device info into list
    devices_list.append(device_info_list)

file.close() # Close the file since we are done with it

print ''
print 'Name     OS-type    IP address           Software            '
print '-------  ---------  -------------------  --------------------'

ip_addresses = set()

# Go through the list of devices, printing out values in nice format
for device in devices_list:

    print '{0:8} {1:10} {2:20} {3:20}'.format(device[0],device[1],device[2],device[3]),

    # Print 'duplicate' if IP address exists for another device
    if device[2] in ip_addresses:
        print '*Duplicate IP!*'
        continue

    ip_addresses.add(device[2])
    print ''

print ''
