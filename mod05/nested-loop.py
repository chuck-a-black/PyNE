from pprint import pprint

devices_list = [] # Create the outer list for all devices

print ''
print 'Name    OS-type   IP address           Software            '
print '------- --------- -------------------- --------------------'

# Read in the devices from the file
file = open('devices','r')
for line in file:

    device_info = line.strip().split(',') # Get device info into list
    devices_list.append(device_info)

    print '{0:8} {1:8} {2:20} {3:20}'.format( device_info[0],device_info[1],
                                              device_info[2],device_info[3])

file.close() # Close the file since we are done with it
print ''

# Sit in this while loop, until the user wants to quit
while True:

    # Request user to input the device name we will search for
    try:
        name = raw_input('Enter device name to find (Ctrl-C to exit):')
    except KeyboardInterrupt:
        break;

    # Loop through our devices looking for a match on device name
    for device_info in devices_list:

        if device_info[0] == name:  # Check to see if device name is a match

            # If a match, print results and stop looking
            print '{0:8} {1:8} {2:20} {3:20}'.format( device_info[0],device_info[1],
                                                      device_info[2],device_info[3]), \
                                                      ': found match!'
            break

        else:
            print 'continuing'

    else:  # We get here if we exhausted the device list, name not found
        print '--- Given device name not found ---'

print '\n'
print 'Device search terminated.\n'
