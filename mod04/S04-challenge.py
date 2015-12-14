from pprint import pprint
import re

# Print heading
print ''
print 'Interfaces, routes list, routes details'
print '---------------------------------------'

# Create regular expressions to match interfaces and IS-IS L2
iL2_pattern = re.compile('^i L2')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

# Create regular expressions to match prefix and routes
prefix_pattern = re.compile('^i L2 ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

intf_routes= {} # Create dictionary to hold number of routes per interface

# Read all lines of IP routing information
file = open('ip-routes','r')
for line in file:

    iL2_match = iL2_pattern.search(line)
    if iL2_match:

        intf_match = intf_pattern.search( line ) # Match for Gigabit Ethernet

        # Check to see if we matched the Gig Ethernet string
        if intf_match:

            intf = intf_match.group(2) # get the interface from the match

            if intf not in intf_routes: # If route list not yet created, do so now
                intf_routes[intf] = []

            # Extract the prefix (destination IP address/subnet)
            prefix_match = prefix_pattern.search(line)
            prefix = prefix_match.group(1)

            # Extract the route
            route_match = route_pattern.search(line)
            next_hop = route_match.group(1)

            # Create dictionary for this route, and add it to the list
            route = {'prefix':prefix,'next-hop':next_hop}
            intf_routes[intf].append(route)

pprint(intf_routes)
print '' # Print final blank line
