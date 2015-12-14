import pexpect

routes_list = [] # Create the list of routes

session = pexpect.spawn('ssh cisco@198.18.1.30', timeout=20)
result = session.expect(['password:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print 'Timout or unexpected reply from device'
    exit()

# Successfully got password prompt, enter password now
session.sendline('cisco')
session.expect('#')

print 'going into admin mode'
session.sendline('admin')
result = session.expect('#')

print 'setting terminal length 0'
session.sendline('terminal length 0')
result = session.expect('#')

print 'exiting admin mode'
session.sendline('exit')
result = session.expect('#')

print 'show ip route'
session.sendline('show ip route')
result = session.expect('#')

print 'getting ip route command output'
show_ip_route_output = session.before

print show_ip_route_output

