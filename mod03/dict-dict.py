from pprint import pprint

devices = {} # Create the outer dictionary for all devices

file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary for device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]

    # Print out what we have read and built so far
    print 'device_info: ', device_info

    # Now place our device and its info onto our 'devices' list
    devices[device_info['name']] = (device_info)

# Done with all lines in the file; now print the results
pprint(devices)

file.close() # Close the file since we are done with it
