from pprint import pprint

device_info = {} # Create my device_info dictionary

# Open the file and read in the single line
file = open('devices','r')
file_line = file.readline().strip()

print 'read line: ', file_line # Print out the line I just read

# Here is the main part: use the string 'split' to create a list
# of items that are separated by commas
device_info_list = file_line.split(',')

# Now put those items from the list into our dictionary
device_info['name'] = device_info_list[0]
device_info['os-type'] = device_info_list[1]
device_info['ip'] = device_info_list[2]
device_info['username'] = device_info_list[3]
device_info['password'] = device_info_list[4]

pprint(device_info) # Print out the dictionary with nice formatting

file.close() # Be a good steward of resources and close the file
