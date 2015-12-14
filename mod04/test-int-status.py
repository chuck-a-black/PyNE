import re

input_string = """ Lo0          up          up           Loopback  1500          0
                   Nu0          up          up               Null  1500          0
          Mg0/0/CPU0/0          up        down               ARPA  1514          0
             Gi0/0/0/0          up          up               ARPA  1514    1000000
             Gi0/0/0/1          up        down               ARPA  1514      10000
             Gi0/0/0/2        down        down               ARPA  1514      10000
"""

# Print heading
print ''
print 'Interfaces with possible problems'
print '------------------------------------------------------------'

# Read all lines of device information from string
for line in input_string.splitlines():

    int_info_list = line.split() # Get interface info into list

    # Put interface information into dictionary for this interface
    int_info = {} # Create the inner dictionary of device info
    int_info['name'] = int_info_list[0]
    int_info['int-state'] = int_info_list[1]
    int_info['linep-state'] = int_info_list[2]
    int_info['bw'] = int_info_list[5]

    if int_info['int-state'] == 'up' and int_info['linep-state'] != 'up':
        print '    Interface: ' + int_info['name'] + ': line protocol state is ' + int_info['linep-state']
 
print '' # Print final blank line
