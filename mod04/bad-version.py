current_version = 'Version 5.3.1'

# Print heading
print ''
print 'Devices with bad software versions'
print '=================================='

# Read all lines of device information from file
file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]

    # If the version doesn't match our 'current version', print out warning
    if device_info['version'] != current_version:
        print '      Device:', device_info['name'], '   Version:', device_info['version']
 
print '' # Print final blank line

file.close() # Close the file since we are done with it
