import re

# Print heading
print ''
print 'Devices and their Management IP addresses'
print '========================================='

# Create regular expression to find the Mgmt IP address
ip_addr_pattern = re.compile('Mgmt:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# Read all lines of device information from file
file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]

    # Find the Mgmt IP address from the line in the file, and put it into device_info
    mgmt_addr = ip_addr_pattern.search(line)
    device_info['ip'] = mgmt_addr.group(1)

    print '      Device:', device_info['name'], '   Mgmt IP:', device_info['ip']
 
print '' # Print final blank line

file.close() # Close the file since we are done with it
