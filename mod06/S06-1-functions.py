devices_list = [] # Create the outer list for all devices

#---- Function to read device information from file -------------------
def read_device_info():

    # Read in the devices from the file
    file = open('devices','r')
    for line in file:

        device_info_list = line.split(',') # Get device info into list
        devices_list.append(device_info_list)

    file.close() # Close the file since we are done with it

#---- Function to go through devices printing them to table -----------
def print_device_info():

    print ''
    print 'Name     OS-type  IP address           Software         '
    print '------   -------  ------------------   ------------------'

    # Go through the list of devices, printing out values in nice format
    for device in devices_list:

        print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
                                                 device[2],device[3])

    print ''

#---- Main: read device info, then print ------------------------------
read_device_info()
print_device_info()
