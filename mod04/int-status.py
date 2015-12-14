import re

# Print heading
print ''
print 'Interfaces with possible problems'
print '-----------------------------------------------------------------'

# Read all lines of device information from file
file = open('interfaces','r')
for line in file:

    int_info_list = line.split() # Get interface info into list

    # Put interface information into dictionary for this interface
    int_info = {} # Create the inner dictionary of device info
    int_info['name'] = int_info_list[0]
    int_info['int-state'] = int_info_list[1]
    int_info['linep-state'] = int_info_list[2]
    int_info['bw'] = int_info_list[5]

    if int_info['int-state'] == 'up' and int_info['linep-state'] != 'up':
        print 'Interface: ' + int_info['name'] + ': line protocol state is ' + int_info['linep-state']
 
print '' # Print final blank line

file.close() # Close the file since we are done with it
