from pprint import pprint

devices_list = [] # Create the outer list for all devices
index = 0

print ''
print 'Name    OS-type   IP address           Software            '
print '------- --------- -------------------- --------------------'

# Read in the devices from the file
file = open('devices','r')
for line in file:

    device_info = line.strip().split(',') # Get device info into list
    devices_list.append(device_info)

    index += 1  # increment the index of this device in the list
    print '{0:3}: {1:8} {2:8} {3:20} {4:20}'.format(index,
                                                    device_info[0],device_info[1],
                                                    device_info[2],device_info[3])

file.close() # Close the file since we are done with it
print ''

while True:
    index = raw_input('Enter selected device: ')

    if index > 0 and index <= len(devices_list):
        device = devices_list[index-1]  # don't forget list indexes are zero-based
    else:
        break

    print '{0:3}: {1:8} {2:8} {3:20} {4:20}'.format(index,
                                                    device_info[0],device_info[1],
                                                    device_info[2],device_info[3])

print 'Terminated by user, value out of range'
