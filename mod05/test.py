import pexpect

eoutes_list = [] # Create the list of routes

print ''
print 'IP route output'
print '----------------------------------------------------'

# Read ip route info from device
session = pexpect.spawn('ssh cisco@198.18.1.30', timeout=20)
result = session.expect(['password:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print 'Timout or unexpected reply from device'
    exit()

# Successfully got password prompt, enter password now
session.sendline('cisco')
session.expect('#')
# Check for failure
if result != 0:
    print "didn't get '#'"
    exit()


print 'going into admin mode...'
session.sendline('admin')
result = session.expect('(admin)#')
# Check for failure
if result != 0:
    print "didn't get 'admin"
    exit()

print 'setting terminal length'
session.sendline('terminal length 0')
result = session.expect('(admin)#')
# Check for failure
if result != 0:
    print "didn't get 'admin after setting terminal length"
    exit()

print 'going back out of admin mode...'
session.sendline('exit')
result = session.expect('#')
# Check for failure
if result != 0:
    print "didn't exit out of admin mode"
    exit()


print 'Successfully connected to device, logged in, got prompt'
session.sendline('show ip route')
session.expect('#')
