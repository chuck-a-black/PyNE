from pprint import pprint

devices = [] # Create the outer list for all devices

file = open('devices','r')
for line in file:

    device_info = tuple(line.strip().split(',')) # Get device info into tuple

    # Print out what we have read and built so far
    print 'device_info: ', device_info

    # Now append our device and its info onto our 'devices' list
    devices.append(device_info)

# Done with all lines in the file; now print the results
pprint(devices)

file.close() # Close the file since we are done with it
