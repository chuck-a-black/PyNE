from pprint import pprint

device_info = [] # Create my device_info list

# Open the file and read in the single line of device info
file = open('devices','r')
file_line = file.readline().strip()

print 'read line: ', file_line # Print out the line I just read

# Here is the main part: use the string 'split' function to convert
# the comma-separated string into a list of items
device_info = file_line.split(',')

pprint(device_info) # Print out the dictionary with nice formatting

file.close() # Be a good steward of resourcs and close the file
