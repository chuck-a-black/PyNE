from pprint import pprint

# Open the file and read in the single line of device info
file = open('devices','r')
file_line = file.readline().strip()

print 'read line: ', file_line # Print out the line I just read

# 'split()' will provide is with a python list, which we convert to a tuple
device_info = tuple(file_line.split(','))

pprint(device_info) # Print out the tuple with nice formatting

file.close() # Be a good steward of resourcs and close the file
