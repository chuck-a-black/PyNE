from pprint import pprint
import re

# Print heading
print ''
print 'Lines without any routes and interfaces'
print '---------------------------------------'

# Create regular expression to match Gigabit interface names
gig_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

routes = {} # Create dictionary to hold number of routes per interface

# Read all lines of IP routing information
file = open('ip-routes','r')
for line in file:

    match = gig_pattern.search( line ) # Match for Gigabit Ethernet

    # Check to see if we matched the Gig Ethernet string
    if match:
        intf = match.group(2) # get the interface from the match
        routes[intf] = routes[intf]+1 if intf in routes else 1
    else:
        print '  No matching interface:' + line,

print ''
print 'Number of routes per interface'
print '------------------------------'
pprint(routes)
print '' # Print final blank line
